try:
	from amzsear.consts import *
except ImportError:
	from .consts import *

from lxml import html
import requests

try:
	from urllib.parse import quote
except ImportError:
	from urllib import quote
import re
from functools import reduce

def getItem(query_string,page_num,item_num):

	(products,url) = getSearchPage(query_string,page_num=page_num)
	try:
		item = products[item_num]
	except KeyError:
		raise ValueError('The item number %s could not be found on page %s' % (item_num,page_num))

	url = item['url']
	if 'ref=' in url:
		url += OUT_URL_TAG
	else:
		url += OUT_URL_REF

	return ({item_num:item},url)


def getSearchPage(query_string,page_num):
	(cont,url) = getHtmlUrl(query_string,page_num=page_num)
	products = getProducts(cont)
	return (products,url)

def getProducts(content):
	tree = html.fromstring(content)
	products = {}

	results = tree.xpath('//li[contains(@id,"result_")]')

	for res in results:
		num = res.xpath('./@id')[0]
		num = str(num)
		num = num.rsplit('_',1)[-1]
		num = int(num)

		name = res.xpath('.//*[self::h2 or self::span]/@data-attribute')
		url = res.xpath('.//a[h2]/@href')

		if len(name) > 0 and len(url) > 0:
			name = str(name[0])	
			url = str(url[0])

			if url.startswith('/'):
				url = SITE_URL + url

			rating = [x.text for x in res.xpath('.//*[contains(@class,"a-icon-star")]/span')]

			rows = res.xpath('.//div[@class="a-column a-span7" or @class="s-item-container"]/div[contains(@class,"a-row")]')
			temp_title = DEFAULT_PRICE_TEXT
			prices = {}
			for row in rows:
				get_title = [x.text for x in row.xpath('.//h3')]
				get_prices = row.xpath('.//span/@aria-label')
	
				if len(get_title) > 0:
					temp_title = get_title[0]
				elif len(get_prices) > 0:
					prices[temp_title] = get_prices
					temp_title = DEFAULT_PRICE_TEXT
	
			products[num] = {
				'name' : name,
				'url' : url,
				'prices' : prices,
				'rating' : rating[0] if len(rating) > 0 else ''
			}
	
	return products

def getHtmlUrl(query_string,page_num=1):
	url = BASE_URL % (quote(query_string),page_num)
	req = requests.get(url,headers=URL_HEADERS)

	if not req.ok:
		raise ValueError('The requested page could not be found')

	return (req.content.decode('utf8', errors='ignore'),url)

def getCleanPrices(price_dict):

	price_texts = reduce(lambda a, b: a + b[1],price_dict.items(),[])
	price_texts = reduce(lambda x, y: x + y.split('-'),price_texts,[])

	out_prices = []
	for text in price_texts:
		val = float(re.sub('[^\d.]','',text))
		out_prices.append(val)



	return sorted(out_prices)

def getRatingValue(text):
	val = text.split()

	try:
		int_val = float(val[0])
		return int_val
	except:
		return 0

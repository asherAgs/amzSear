try:
	from amzsear.consts import *
	from amzsear.api import getItem,getSearchPage,getCleanPrices,getRatingValue
except ImportError:
	from .consts import *
	from .api import getItem,getSearchPage,getCleanPrices,getRatingValue

import sys
import webbrowser

def getKwargs(args):
	options = {'q':False,'d':True,'v':False}
	ignore = []

	for i in range(0,len(args)):
		arg = args[i]
	
		if i not in ignore:
			if args[i] not in ['-p','-i','-q','-d','-v']:
				raise ValueError('Invalid argument')
			else:
				val = args[i][1:]
				if val in ['q','d','v']:
					options[val] = not options[val]	
				else:
					try:
						num = int(args[i+1])
						options[val] = num
						ignore.append(i+1)
					except:
						raise ValueError('Invalid argument')

	translate = {'i':'item_number','p':'page_number',
				 'q':'quiet','d':'open_url','v':'print_all_info'}
	out = {}

	for name,val in options.items():
		out[translate[name]] = val

	return out


def client(query_string,page_number=1,item_number=None,
	   quiet=False,open_url=False,print_all_info=False):

	if item_number != None:
		(products,url) = getItem(query_string,page_num=page_number,item_num=item_number)
	else: 
		(products,url) = getSearchPage(query_string,page_number)

	if open_url:
		webbrowser.open(url)
	if not quiet:	
		printProducts(products,print_all_info)


def printProducts(products,print_all_info=False):
	if not print_all_info:
		print("{: >4} {: <55} {: >6}    {: >5}".format('','Name','Price','Rating'))
	
	for count in sorted(products.keys()):
		if print_all_info:
			## Print all info scraped
			
			name_text = "{: <4} {}".format(count,products[count]['name'])
			url_text = '{: >10} {}'.format('Url:',str(products[count]['url']))
			print(shortenText(name_text))
			print(shortenText(url_text))

			for name,values in products[count]['prices'].items():
				for price in values:
					print("{: >10} {: >20} {: >40}".format('Price:',name,price))
			print("{: >10} {: >20} {: >40}".format('Rating:','',products[count]['rating']))	
			print('')
		else:
			## Print info in table format

			price = getCleanPrices(products[count]['prices'])
			if len(price) > 0:
				price_text = '${:,.2f}'.format(price[0])
			else:
				price_text = ""

			star_rating = '*' * int(round(getRatingValue(products[count]['rating'])))
			print("{: <4} {: <55}  {: <7}   {: >5}".format(count,products[count]['name'][:55],
				price_text,star_rating))


def shortenText(text):
	col_size = MAX_COL_SIZE

	if len(text) > col_size:
		return text[:col_size] + '...'
	else:
		return text

def run():
	if len(sys.argv) < 2 or sys.argv[1].startswith('-'):
		print("Usage: amzsear query_string [-p num [-i num]] [-q] [-v] [-d]")
		exit(1)

	kws = getKwargs(sys.argv[2:])

	query = sys.argv[1]

	client(query,**kws)

if __name__ == '__main__':
	run()

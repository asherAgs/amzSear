import re

try:
    from amzsear.core.AmzBase import AmzBase
    from amzsear.core import requires_valid_data, capture_exception, build_url
    from amzsear.core.AmzRating import AmzRating
except ImportError:
    from .amzsear.core.AmzBase import AmzBase
    from .amzsear.core import requires_valid_data, capture_exception, build_url
    from .amzsear.core.AmzRating import AmzRating
"""
    The AmzProduct class extends the AmzBase class and, as such the following
    attributes are available to be called as an index call or as an attribute:

        title (str): The name of the product.
        product_url (str) A url directly to the product's Amazon page.
        image_url (str) A url to the product's default image.
        rating (AmzRating) An AmzRating object.
        prices (dict) A dictionary of prices, with the price type as a key and
          a string for the price value (see get_prices method to get float values).
        extra_attributes (dict) Any extra information that can be extracted
          from the product.
        subtext (list) A list of strings under the title, typically the author's
          name and/or the date of publication.

    This class should usually not be instantiated directly (rather be used in
    an (AmzSear object) but can be created by passing an HTML element to
    the constructor. If nothing is passed, an empty AmzProduct object is
    created.

    Optional Args:
        html_element (LXML root): A root for an HTML tree derived from an element on an Amazon search page.
"""
class AmzProduct(AmzBase):
    title = None
    product_url = None
    image_url = None
    rating = None
    prices = None
    extra_attributes = None 
    subtext = None

    _all_attrs = ['title','product_url','image_url','rating','prices',
        'extra_attributes', 'subtext']

    def __init__(self, html_element=None):
        if html_element != None:
            html_dict = self._get_from_html(html_element)
            for k,v in html_dict.items():
                setattr(self, k, v)
            if len(html_dict) > 0:
                self._is_valid = True

    """
        Private method - used in to initialise fields from HTML

        Returns:
            dict: A dict of fields with extracted data
    """
    @capture_exception(IndexError,default={})
    def _get_from_html(self, root):
        d = {}

        title_root = [x for x in root.cssselect('a') if len(x.cssselect('h2')) > 0][0]
        d['title'] = ''.join([x.text_content() for x in title_root.cssselect('h2')])
        d['product_url'] = build_url(title_root.get('href'))
        for elem in title_root.getparent().getparent().cssselect('div[class="a-row a-spacing-none"]'):
            temp_subtext = ''.join([x.text_content() for x in elem.cssselect('span[class*="a-size-small"]')])
            if len(temp_subtext) > 0:
                d['subtext'] = d.get('subtext',[]) + [temp_subtext]


        d['image_url'] = root.cssselect('img[src]')[0].get('src')
        d['rating'] = AmzRating(root) or None

        d['prices'] = {}
        price_names = root.cssselect('h3[data-attribute]')
        price_text = root.cssselect('span[class^="a"]')
        price_text = filter(lambda x: re.match('^[^a-z\-]+$',str(x.text)) and
            re.search('[\.\,]',str(x.text)) and re.search('\d',str(x.text)), price_text)

        for i, el in enumerate(price_text):
            if i >= len(price_names):
                price_key = str(len(d['prices'])) # defaults to a number if no name for price type
            else:
                price_key = price_names[i].text
            d['prices'][price_key] = el.text

        extras = root.cssselect('div[class="a-fixed-left-grid-inner"] > div > span')
        extras = [re.sub('\s+',' ', x.text_content().strip()) for x in extras]
        d['extra_attributes'] = dict(list(zip(extras,extras[1:]))[::2])

        # _index is not used explicitly in _all_attrs but can be referenced elsewhere
        d['_index'] = root.get('id','').split('_')[-1]

        # clean up before returning
        return dict(map(lambda k: (k, d[k].strip() if isinstance(d[k],str) else d[k]), d)) 


    """
        Gets a list of floats from the dictionary of price text. A key can be passed
        to explicitly specify the prices to select. If the key is None, all prices keys
        are used.

        Optional Args:
            key (str or list): A key or list of keys to in the price dictionary.

        Returns:
            list: List of floats for the subset of price specified.
    """
    @requires_valid_data(default=[])
    def get_prices(self, key=None):
        keys = []
        if key == None:
            keys = self.prices.keys()
        elif isinstance(key,list):
            keys = key
        else:
            keys = [key]

        prices = []
        for k in keys:
            if k not in self.prices:
                raise KeyError(k)
            prices += [re.sub(',','',x) for x in re.findall('[\d.,]+', self.prices[k])]

        return sorted(map(float,prices))


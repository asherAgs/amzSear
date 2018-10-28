from urllib import parse

try:
    from amzsear.core.consts import (QUERY_BUILD_DICT, BASE_URL, DEFAULT_REGION,
        REGION_CODES, SEARCH_URL)
except ImportError:
    from .amzsear.core.consts import (QUERY_BUILD_DICT, BASE_URL, DEFAULT_REGION,
        REGION_CODES, SEARCH_URL)


"""
    Decorator for valid data in an object, returns default if not valid
"""
def requires_valid_data(default=None):
    def funcParams(f):
        def funcWrapper(self,*args,**kws):
            if hasattr(self, '_is_valid') and self._is_valid == True:
                return f(self,*args,**kws)
            else:
                return default
        return funcWrapper
    return funcParams



"""
    Decorator to capture exception and pass a default instead
"""
def capture_exception(error, default=None):
    def funcParams(f):
        def funcWrapper(*args,**kws):
            try:
                return f(*args, **kws)
            except error:
                return default
        return funcWrapper
    return funcParams


"""
    Builds a url based on a query
"""
def build_url(url=None, query='', page_num=1, region=DEFAULT_REGION):
    if url == None:
        #build from query, page_num and region
        base = build_base_url(region)
        url = SEARCH_URL % (base, query, page_num)

    if url.startswith('/'):
        url =  build_base_url(region) + url 

    parsed_obj = parse.urlparse(url)
    query_dict = parse.parse_qs(parsed_obj.query)

    #update the query dict
    query_dict.update(QUERY_BUILD_DICT)

    parsed_obj = parsed_obj._replace(query=parse.urlencode(query_dict, doseq=True)) 
    return parsed_obj.geturl()


"""
    Builds URL based on region
"""
def build_base_url(region=DEFAULT_REGION):
    find_region = region.upper()
    if find_region not in REGION_CODES.keys():
        raise ValueError('%s is not a know Amazon region' % (repr(region)))

    return BASE_URL + REGION_CODES[find_region]

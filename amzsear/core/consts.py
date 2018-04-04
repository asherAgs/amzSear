#Defaults
REPR_MAX_LEN_DEFAULT = 90

#URL CODES
REGION_CODES = {
    'AU': '.com.au',
    'BR': '.com.br',
    'CA': '.ca',
    'CN': '.cn',
    'DE': '.de',
    'ES': '.es',
    'FR': '.fr',
    'IN': '.in',
    'IT': '.it',
    'JP': '.co.jp',
    'MX': '.com.mx',
    'NL': '.nl',
    'SG': '.com.sg',
    'UK': '.co.uk',
    'US': '.com'
}

DEFAULT_REGION = "US"

#URL Building
BASE_URL = 'https://www.amazon'
URL_ADDONS = {'headers': {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) '
                           'AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/60.0.3112.113 Safari/537.36'}}
GAT_ID = 't' + 'ag'
QUERY_BUILD_DICT = {GAT_ID : 'alhs-20'}

SEARCH_URL = '%s/s/ref=nb_sb_noss?sf=qz&keywords=%s&ie=UTF8&unfiltered=1&page=%s' 

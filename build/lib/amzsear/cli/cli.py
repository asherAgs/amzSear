try:
    from amzsear import AmzSear
    from amzsear.core.consts import DEFAULT_REGION, REGION_CODES
except ImportError:
    from .amzsear import AmzSear
    from .amzsear.core.consts import DEFAULT_REGION, REGION_CODES

import argparse
import webbrowser
import json
import sys
import csv

"""
"""
def run(*passed_args):
    parser = get_parser()
    args = parser.parse_args(*passed_args) # the parser defaults to sys args if nothing passed
    args = vars(args)

    amz_args = {x:y for x,y in args.items() if x not in ['item','output','dont_open']}
    out = AmzSear(**amz_args)

    if args['item'] != None:
        # single item selection
        prod = out[args['item']]
        out = AmzSear(products=[prod]) # error raised if not found
        out._urls = [prod.product_url] 


    # handle output types
    if args['output'] == 'short':
        print_short(out)
    if args['output'] == 'verbose':
        print_verbose(out)
    elif args['output'] == 'csv':
        print_csv(out)
    elif args['output'] == 'json':
        print_json(out)
    # elif args['output'] == 'quite' --> no output


    if args['dont_open'] != True:
        for url in out._urls:
            webbrowser.open(url)



def get_parser():
    parser = argparse.ArgumentParser(description='The unofficial Amazon search CLI')

    parser.add_argument('query', type=str, help='The query string to be searched')
    parser.add_argument('-p','--page', type=int,
        help='The page number to be searched (defaults to 1)', default=1)
    parser.add_argument('-i','--item', type=str,
        help='The item index to be displayed (relative to the page)', default=None)
    parser.add_argument('-r','--region', type=str, choices=REGION_CODES,
        default=DEFAULT_REGION, help='The amazon country/region to be searched')

    parser.add_argument('-d','--dont-open', action='store_true',
        help='Stop the page from opening in the default browser')

    parser.add_argument('-o','--output', type=str, choices=['short','verbose','quiet','csv','json'],
        default='short', help='The output type to be displayed (defaults to short)')

    return parser


def print_csv(cls):
    # flattens to list of dicts with index value
    data = [{**v.to_dict(flatten=True),**({'_index' : k})} for k,v in cls.items()]

    # print with all quotes
    writer = csv.DictWriter(sys.stdout, data[0].keys(), quoting=csv.QUOTE_ALL) 
    writer.writeheader()
    writer.writerows(data)

def print_json(cls):
    print(json.dumps({k: v.to_dict() for k,v in cls.items()}))

def print_verbose(cls):
    print(cls)


def print_short(cls):
    fields = ['','Title','Prices','Rating']

    rows = [{f:f for f in fields}]
    for index, product in cls.items():
        temp_dict = {}

        temp_dict[''] = index

        # get price in format '$nn.nn-$mm.mm'
        price_tup = {product.prices[k]:product.get_prices(k) for k in product.prices}
        if len(price_tup) > 0:
            price_tup = (min(price_tup, key=lambda x: price_tup[x]), max(price_tup, key=lambda x: price_tup[x]))
            if price_tup[0] == price_tup[-1]:
                temp_dict['Prices'] = price_tup[0] # one price
            else:
                temp_dict['Prices'] = price_tup[0] + ' - ' + price_tup[-1] # range of prices
        else:
            temp_dict['Prices'] = '------------'
        temp_dict['Title'] = product.get('title','----------')[:50] # limit title length
    
        temp_dict['Rating'] = product.get('rating','-----')
        if temp_dict['Rating'] != '-----':
            temp_dict['Rating'] = temp_dict['Rating'].get_star_repr()

        rows.append(temp_dict)

    format_str = []
    for field in fields:
        #get longest in each field into format_str
        format_str.append('{:%d}' % (max(len(x[field]) for x in rows)+ 1))
    format_str = ' '.join(format_str)

    for row in rows:
        print(format_str.format(*[row.get(x,'') for x in fields])) # print in order

if __name__ == '__main__':
    run()

# amzSear

The unofficial Amazon Product CLI & API. Easily search the amazon product directory from the command line without the need for an Amazon API key.

Wondering about about an amazon product listing? Find the amzSear!

__Version 2 has been released!__ See [below](#whats-new) for more info.


```
$ amzsear 'Harry Potter Books'
```


```
    Title                                               Prices             Rating
0   Harry Potter Paperback Box Set (Books 1-7)          $21.20 - $52.99    *****
1   Harry Potter and the Sorcerer's Stone               $0.00 - $10.99     *****
2   Harry Potter And The Chamber Of Secrets             $0.00 - $10.99     *****
3   Harry Potter And The Goblet Of Fire                 $0.00 - $12.99     *****
4   Harry Potter and the Prisoner of Azkaban            $0.00 - $10.99     *****
5   Harry Potter And The Order Of The Phoenix           $0.00 - $12.99     *****
6   Harry Potter and the Deathly Hallows (Book 7)       $0.00 - $14.99     *****
7   Harry Potter and the Half-Blood Prince (Book 6)     $0.00 - $12.99     *****
8   [Sponsored]Hudson James & the Baker Street Legacy   $0.00 - $3.07      -----
9   [Sponsored]Kids' Travel Guide - London: The fun wa  $8.37 - $10.90     *****
10  Harry Potter and the Sorcerer's Stone: The Illustr  $9.23 - $39.99     ****
11  Harry Potter Complete Book Series Special Edition   $64.88 - $81.95    *****
12  Harry Potter and the Cursed Child, Parts One and T  $3.15 - $12.99     ****
13  Harry Potter Books Set #1-7 in Collectible Trunk-L  $73.96 - $157.95   ****
14  Harry Potter Complete Collection 7 Books Set Colle  $146.89 - $163.99  *****
15  Harry Potter and the Chamber of Secrets: The Illus  $20.51 - $39.99    *****
16  Harry Potter and the Prisoner of Azkaban: The Illu  $15.92 - $275.00   *****
17  The Unofficial Harry Potter Spellbook: Wizard Trai  $0.00 - $13.95     ****
18  [Sponsored]Widdershins – Part One: The Boy with Ab  $0.00 - $0.76      *****
19  [Sponsored]Missions Accomplished: And some funny b  $0.00 - $3.96      *****
```

![Amazon Comparison Shot](amazon_screenshot.png)

<a name="installation"></a>
### Installation

Can easily be be run on Python version 3 or greater with minimal additional dependencies.

Install the dependencies and main package using pip.

```
$ pip install amzsear
```

For those wanting to upgrade to version 2, use the command:

```
$ pip install amzsear --upgrade
```

Note: The [Pandas](https://pandas.pydata.org/) package is not a required dependency for amzSear, however a few methods do use it (see [AmzSear.md](docs/core/AmzSear.md#to_dataframe), [AmzBase.md](docs/core/AmzBase.md#to_series)) if one wants to integrate with Pandas. If this is the case, pandas should be installed separately using:
```
$ pip install pandas
```

<a name="usage"></a>
### Usage

AmzSear can be used in two ways, from the command line and as a Python package.

#### CLI
The amzSear CLI allows Amazon search queries to be performed directly from the command line. In it's simplest form, the CLI only requires a query.

```
$ amzsear 'Harry Potter Books'
```

However, additional options can be set to select the page number, item number, region or the output format. For example:

```
$ amzsear 'Harry Potter' -p 2 -i 35 --output json
```

The above query will display the item at index 35 on page 2 as a JSON object. For more examples and for extended usage information see the [CLI Readme](docs/cli/README.md).


#### API

```python
from amzsear import AmzSear
amz = AmzSear('Harry Potter')
```

In the latest version of amzSear dedicated `AmzSear` and `AmzProduct` classes have been created to allow easier extraction of Amazon product information in a Python program. For example:
```python
>>> from amzsear import AmzSear
>>> amz = AmzSear('Harry Potter', page=2, region='CA')
>>> 
>>> last_item = amz.rget(-1) # retrieves the last item in the amzSear
>>> print(last_item)
title               "[Sponsored]Kids' Travel Guide - London: The fun way to discover Lo..."
product_url         'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_s...'
image_url           'https://images-na.ssl-images-amazon.com/images/I/61CatLnbhQL._AC_U...'
rating              ratings_text          '4.6 out of 5 stars'
                    ratings_count_text    '29'
                    <Valid AmzRating object>
prices              {'Perfect Paperback': '$8.37', '1': '$10.90'}
extra_attributes    {}
subtext             ['by Sarah-Jane Williams and FlyingKids']
<Valid AmzProduct object>
>>> 
>>> print(last_item.get_prices()) # retrieves all price values as floats
[8.37, 10.9]
```

For a complete explanation of the intricacies of the amzSear core API, see the [API docs](docs/core/).



<a name="whats-new"></a>
### What's New in Version 2.0

| Feature                                                        | v 1.0 | v 2.0 |
|----------------------------------------------------------------|-------|-------|
| Command line Amazon queries                                    | ✓     | ✓     |
| Command line conversion to CSV or JSON                         |       | ✓     |
| Support for US Amazon                                          | ✓     | ✓     |
| Support across __all__ Amazon regions                          |       | ✓     |
| Single page API queries                                        | ✓     | ✓     |
| Multiple page API queries                                      |       | ✓     |
| Dedicated AmzSear class & subclasses                           |       | ✓     |
| Extraction of (title, url, prices & rating)                    | ✓     | ✓     |
| Extraction of (image_url, rating's count, extra text, subtext) |       | ✓     |
| Consistent extraction across Amazon sites                      |       | ✓     |
| Support for API input from query or url or html directly       |       | ✓     |


##### Summary
* Support across all Amazon regions (Australia, India, Spain, UK, US, etc.)
* Dedicated AmzSear class & subclasses
* Better scraping & extraction to retrieve all data
* Additional fields - including image_url, subtitle/subtext, rating's count
* Simpler usability and clearer command line interface
* Multiple command line export formats - CSV, JSON, etc.

A more in depth understanding of the latest features of the CLI can be explored in the [CLI Readme](docs/cli/README.md). A complete breakdown of the core API's extended features can be seen in the core [API docs](docs/core/).

### About

##### Articles

* [OSTechNix](https://www.ostechnix.com/search-amazon-products-command-line/)
* [CrackWare](http://crackware.me/technology/search-amazon-products-from-command-line/)
* [Linux-OS.net](http://linux-os.net/amzsear-busca-productos-en-amazon-desde-la-linea-de-comandos/)
* [MasLinux](http://maslinux.es/buscar-productos-de-amazon-desde-la-linea-de-comandos/)

This library was designed to facilitate the use of amazon search on the command line whilst also providing a utility to easily scrape basic product information from Amazon (for those without access to Amazon's Product API). The developer does, however, append an Amazon Affiliate Tag in order to track usage of this software and to monetize this and other publicly accessible projects. We are a participant in the Amazon Services LLC Associates Program, an affiliate advertising program designed to provide a means for us to earn fees by linking to Amazon.com and affiliated sites.

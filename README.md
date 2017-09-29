# amzSear

The unofficial Amazon Product CLI & API. Easily search the amazon product directory from the command line without the need for an Amazon API key.

Wondering about about an amazon product listing? Find the amzSear!


```
$ amzsear 'Harry Potter Books'
```


```
     Name                                                     Price    Rating
0    Harry Potter Paperback Box Set (Books 1-7)               $21.20    *****
1    Harry Potter and the Sorcerer's Stone                    $7.89     *****
2    Harry Potter and the Sorcerer's Stone: The Illustrated   $9.54     *****
3    Harry Potter and the Prisoner of Azkaban                 $7.79     *****
4    Harry Potter And The Goblet Of Fire                      $8.75     *****
5    Harry Potter And The Order Of The Phoenix                $8.75     *****
6    Harry Potter And The Chamber Of Secrets                  $8.34     *****
7    Harry Potter and the Half-Blood Prince (Book 6)          $8.75      ****
8    Harry Potter and the Deathly Hallows (Book 7)            $8.75     *****
9    Harry Potter and the Cursed Child, Parts 1 & 2, Special  $8.75      ****
10   Harry Potter and the Prisoner of Azkaban: The Illustrat  $23.99         
11   Harry Potter Complete Book Series Special Edition Boxed  $70.28    *****
12   Harry Potter: A Journey Through a History of Magic       $15.99         
13   Harry Potter Books Set #1-7 in Collectible Trunk-Like T  $133.62   *****
14   Fantastic Beasts and Where to Find Them                  $5.74      ****
15   Harry Potter and the Chamber of Secrets: The Illustrate  $26.12    *****
16   When Hamburgers Fly                                      $3.18          
17   The Silver Portal (Weapons of Power Book 1)              $4.02     *****
18   Bentwhistle the Dragon in A Threat from the Past         $3.90      ****
19   Overworld Chronicles Box Set Books 1-4: Urban Fantasy T  $3.18      ****
```

![Amazon Comparison Shot](amazon_screenshot.png)

### Installation

Can easily be be run on Python version 2.7 or greater with minimal additional dependencies (works best on Python3).

Install the dependencies and main package using pip.

```
$ pip install amzsear
```

### Usage

#### CLI
Typing `amzsear` without any additionally arguments will display the following usage information:

```
Usage: amzsear query_string [-p num [-i num]] [-q] [-v] [-d]
```
###### Optional Parameters
- `-p num` - Specify the page number to search (defaults to `-p 1`)
- `-i num` - Select the number item to display (relative to the page number)
- `-q` - Disable any printout from occurring on the command line
- `-v` - Display all information scraped (name, url, all prices, rating string)
- `d` - Disable the page from opening in your default web browser


#### API
The API can be used to download Amazon data within a Python script. The main methods `getSearchPage` and `getItem` are the best entry points to use for such cases. These methods will return a tuple of the products (or product) as well as a url to access either the search page (for a search query) or the item page (for a single item query).

```
>>> from amzsear import api
>>> api.getSearchPage('Harry Potter Books')
>>> (products,url) = api.getSearchPage('Harry Potter Books',page_num=1)
```

The products returned from `getSearchPage` and `getItem` have unrefined data which, whilst usable, usually requires some cleansing. Consequently, the methods  `getCleanPrices` and `getRatingValue` can be used to receive numeric information from the data collected.

### About
This library was designed to facilitate the use of amazon search on the command line whilst also providing a utility to easily scrape basic product information from Amazon (for those without access to Amazon's Product API). The developer does, however, append an Amazon Affiliate Tag in order to track usage of this software and to monetize this and other publicly accessible projects.

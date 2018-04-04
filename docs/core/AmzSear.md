## Class Definition
<a name="AmzSear"></a>
#### AmzSear(*query=None, page=1, region='US', url=None, html=None, html_element=None, products=None*):

The AmzSear object is similar to a Python dict, with each item having a unique index (Amazon search number) to reference each [AmzProduct](AmzProduct.md). The items can be indexed and iterated over using standard indexing and iteration or utilising the methods below.

##### Constructor

The object can be created at different stages, however in it's simplest form the object is instantiated using the `query` argument.

```python
from amzsear import AmzSear
amz = AmzSear('Harry Potter')
```

Whilst it may appear that multiple different arguments can be passed to the constructor this is not the case in terms of outcome. The arguments follow the following hierarchy:

```
(query, [page], [region])
           |
         (url)
           |
         (html)
           |
     (html_element)
           |
       (products)
```

That is to say that if arguments are passed at more than one level, the arguments at the highest level will be used to override the arguments passed on other levels. For example, if a url was passed as well as a query, the url would be ignored and generated from the query.

###### Optional Args:
*query* (str): A search query to look up on Amazon.  
*page* (int\*): The page number of the query (defaults to 1).  
*region* (str): The Amazon region/country to search. For a list of countries to country code see the [regions table](../regions.md) (defaults to US).  
*url* (str\*): An Amazon search url (not recommended).  
*html* (str\*): The HTML code from an Amazon search page (not recommended).  
*html_element* (LXML root\*): The LXML root generated from the HTML off of an Amazon search page (not recommended).  
*products* (list\*): A list of AmzProducts.  

Note: All arg types marked with a "\*" can be an iterable of that type. In other words, a page can either be an int or a list or range, etc. of ints to be searched. The same is true for url, html, html_elements and products.


## Class Methods

<a name="aget"></a>
#### aget(*key, default=None, raise_error=False*):

"All get" - gets a list of attributes values from one or more attribute keys.

```python
amz = AmzSear('Harry Potter')
titles_and_urls = amz.aget(['title','product_url'])
```
In the above example, `titles_and_urls` will have a list of tuples each with a url and a title for each product in the AmzSear object (if the key is available).

###### Args:
*key* (str or list): A single attribute name or a list of attributes.  

###### Optional Args:
*default*: The default value, should raise_error=False and the attribute name be unavailable for a product.  
*raise_error* (bool): If True, an error will be raised if the value of key or any of the values of key are not found.  

###### Returns:
list: List of tuples in product order of the AmzSear.


## 

<a name="get"></a>
#### get(*key, default=None, raise_error=False*):

Gets the AmzProduct by index, default is returned if the index is not found or an error is raised if raise_error=True.

Indexing the AmzSear object is equivalent to calling this method with raise_error=True. For example:

```python
amz = AmzSear('Harry Potter')
indexed = amz[0]
from_get = amz.get(0, default=None, raise_error=True)

#indexed == from_get

```

###### Args:
*key* (str): The index number of the product in the AmzSear object.  

###### Optional Args:
*default*: The default value, should raise_error=False.  
*raise_error* (bool): If True, an error will be raised if the key cannot be found.  

###### Returns:
The AmzProduct at the key, otherwise the default value.


## 

<a name="indexes"></a>
#### indexes():

A list of all all indexes in the current object.


###### Returns:
list: A list of all the indexes in the object.


## 

<a name="items"></a>
#### items():

An iterator yielding a tuple of an index and a AmzProduct for each iteration.

###### Returns:
zip: A generator to be iterated over.


## 

<a name="keys"></a>
#### keys():

Alternate name for [indexes](#indexes).

## 

<a name="products"></a>
#### products():

Alternate name for [values](#values).

## 

<a name="rget"></a>
#### rget(*key, default=None, raise_error=False*):

"Relative get" - Gets the nth key of the the object.

For example, if the [indexes](#indexes) method returns the list `['0', '2', '4', '7']`, calling rget with key=1 will return the AmzProduct at index `'2'`, whereas calling rget with key=-1 will return the AmzProduct at index `'7'`.

###### Args:
*key* (int): The relative index of the desired product.  

###### Optional Args:
*default*: The default value, should raise_error=False.  
*raise_error* (bool): If True, an error will be raised if the index is out of range.

###### Returns:
The AmzProduct at the relative index, otherwise the default value.


## 

<a name="to_dataframe"></a>
#### to\_dataframe(*recursive=True, flatten=False*):

Pandas must be installed for this method to be called. It will convert the object to a [Pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) using the same possible recursive and flattening options of the [AmzBase to\_dict](AmzBase.md#to_dict) method.

###### Optional Args:
*recursive* (bool): See [AmzBase to\_dict](AmzBase.md#to_dict) method.  
*flatten* (bool): See [AmzBase to\_dict](AmzBase.md#to_dict) method.  

###### Returns:
[Pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html): A dataframe with each product in a series with it's index.


## 

<a name="values"></a>
#### values():

A list of all products in the current object.

###### Returns:
list: A list of AmzProduct objects.



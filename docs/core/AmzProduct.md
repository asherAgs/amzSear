## Class Definition
<a name="AmzProduct"></a>
#### AmzProduct(*html_element=None*):

The AmzProduct class extends the [AmzBase](AmzBase.md#AmzBase) class and, as such the following attributes are available to be called as an index call or as an attribute:

* *title* (str): The name of the product.
* *product_url* (str) A url directly to the product's Amazon page.
* *image_url* (str) A url to the product's default image.
* *rating* ([AmzRating](AmzRating.md)) An AmzRating object.
* *prices* (dict) A dictionary of prices, with the price type as a key and a string for the price value (see [get_prices](#get_prices) to get float values).
* *extra_attributes* (dict) Any extra information that can be extracted from the product.
* *subtext* (list) A list of strings under the title, typically the author's name and/or the date of publication.

This class should usually not be instantiated directly (rather be used in an [AmzSear](AmzSear.md) object) but can be created by passing an HTML element to the constructor. If nothing is passed, an empty AmzProduct object is created.

###### Optional Args:
*html_element* (LXML root): A root for an HTML tree derived from an element on an Amazon search page.


## Class Methods

<a name="get"></a>
#### get(*key, default=None, raise_error=False*):

Inherited method from [AmzBase](AmzBase.md#get).

## 

<a name="get_prices"></a>
#### get\_prices(*key=None*):

Gets a list of floats from the dictionary of price text. A key can be passed to explicitly specify the prices to select. If the key is None, all prices keys are used.

###### Optional Args:
*key* (str or list): A key or list of keys to in the price dictionary.  

###### Returns:
list: List of floats for the subset of price specified.


## 

<a name="is_valid"></a>
#### is\_valid():

Inherited method from [AmzBase](AmzBase.md#is_valid).

## 

<a name="items"></a>
#### items():

Inherited method from [AmzBase](AmzBase.md#items).

## 

<a name="keys"></a>
#### keys():

Inherited method from [AmzBase](AmzBase.md#keys).

## 

<a name="to_dict"></a>
#### to\_dict(*recursive=True, flatten=False*):

Inherited method from [AmzBase](AmzBase.md#).

## 

<a name="to_series"></a>
#### to\_series(*recursive=True, flatten=False*):

Inherited method from [AmzBase](AmzBase.md#to_series).


## 

<a name="values"></a>
#### values():

Inherited method from [AmzBase](AmzBase.md#values).


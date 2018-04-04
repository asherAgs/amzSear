## Class Definition
<a name="AmzRating"></a>
#### AmzRating(*html_element=None*):

The AmzRating class extends the [AmzBase](AmzBase.md#AmzBase) class and, as such the following attributes are available to be called as an index call or as an attribute:

* *ratings_text* (str): The star rating (e.g. "4.5/5").
* *ratings_count_text* (str): The number of votes (e.g. "100").

This class should usually not be instantiated directly (rather be used as part of an [AmzProduct](AmzProduct.md) element) but can be created by passing an HTML element to the constructor. If nothing is passed, an empty AmzRating object is created.

###### Optional Args:
*html_element* (LXML root): A root for an HTML tree derived from an element on an Amazon search page.


## Class Methods

<a name="get"></a>
#### get(*key, default=None, raise_error=False*):

Inherited method from [AmzBase](AmzBase.md#get).

## 

<a name="get_count"></a>
#### get\_count():

Gets the total number of ratings.

###### Returns:
int: The number of ratings.

## 

<a name="get_denominator"></a>
#### get\_denominator():
Gets the value the star rating is out of (usually 5).

###### Returns:
float: The denominator of the star rating.

## 

<a name="get_numerator"></a>
#### get\_numerator():

Gets the value the average value of the star rating (usually between 0 and 5).

###### Returns:
float: The numerator of the star rating.

## 

<a name="get_perc"></a>
#### get\_perc():

Gets a percentage value of the rating - 0% being a 0/5 star rating and 100% being a 5/5 star rating.

###### Returns:
float: The star percentage.

## 

<a name="get_star_repr"></a>
#### get\_star\_repr(star_repr='*'):

Gives a visual representation of the star rating, rounding to the nearest star.

###### Optional Args:
*star_repr* (str): A (typically) single character used to represent a star.   

###### Returns:
str: A representation of the star rating.

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

Inherited method from [AmzBase](AmzBase.md#to_dict).

## 

<a name="to_series"></a>
#### to\_series(*recursive=True, flatten=False*):

Inherited method from [AmzBase](AmzBase.md#to_series).

## 

<a name="values"></a>
#### values():

Inherited method from [AmzBase](AmzBase.md#values).



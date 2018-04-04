## Class Definition
<a name="AmzBase"></a>
#### AmzBase(*key1=value1, key2=value2, ...*):

The AmzBase class can be works similarly to the 'dict' class in Python. However, keys for the class are predefined when in the subclass that inherits AmzBase and there is also the potential for validity/invalidity to be defined in the object. The keys can also be indexed (as they would be for a dict) but can also be accessed as attributes. For example:

```python
obj = AmzBase(a=1, b=2, c=3)
indexed = obj['b']
attribute = obj.b

# indexed == attribute == 2

```

###### Optional Args:
Any key value pairs passed to the constructor will be set as attributes that can be accessed using an index call or as directly, as an attribute.

## Class Methods

<a name="get"></a>
#### get(*key, default=None, raise_error=False*):

Gets an element by key if available. If the key does not exist an error will be raised if raise_error is True otherwise the default value will be returned.

###### Args:
*key* (str): The key to be accessed in the AmzBase object.  

###### Optional Args:
*default*: A default value to return if the key specified does not exist.  
*raise_error* (bool): True if an error is to be raised, should the key not exist.  

###### Returns:
The value of the key or the default value if an error is not raised.


## 

<a name="is_valid"></a>
#### is\_valid():

Gets the validity of the object, as outlined in each object's constructor.

###### Returns:
bool: True if the object is valid, otherwise False.


## 

<a name="items"></a>
#### items():

Similar to dict.items, this method yields a generator with each iteration returning a tuple of an attribute name and the attribute for each element in the object.

###### Returns:
zip: A generator to be iterated over.

## 

<a name="keys"></a>
#### keys():

Similar to dict.keys, this method gives a list of the names of all the attributes in the object.

###### Returns:
list: The names of all the attributes in the object.

## 

<a name="to_dict"></a>
#### to\_dict(*recursive=True, flatten=False*):

Converts the object to a dict with optionally being able to recurse of to_dict methods for composite AmzBase objects and to place these composite elements at the same level when flatten=True.

Calling dict(cls) will have the same effect as calling cls.to_dict(recursive=False, flatten=False).

###### Optional Args:
*recursive* (bool): If true any values with a to_dict method will have their method called too, otherwise the value will be the object.  
*flatten* (bool): If true recursive calls to to_dict will cause the values to be merged at the top level. Note that recursive must be True for this to have an effect.  

###### Returns:
dict: A dict of the with attribute names as keys and their values as values.


## 

<a name="to_series"></a>
#### to\_series(*recursive=True, flatten=False*):

Pandas must be installed for this method to be called. It will convert the object to a [Pandas Series](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html) using the same possible recursive and flattening options of the [to\_dict](#to_dict) method.

###### Optional Args:
*recursive* (bool): See [to\_dict](#to_dict).  
*flatten* (bool): See [to\_dict](#to_dict).  

###### Returns:
[Pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html): A series with attribute names as keys and their values as values.


## 

<a name="values"></a>
#### values():

Similar to dict.values, this method gives a list of the values of all the attributes in the object.

###### Returns:
list: The values of all the attributes in the object.


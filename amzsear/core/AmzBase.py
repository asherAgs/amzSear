try:
    from amzsear.core.consts import REPR_MAX_LEN_DEFAULT
    from amzsear.core import requires_valid_data
except ImportError:
    from .amzsear.core.consts import REPR_MAX_LEN_DEFAULT
    from .amzsear.core import requires_valid_data

"""
    The AmzBase class can be works similarly to the 'dict' class in Python.
    However, keys for the class are predefined when in the subclass that
    inherits AmzBase and there is also the potential for validity/invalidity
    to be defined in the object. The keys can also be indexed (as they would
    be for a dict) but can also be accessed as attributes.

    Optional Args:
        Any key value pairs passed to the constructor will be set as
        attributes that can be accessed using an index call or as directly,
        as an attribute.
"""
class AmzBase(object):
    _is_valid = False
    _all_attrs = []

    REPR_MAX_LEN = REPR_MAX_LEN_DEFAULT

    """
    """
    def __init__(self,**kws):
        for k, v in kws.items():
            setattr(self,k,v)
            self._all_attrs.append(k)

    def __getitem__(self, key):
        return self.get(key, raise_error=True)

    def __len__(self):
        return len([x for x in self])

    def __bool__(self):
        return self.is_valid()

    def __contains__(self,it):
        return it in list(self)

    def __iter__(self):
        for attr_name in self._all_attrs:
            if getattr(self, attr_name, None) != None:
                yield attr_name

    def __repr__(self):
        def get_repr():
            out = []

            if len(self) > 0:
                max_k = len(max(self._all_attrs, key=lambda x: len(x)))
                str_format = '{:%d}    {}' % (max_k)
                for key, value in self.items():
                    #indent newlines (these will usually be for an instance of a class inheriting AmzBase)
                    value = repr(value).replace('\n','\n' + ' '*(max_k + 4)) #length of space
                    out.append(str_format.format(key, value)) 

            #add validity & class to the end
            out.append('<' + ('V' if self else 'Inv') + 'alid ' + self.__class__.__name__ + ' object>') 
            return '\n'.join(out)

        lines = get_repr().split('\n') 
        out_lines = [l if len(l) <= self.REPR_MAX_LEN else l[:(self.REPR_MAX_LEN-3)] + '...' for l in lines]
        return '\n'.join(out_lines)

    """
        Gets an element by key if available. If the key does not exist an error will be raised
        if raise_error is True otherwise the default value will be returned.

        Args:
            key (str): The key to be accessed in the AmzBase object.

        Optional Args:
            default: A default value to return if the key specified does not exist.
            raise_error (bool): True if an error is to be raised, should the key not exist.

        Returns:
            The value of the key or the default value if an error is not raised.
    """
    def get(self, key, default=None, raise_error=False):
        if key not in self:
            if raise_error == True:
                raise KeyError('The key %s is not a know attribute' % (repr(key)) )
            else:
                return default

        return getattr(self,key)

    """
        Similar to dict.items, this method yields a generator with each iteration
        returning a tuple of an attribute name and the attribute for each element in the object.

        Returns:
            zip: A generator to be iterated over.
    """
    @requires_valid_data(default=iter(()))
    def items(self):
        for attr_name in self._all_attrs:
            if getattr(self, attr_name, None) != None:
                yield (attr_name, getattr(self,attr_name))

    """
    Similar to dict.keys, this method gives a list of the names of all the
    attributes in the object.

    Returns:
        list: The names of all the attributes in the object.
    """
    @requires_valid_data(default=[])
    def keys(self):
        return list(x for x in self)

    """
        Similar to dict.values, this method gives a list of the values of
        all the attributes in the object.

        Returns:
            list: The values of all the attributes in the object.
    """
    @requires_valid_data(default=[])
    def values(self):
        return list(y for x,y in self.items())


    """
        Gets the validity of the object, as outlined in each object's constructor.

        Returns:
            bool: True if the object is valid, otherwise False.
    """
    def is_valid(self):
        return self._is_valid

    """
        Converts the object to a dict with optionally being able to recurse of to_dict
        methods for composite AmzBase objects and to place these composite elements at
        the same level when flatten=True.

        Calling dict(cls) will have the same effect as calling
        cls.to_dict(recursive=False, flatten=False).

        Optional Args:
            recursive (bool): If true any values with a to_dict method will have their
              method called too, otherwise the value will be the object.
            flatten (bool): If true recursive calls to to_dict will cause the values to
              be merged at the top level. Note that recursive must be True for this to have an effect.

         Returns:
             dict: A dict of the with attribute names as keys and their values as values.
    """
    def to_dict(self, recursive=True, flatten=False):
        d = {}
        for k, v in self.items():
            if recursive == True and hasattr(v,'to_dict'):
                if flatten == True:
                    d = {**d, **v.to_dict()}
                else:
                    d[k] = v.to_dict()
            else:
                d[k] = v
        return d

    """
        Pandas must be installed for this method to be called. It will convert
        the object to a Pandas Series using the same possible recursive and
        flattening options of the to_dict method above.

        Optional Args:
            recursive (bool): See above.
            flatten (bool): See above.

        Returns:
            Pandas DataFrame: A series with attribute names as keys and their values as values.
    """
    def to_series(self, recursive=True, flatten=False):
        #only import at this point as amzSear can be used without pandas if desired
        from pandas import Series 
        return Series(self.to_dict(recursive=recursive,flatten=flatten))

# -*- coding: utf-8 -*-
"""
Handling custom data types.
"""

from __future__ import absolute_import
from .exceptions import ValidateNotImplemented, InvalidDidoType


class MetaTypes(type):
    """
    Class handling data types. We have to specific the 
    data that knows. In case of inappropriate value raise
    ValueError.
    """

    def __init__(cls, name, bases, dct):
        cls.dct = dct
        super(MetaTypes, cls).__init__(name, bases, dct)
    
    def __call__(cls, *args, **kwargs):
    
        if 'validate' not in cls.dct:
            raise ValidateNotImplemented()

        return super(MetaTypes, cls).__call__(*args, **kwargs)
    

class Types(object):
    __metaclass__ = MetaTypes

    def __init__(self, value=None):
        self._val = None

        if value:
            self.val = value

    def __str__(self):
        return '{}'.format(self.val)
    
    def __repr__(self):
        return '{}'.format(self.val)        
    
    @property
    def val(self):
        return self._val
    
    @val.setter
    def val(self, value):

        if isinstance(value, int):
            valeu = str(value)

        self._val = value
        self.validate(self._val)
    
    def validate(self, value):
        """To implement this method to handling data. If valid raises
        InvalidDidoType."""
        pass

    def __call__(self, value=None):
        if value:
            self.val = value

        return self.val


class ZipCodeBR(Types):
    """
    Class handling zipcode from Brazil.
    """
    
    def validate(self, data, sep='-', **kwargs):
        """
        Validates if content is ZipCode with or less separator. The Brazil 
        ZipCode contains five numbers at left side and three numbers in right
        side.

        :param sep: separator when string of the data is passed

        """
        print ('Eu sou validate de ZIP da classe pai...')
        def int_convertible(*args):
            try:
                for pos in args:
                    p = int(pos)
                    return p 
            except:
                raise InvalidDidoType(self.__class__)

        data = str(data) if isinstance(data, int) else data

        if sep in data:
            code_places = data.split(sep)
            if len(code_places) == 2:
                int_convertible(code_places[0], code_places[1])
                
            else:
                raise InvalidDidoType(self.__class__)
        
        elif len(data) == 8:
            int_convertible(data[:5], data[5:8])

        else:
            raise InvalidDidoType(self.__class__)
            



#email
#ip_address
#mac_address
#url
#zipcode
#currency
#int
#...


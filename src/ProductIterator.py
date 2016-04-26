#!/usr/bin/python3
"""
.. moduleauthor:: Albert Heinle<albert.heinle@gmail.com>
"""

import json
from Product import Product

class ProductIterator:
    """
    An iterator that goes through a given file containing JSON entries,
    and returning an instance of Product each time. The format of the
    JSON entries should be given as in the product example file from
    http://sortable.com/challenge.
    """

    def __init__(self,filename):
        """
        Constructor for ProductIterator. It gets passed a filename and
        tries to open it. If successful, it will return a Product
        instance at each step.
        
        :param filename:  The name of the file with the JSON strings.
        :type  filename:  String
        :raises:          TypeError, ValueError
        """
        if (type(filename)!=str):
            raise TypeError("Type of filename was not string")
        try:
            self.__file = open(filename,'r')
        except:
            raise ValueError("The file with the given name did not\
 exist (%s)"%filename)
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.__file==None:
            raise StopIteration()
        line = self.__file.readline()
        if line.strip() == "":
            self.__file.close()
            self.__file = None
            raise StopIteration()
        product_dict = json.loads(line) #TODO: maybe make handle
                                        #premature exit
        name = product_dict["product_name"]
        manufacturer = product_dict["manufacturer"]
        model = product_dict["model"]
        if "family" in product_dict:
            family = product_dict["family"]
        else:
            family = ""
        a_d = product_dict["announced-date"]
        return Product(name,manufacturer,family,model,a_d)


    def __del__(self):
        if self.__file!=None:
            self.__file.close()

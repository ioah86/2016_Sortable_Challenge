#!/usr/bin/python3
"""
.. moduleauthor:: Albert Heinle<albert.heinle@gmail.com>
"""

import json
from Listing import Listing

class ListingIterator:
    """
    An iterator that goes through a given file containing JSON entries,
    and returning an instance of Listing each time. The format of the
    JSON entries should be given as in the product example file from
    http://sortable.com/challenge.
    """

    def __init__(self,filename):
        """
        Constructor for ListingIterator. It gets passed a filename and
        tries to open it. If successful, it will return a Listing
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
        listing_dict = json.loads(line) #TODO: maybe make handle
                                        #premature exit
        title = listing_dict["title"]
        manufacturer = listing_dict["manufacturer"]
        currency = listing_dict["currency"]
        price = listing_dict["price"]
        return Listing(title,manufacturer,currency,price)


    def __del__(self):
        if self.__file!=None:
            self.__file.close()

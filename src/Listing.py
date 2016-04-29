#!/usr/bin/python3
"""
.. moduleauthor:: Albert Heinle<albert.heinle@gmail.com>
"""

import json


class Listing:
    """
    This class represents listings as provided in the sortable
    challenge. For additional details refer to
    http://sortable.com/challenge.
    """
    
    def __init__(self,title,manufacturer,currency,price,jsonString=None):
        """
        The constructor for Listing.

        :param title:        Description of product for sale
        :type  title:        String
        :param manufacturer: Who manufactures the product for sale
                             (can be empty)
        :type  manufacturer: String
        :param currency:     currency code, e.g. USD, CAD, GBP, etc.
        :type  currency:     String
        :param price:        price, e.g. 19.99, 100.00
        :type  price:        String
        :param jsonString:   The JSON representation of the product as
                             given in the file
        :type jsonString:    String or None
        :raises:             TypeError, ValueError
        """
        if (type(title)!=str or
            type(manufacturer) != str or
            type(currency)!= str or
            type(price)!= str or
            (jsonString and type(jsonString)!=str)):
            raise TypeError("Incorrect types given as input")
        if title.strip()=="":
            raise ValueError("title was an empty string")
        self.__title = title
        #if manufacturer.strip()=="":
        #    raise ValueError("manufacturer was an empty string")
        self.__manufacturer = manufacturer.strip()
        if currency.strip()=="":
            raise ValueError("currency was an empty string")
        self.__currency = currency.strip()
        if price.strip()=="":
            raise ValueError("price was an empty string")
        self.__price = price.strip()
        self.__jsonString = jsonString
        

    def getTitle(self):
        return self.__title

    def getManufacturer(self):
        return self.__manufacturer

    def getCurrency(self):
        return self.__currency

    def getPrice(self):
        return self.__price

    def __eq__(self,other):
        return(self.__title == other.getTitle() and
               self.__manufacturer == other.getManufacturer() and
               self.__currency == other.getCurrency() and
               self.__price == other.getPrice())

    def __ne__(self,other):
        return not self.__eq__(other)

    def __str__(self):
        return """Title: %s
Manufacturer: %s
Currency: %s
Price: %s"""%(self.__title,
              self.__manufacturer,
              self.__currency,
              self.__price)

    def toJSON(self):
        if self.__jsonString:
            return self.__jsonString
        jsonDict = {
            "title":self.__title,
            "manufacturer":self.__manufacturer,
            "currency":self.__currency,
            "price":self.__price
        }
        return json.dumps(jsonDict)

#!/usr/bin/python3
"""
.. moduleauthor:: Albert Heinle<albert.heinle@gmail.com>
"""

import json

class Product:
    """
    This class represents known products as provided in the sortable
    challenge. For additional details refer to
    http://sortable.com/challenge.
    """
    
    def __init__(self, name, manufacturer, family, model, a_d):
        """
        The constructor for product.
        
        :param name:         unique id for the product, nonempty
        :type  name:         String
        :param manufacturer: The manufacturer of the product, nonempty
        :type  manufacturer: String
        :param family:       optional grouping of products
        :type  family:       String
        :param model:        The specific model of the product, nonempty
        :type  model:        String
        :param a_d:          Announcement date, nonempty
        :type  a_d:          String
        :raises:             TypeError, ValueError
        """
        if (type(name) != str or
            type(manufacturer) != str or
            type(family) != str or
            type(model) !=  str or
            type(a_d) != str):
            raise TypeError("Incorrect types given as input")
        if (name.strip() == ""):
            raise ValueError("Name was empty string")
        self.__name         = name.strip()
        if (manufacturer.strip() == ""):
            raise ValueError("Manufacturer was empty string")
        self.__manufacturer = manufacturer.strip()
        self.__family       = family.strip()
        if (model.strip() == ""):
            raise ValueError("Model was empty string")
        self.__model        = model.strip()
        if (a_d.strip() == ""):
            raise ValueError("Announcement date was empty string")
        self.__a_d          = a_d.strip()

    def getName(self):
        """
        :returns: The name of the product.
        :rtype:   String
        """
        return self.__name
    
    def getManufacturer(self):
        """
        :returns: The manufacturer of the product.
        :rtype:   String
        """
        return self.__manufacturer

    def getFamily(self):
        """
        :returns: The family of the product.
        :rtype:   String
        """
        return self.__family

    def getModel(self):
        """
        :returns: The model of the product.
        :rtype:   String
        """
        return self.__model

    def getAnnouncementDate(self):
        """
        :returns: The announced date of the product.
        :rtype:   String
        """
        return self.__a_d

    def __eq__(self,other):
        return (self.__name == other.getName() and
                self.__manufacturer == other.getManufacturer() and
                self.__family == other.getFamily() and
                self.__model == other.getModel() and
                self.__a_d == other.getAnnouncementDate())

    def __ne__(self,other):
        return not self.__eq__(other)

    def __str__(self):
        return """Name: %s
Manufacturer: %s
Family: %s
Model: %s
Announced Date: %s"""%(self.__name,
                       self.__manufacturer,
                       self.__family,
                       self.__model,
                       self.__a_d)

    def toJSON(self):
        """
        :returns: The JSON representation of the product.
        :rtype:   String
        """
        jsonDict = {
            "product_name":self.__name,
            "manufacturer":self.__manufacturer,
            "model":self.__model,
            "family":self.__family,
            "announced-date":self.__a_d
        }
        if jsonDict["family"]=="":
            jsonDict.pop("family",None)
        return json.dumps(jsonDict)

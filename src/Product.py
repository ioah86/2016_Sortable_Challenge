#!/usr/bin/python3
"""
.. moduleauthor:: Albert Heinle<albert.heinle@gmail.com>
"""


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
        return self.__name
    
    def getManufacturer(self):
        return self.__manufacturer

    def getFamily(self):
        return self.__family

    def getModel(self):
        return self.__model

    def getAnnouncementDate(self):
        return self.__a_d

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

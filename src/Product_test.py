#!/usr/bin/python3
"""
.. moduleauthor:: Albert Heinle<albert.heinle@gmail.com>
"""

import unittest
from Product import Product

class TestProduct(unittest.TestCase):
    """
    Testing the class Product for correct functionality
    """

    def test_Product_From_Sortable_Challenge(self):
        """
        Tests the first entry from the sortable challenge, namely:
        "product_name":"Sony_Cyber-shot_DSC-W310",
        "manufacturer":"Sony",
        "model":"DSC-W310",
        "family":"Cyber-shot",
        "announced-date":"2010-01-06T19:00:00.000-05:00"
        We test if the Product is correctly initiated, if all the
        getters work properly and the string representation is right.
        """
        name = "Sony_Cyber-shot_DSC-W310"
        manufacturer = "Sony"
        model = "DSC-W310"
        family = "Cyber-shot"
        a_d ="2010-01-06T19:00:00.000-05:00"
        stringRep = """Name: Sony_Cyber-shot_DSC-W310
Manufacturer: Sony
Family: Cyber-shot
Model: DSC-W310
Announced Date: 2010-01-06T19:00:00.000-05:00"""
        try:
            testProduct = Product(name,manufacturer,family,model,a_d)
        except:
            self.fail("Correct product initialization was not possible")
        self.assertEqual(name, testProduct.getName(),
                         "The name did not coincide with the given one")
        self.assertEqual(manufacturer,testProduct.getManufacturer(),
                         "The manufacturer was not stored properly")
        self.assertEqual(model,testProduct.getModel(),
                         "The model name was not stored properly")
        self.assertEqual(family,testProduct.getFamily(),
                         "The family name was not stored properly")
        self.assertEqual(a_d,testProduct.getAnnouncementDate(),
                         "The announcement date was not stored properly")
        self.assertEqual(stringRep,str(testProduct),
                         "String representation was not correct")


    def test_Invalid_Types(self):
        """
        Tests if everything works even with invalid types for each
        parameter for the constructor.
        """
        name = "Sony_Cyber-shot_DSC-W310"
        manufacturer = "Sony"
        model = "DSC-W310"
        family = "Cyber-shot"
        a_d = "2010-01-06T19:00:00.000-05:00"
        testPassed = 1
        try:
            testProduct = Product(1,manufacturer,family,model,a_d)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("It was possible to provide a non-string type to\
 name")
        try:
            testProduct = Product(name,1,family,model,a_d)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("It was possible to provide a non-string type to\
 manufacturer") 
        try:
            testProduct = Product(name,manufacturer,1,model,a_d)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("It was possible to provide a non-string type to\
 family")
        try:
            testProduct = Product(name,manufacturer,family,1,a_d)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("It was possible to provide a non-string type to\
 model")
        try:
            testProduct = Product(name,manufacturer,family,model,1)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("It was possible to provide a non-string type to\
 announcement date")


    def test_EmptyStrings(self):
        """
        Tests if everything works even with empty strings for each
        parameter for the constructor. Empty strings are only allowed
        for the field "family", since it is optional
        """
        name = "Sony_Cyber-shot_DSC-W310"
        manufacturer = "Sony"
        model = "DSC-W310"
        family = "Cyber-shot"
        a_d = "2010-01-06T19:00:00.000-05:00"
        testPassed = 1
        try:
            testProduct = Product("",manufacturer,family,model,a_d)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("It was possible to provide an empty string to\
 name")
        try:
            testProduct = Product(name,"",family,model,a_d)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("It was possible to provide an empty string type to\
 manufacturer") 
        try:
            testProduct = Product(name,manufacturer,"",model,a_d)
            testPassed = 1
        except:
             testPassed = 0
        if not testPassed:
            self.fail("It was not possible to provide an empty string type to\
 family")
        try:
            testProduct = Product(name,manufacturer,family,"",a_d)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("It was possible to provide an empty string type to\
 model")
        try:
            testProduct = Product(name,manufacturer,family,model,"")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("It was possible to provide an empty string type to\
 announcement date")

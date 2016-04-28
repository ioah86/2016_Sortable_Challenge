#!/usr/bin/python3
"""
.. moduleauthor:: Albert Heinle<albert.heinle@gmail.com>
"""

import unittest
from Listing import Listing
import json

class TestProduct(unittest.TestCase):
    """
    Testing the class Product for correct functionality
    """
    
    def test_Product_From_Sortable_Challenge(self):
        """
        Tests the first Listing entry from the sortable challenge, namely:
        "title":"Fujifilm FinePix REAL 3D W3 10 MP Digital Camera\
 with Dual 3x Optical Zoom Lenses (Black)",
        "manufacturer":"Fujifilm Canada",
        "currency":"CAD",
        "price":"499.99"
        We test if the Listing is correctly initiated, if all the
        getters work properly, the string representation is right
        and the JSON representation is right.
        """
        title = "Fujifilm FinePix REAL 3D W3 10 MP Digital Camera\
 with Dual 3x Optical Zoom Lenses (Black)"
        manufacturer = "Fujifilm Canada"
        currency = "CAD"
        price = "499.99"
        stringRep = """Title: Fujifilm FinePix REAL 3D W3 10 MP Digital Camera\
 with Dual 3x Optical Zoom Lenses (Black)
Manufacturer: Fujifilm Canada
Currency: CAD
Price: 499.99"""
        jsonRep = """{"title":"Fujifilm FinePix REAL 3D W3 10 MP Digital Camera with Dual 3x Optical Zoom Lenses (Black)","manufacturer":"Fujifilm Canada","currency":"CAD","price":"499.99"}"""
        try:
            testListing = Listing(title,manufacturer,currency,price)
        except:
            self.fail("Could not instanciate valid Listing")
        self.assertEqual(title,testListing.getTitle(),
                         "The title was not stored properly")
        self.assertEqual(manufacturer,testListing.getManufacturer(),
                         "The manufacturer was not stored properly")
        self.assertEqual(currency,testListing.getCurrency(),
                         "The Currency was not stored properly")
        self.assertEqual(price,testListing.getPrice(),
                         "The price was not stored properly")
        self.assertEqual(stringRep, str(testListing),
                         "The string representation was not correct")
        self.assertEqual(json.loads(jsonRep),json.loads(testListing.toJSON()),
                         "The JSON representation was not correct")
        

    def test_Invalid_Types(self):
        """
        Tests if everything Listing works even with invalid types for each
        parameter for the constructor.
        """
        title = "Fujifilm FinePix REAL 3D W3 10 MP Digital Camera\
 with Dual 3x Optical Zoom Lenses (Black)"
        manufacturer = "Fujifilm Canada"
        currency = "CAD"
        price = "499.99"
        testPassed = 1
        try:
            testListing = Listing(1,manufacturer,currency,price)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("It was possible to provide a non-string type to\
 title")
        try:
            testListing = Listing(title,1,currency,price)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("It was possible to provide a non-string type to\
 manufacturer")
        try:
            testListing = Listing(title,manufacturer,1,price)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("It was possible to provide a non-string type to\
 currency")
        try:
            testListing = Listing(title,manufacturer,currency,1)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("It was possible to provide a non-string type to\
 price")

            
    def test_EmptyStrings(self):
        """
        Tests if everything works in Listings even with empty strings for each
        parameter for the constructor. No entry is optional
        """
        title = "Fujifilm FinePix REAL 3D W3 10 MP Digital Camera\
 with Dual 3x Optical Zoom Lenses (Black)"
        manufacturer = "Fujifilm Canada"
        currency = "CAD"
        price = "499.99"
        testPassed = 1
        try:
            testListing = Listing("",manufacturer,currency,price)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("It was possible to provide an empty string to\
 title")
        try:
            testListing = Listing(title,"",currency,price)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("It was possible to provide an empty string to\
 manufacturer")
        try:
            testListing = Listing(title,manufacturer,"",price)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("It was possible to provide an empty string to\
 currency")
        try:
            testListing = Listing(title,manufacturer,currency,"")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("It was possible to provide an empty string to\
 price")

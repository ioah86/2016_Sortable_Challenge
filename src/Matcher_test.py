"""
.. moduleauthor:: Albert Heinle<albert.heinle@gmail.com>
"""

import unittest
from Product import Product
from Listing import Listing
from Matcher import Matcher

class TestMatcher(unittest.TestCase):
    """
    Testing the class Matcher for correct functionality
    """
    
    def test_is_matching_english(self):
        """
        Tests the function is_matching for the English language. The test cases are the
        following:
        1. A clear match
        2. A clear mismatch
        3. A match with "for" and/or "with"
        4. A mismatch with "for" and "with"
        5. Same manufacturer, different models
        """
        #1
        name = "Sony_Cyber-shot_DSC-W310"
        manufacturer = "Sony"
        model = "DSC-W310"
        family = "Cyber-shot"
        a_d ="2010-01-06T19:00:00.000-05:00"
        testProduct = Product(name,manufacturer,family,model,a_d)
        title="Sony DSC-W310 12.1MP Digital Camera with 4x Wide Angle\
 Zoom with Digital Steady Shot Image Stabilization and 2.7 inch\
 LCD (Silver)"
        manufacturer="Sony"
        currency="CAD"
        price="139.99"
        testListing = Listing(title,manufacturer,currency,price)
        res = Matcher.is_match(testProduct,testListing)
        self.assertEqual(1,res,"Clear matching was not fulfilled")
        #2
        title="Canon PowerShot A800 (Black)"
        manufacturer = "Canon Canada"
        currency = "CAD"
        price= "99.99"
        testListing = Listing(title,manufacturer,currency,price)
        res = Matcher.is_match(testProduct,testListing)
        self.assertEqual(-1,res,"Clear mismatching was not fulfilled")
        #3
        name="Canon_PowerShot_SX130_IS"
        manufacturer = "Canon"
        model = "SX130 IS"
        family ="PowerShot"
        a_d="2010-08-18T20:00:00.000-04:00"
        testProduct = Product(name,manufacturer,family,model,a_d)
        title="Canon PowerShot SX130IS 12.1 MP Digital Camera with 12x\
 Wide Angle Optical Image Stabilized Zoom with 3.0-Inch LCD"
        manufacturer="Canon Canada"
        currency = "CAD"
        price ="199.96"
        testListing = Listing(title,manufacturer,currency,price)
        res = Matcher.is_match(testProduct,testListing)
        self.assertEqual(1,res,"Matching with \"for\" or \"with\" was not fulfilled")
        #4
        name= "Panasonic-FH5"
        manufacturer = "Panasonic"
        model= "DMC-FH5"
        family = "Lumix"
        a_d = "2011-01-05T19:00:00.000-05:00"
        testProduct = Product(name,manufacturer,family,model,a_d)
        title="DURAGADGET Premium wrist Camera Carrying Strap with 2\
 Year Warranty for Panasonic Lumix FH27, FH25, FP5, FP7, FH5,\
 FH2, S3, S1"
        manufacturer="DURAGADGET"
        currency="CAD"
        price="16.99"
        testListing = Listing(title,manufacturer,currency,price)
        res = Matcher.is_match(testProduct,testListing)
        self.assertEqual(-1,res,
                         "Mismatching with \"for\" or \"with\" was not fulfilled")
        #5
        title="Panasonic Lumix DMW-BCG10 for Lumix ZS7, ZS5, TZ10, TZ8\
 Series"
        manufacturer="Panasonic"
        currency="CAD"
        price="39.99"
        res = Matcher.is_match(testProduct,testListing)
        self.assertEqual(-1,res,
                         "Mismatching different models not fulfilled")

#!/usr/bin/python3
"""
.. moduleauthor:: Albert Heinle<albert.heinle@gmail.com>
"""

import unittest
import os
from ProductIterator import ProductIterator
from Product import Product

class TestProductIterator(unittest.TestCase):
    """
    Testing the class ProductIterator for correct functionality
    """
    
    def test_Product_Iterator_with_small_test_file(self):
        """
        Opens the file
        ../test_files/part_of_challenge_products.txt
        and reads the products from there. This file contains four
        products.
        """
        ourIter = ProductIterator(
            str(os.path.join("..","test_files",
                             "part_of_challenge_products.txt")))
        ourProducts = []
        product1 = Product("Sony_Cyber-shot_DSC-W310",
                           "Sony","Cyber-shot",
                           "DSC-W310",
                           "2010-01-06T19:00:00.000-05:00")
        product2 = Product("Samsung_TL240",
                           "Samsung",
                           "",
                           "TL240",
                           "2010-01-05T19:00:00.000-05:00")
        product3 = Product("Nikon-s6100",
                           "Nikon",
                           "Coolpix",
                           "S6100",
                           "2011-02-08T19:00:00.000-05:00")
        product4 = Product("Samsung_TL220",
                           "Samsung",
                           "",
                           "TL220",
                           "2009-08-12T20:00:00.000-04:00")
        for i in ourIter:
            ourProducts.append(i)
        if len(ourProducts)!=4:
            self.fail("We did not read the exact number of products")
        if not (product1 in ourProducts):
            self.fail("%s was missing in the product list"%str(product1))
        if not (product2 in ourProducts):
            self.fail("%s was missing in the product list"%str(product2))
        if not (product3 in ourProducts):
            self.fail("%s was missing in the product list"%str(product3))
        if not (product4 in ourProducts):
            self.fail("%s was missing in the product list"%str(product4))

    

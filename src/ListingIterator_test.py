#!/usr/bin/python3
"""
.. moduleauthor:: Albert Heinle<albert.heinle@gmail.com>
"""

import unittest
import os
from ListingIterator import ListingIterator
from Listing import Listing

class TestListingIterator(unittest.TestCase):
    """
    Testing the class ListingIterator for correct functionality
    """
    
    def test_Listing_Iterator_with_small_test_file(self):
        """
        Opens the file
        ../test_files/part_of_challenge_listings.txt
        and reads the products from there. This file contains four
        products.
        """
        ourIter = ListingIterator(
            str(os.path.join("..","test_files",
                             "part_of_challenge_listings.txt")))
        ourListings = []
        listing1 = Listing("LED Flash Macro Ring Light (48 X LED)\
 with 6 Adapter Rings for For Canon/Sony/Nikon/Sigma Lenses",
                            "Neewer Electronics Accessories",
                            "CAD",
                            "35.99")
        listing2 = Listing("Canon PowerShot SX130IS 12.1 MP Digital\
 Camera with 12x Wide Angle Optical Image Stabilized Zoom with\
 3.0-Inch LCD",
                           "Canon Canada",
                           "CAD",
                           "199.96")
        listing3 = Listing("Canon PowerShot SX130IS 12.1 MP Digital\
 Camera with 12x Wide Angle Optical Image Stabilized Zoom with\
 3.0-Inch LCD",
                           "Canon Canada",
                           "CAD",
                           "209.00")
        for i in ourIter:
            ourListings.append(i)
        if len(ourListings)!=3:
            self.fail("We did not read the exact number of listings")
        if not (listing1 in ourListings):
            self.fail("%s was missing in the listing list"%str(listing1))
        if not (listing2 in ourListings):
            self.fail("%s was missing in the listing list"%str(listing2))
        if not (listing3 in ourListings):
            self.fail("%s was missing in the listing list"%str(listing3))
        

    

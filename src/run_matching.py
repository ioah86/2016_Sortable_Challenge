#!/usr/bin/python3
"""
This is the main running file of the whole project.

This file is run with two parameters, namely filenames that contain
- The listings
- The products

Then it creates as many threads as needed (number of parallel threads
specified in constants.py) and splits the listings into chunks of a
specific size (again specified in constants.py)


.. moduleauthor:: Albert Heinle<albert.heinle@gmail.com>
"""

from optparse import OptionParser
from ProductIterator import ProductIterator
from ListingIterator import ListingIterator
from Matcher import Matcher
import os
import constants

def get_products(products_file):
    """
    This function obtains a filename with products and creates a
    products dictionary and returns it. The dictionary has as keys
    a lowercase version of a manufacturer and as values a list of
    Products of this manufacturer
    
    :param products_file: A file containing products
    :type  products_file: String
    """
    p_it = ProductIterator(products_file)
    products = {}
    for p in p_it:
        manu = p.getManufacturer().lower()
        if manu in products:
            products[manu].append(p)
        else:
            products[manu] = [p]
    return products


def run_matching(products,listings):
    """
    This function obtains a filename for products files and a filename
    for listings, and calls the Matcher threads to produce matchings.
    
    Assumptions:
    - the files for products and listings do exist

    :param products: A filename to a file containing products
    :type  products: String
    :param listings: A filename to a file containing listings
    :type  listings: String
    """
    products = get_products(opts.products_file)
    listings_iter = ListingIterator(opts.listings_file)
    threads = []
    chunk_count=0
    threads = [None for i in range(constants.number_of_threads)]
    one_more = True
    while(one_more):
        for i in range(constants.number_of_threads):
            if (threads[i] == None) or (not threads[i].is_alive()):
                chunk = []
                for j in range(constants.chunk_size):
                    try:
                        chunk.append(next(listings_iter))
                        chunk_count +=1
                    except:
                        one_more = False
                        break
                if len(chunk)>0:
                    threads[i] = (Matcher(chunk_count,products,chunk))
                    threads[i].start()
    for i in threads:
        if i != None:
            i.join()
    
    


if __name__ == '__main__':
    parser = OptionParser("""run_matching.py -p <products_file>\
 -l <listings_file>""")
    parser.add_option("-p", "--products",
                      dest="products_file",
                      help="Specifies the file with the products.")
    parser.add_option("-l", "--listings",
                      dest="listings_file",
                      help="Specifies the file with the listings.")
    (opts, args) = parser.parse_args()
    if (not opts.products_file) or (not opts.listings_file):
        parser.error("We need both a product file and a listings file\
 as arguments.")
    if (not os.path.isfile(opts.products_file)):
        parser.error("The products file was not a valid file")
    if (not os.path.isfile(opts.listings_file)):
        parser.error("The products file was not a valid file")
    run_matching(opts.products_file,opts.listings_file)

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
from datetime import datetime

def get_products(products_file):
    """
    This function obtains a filename with products and creates a
    products dictionary and returns it. The dictionary has as keys
    a lowercase version of a manufacturer and as values a list of
    Products of this manufacturer
    
    :param products_file: A file containing products
    :type  products_file: String
    :returns:             A dictionary of Products, where the
                          manufacturer is the key
    :rtype:               {String:Product}
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


def run_matching(products_file,listings_file):
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
    products = get_products(products_file)
    listings_iter = ListingIterator(listings_file)
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
                    threads[i] = (Matcher(chunk_count,products,chunk,
                                          resultPathForThisRun))
                    threads[i].start()
    for i in threads:
        if i != None:
            i.join()
    mergeFiles(products)
    

def mergeFiles(products):
    """
    This function takes the files produced by the Matchers, and
    creates the result file by merging the files together.
    It also deletes all unneeded files.

    :param products: A dictionary of products, hashed by manufacturer
    :type  products: dict(String:[Product])
    """
    res = open(os.path.join(resultPathForThisRun,
                            constants.result_file),
               encoding='utf-8',
               mode="w")
    first_entry = True
    for manu in products:
        prodArray = products[manu]
        for p in prodArray:
            entry_made = False
            for f in os.listdir(resultPathForThisRun):
                if f.startswith(p.getName()) and f.endswith(".txt"):
                    if not entry_made:
                        begin_string = """{"product_name":"%s",\
"listings":["""%p.getName()
                        if not first_entry:
                            res.write("\n")
                        else:
                            first_entry = False
                        entry_made = True
                        res.write(begin_string)
                    else:
                        res.write(",")
                    file_obj = open(os.path.join(resultPathForThisRun,f),'r')
                    lstngs = file_obj.read().strip()
                    file_obj.close()
                    res.write(lstngs)
                    os.remove(os.path.join(resultPathForThisRun,f))
            if entry_made:
                res.write("]}")


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
    resultPathForThisRun = os.path.join(constants.result_path,
                                        str(datetime.now()))
    os.mkdir(resultPathForThisRun)
    run_matching(opts.products_file,opts.listings_file)

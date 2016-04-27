#!/usr/bin/python3
"""
.. moduleauthor:: Albert Heinle<albert.heinle@gmail.com>
"""

import threading
import constants
from nltk.tokenize import word_tokenize

class Matcher(threading.Thread):
    """
    This is one of an army of in parallel running Threads.
    It receives a reference to a complete dictionary of products
    (hashed by the manufacturer), and a subset of the listings.
    It tries to match the listings to the products and writes a file
    representing the successful matches.
    """

    def __init__(self, beginIndex, products_dict, listings_chunk):
        """
        The constructor of Matcher. It gets passed a beginIndex
        (unique for each thread; will not be checked),
        which represents the index (with
        respect to the total number of listings) of the
        first listing it tries to match, a dictionary of products
        (hashed by manufacturer) and a list of listings it tries
        to match. The beginindex is also part of a filename that is
        written, which contains all the found matches.

        :param beginIndex: unique beginning index of the chunk this
                           instance tries to match with respect to all
                           listings
        :type  beginIndex: Int (non-negative)
        :param products_dict: A dictionary containing all products,
                              hashed by the manufacturer
        :type  products_dict: dict(String:[Product])
        :param listings_chunk: A list of Listing instances that this
                               class is trying to match.
        :type  listings_chunk: list(Listing)
        """
        self.__beginIndex = beginIndex
        self.__products_dict = products_dict
        self.__listings_chunk = listings_chunk

    
    def run(self):
        """
        Tries to find matches of different products with listings.
        When done, for each product name s, if the product had
        matches, it writes a file named s_i.txt, where i is the class
        variable representing the begin index (unique to the thread),
        where a record of the match is given.
        """
        pass


    def is_match(product, listing):
        """
        This function is passed a variable product of type Product,
        a variable listing of type Listing. It returns three possible
        values.
        -1 - No way it is a match
         0 - It could or could not be a match
         1 - I am very certain it is a match
        
        The algorithm idea is the following:
        - Tokenize the words in the title.
        - If you find e.g. the words "for" or "with", delete this word and
          anything after it, as it has nothing to do with the product.
          The word "for" would describe what the product is used for,
          and model numbers appearing afterwards would deceive, since
          they can name other products.
          The word "with" describes certain extras, that are usually
          not provided in product descriptions.
          A complete list of values as given in lowercase are provided
          in constants.py.
        - In the remaining tokens, try to find
          - the manufacturer
          - the family (if given)
          - the model
          While doing this, one has to keep in mind that there are
          different ways to write a model name. e.g. a "Canon
          PowerShot SX130 IS" may appear as "Canon powershot
          SX-130-IS". For this implementation, we assume that we
          should remove any letters like '_', '-' and ' ' and then try
          to find  the model number or so. We return 1, if we find the
          manufacturer and the model (and optimally the family)
          in this simplistic model.
          We return 0 if we find the manufacturer, the family (if
          given), but not the model. For all the other cases we just
          return -1.
        
        Assumptions:
        - The product and the listing manufacturer is the same
        - 0 should technically never appear. But if it does, we should
          log that.

        :param product: A product that is a potential match
        :type  product: Product
        :param listing: A listing that potentially matches product
        :type  listing: Listing
        """
        token_title = word_tokenize(listing.getTitle())
        #finding words like "for" and "with"
        token_title_lc = list(map(lambda x: x.lower(),token_title))
        minIndex = len(token_title_lc)
        for i in constants.separator_words:
            if i in token_title_lc:
                ind_of_i = token_title_lc.index(i)
                if ind_of_i < minIndex:
                    minIndex = ind_of_i
        if minIndex != len(token_title_lc):
            token_title    = token_title[:minIndex]
            token_title_lc = token_title_lc[:minIndex]
        #make a consecutive string out of it
        merged_tt = "".join(token_title_lc)
        merged_tt = "".join(list(filter(lambda x: not x in "_- ",merged_tt)))
        #Now we try to find the model
        model = product.getModel().lower()
        model = "".join(list(filter(lambda x: not x in "_- ",model)))
        if model in merged_tt:
            model_found = True
        else:
            model_found = False
        #Now we try to find the manufacturer
        manufacturer = product.getManufacturer().lower()
        if manufacturer in merged_tt:
            manu_found = True
        else:
            manu_found = False
        #if the family is given, we also try to find it:
        family = product.getFamily().lower()
        family = "".join(list(filter(lambda x: not x in "_- ",family)))
        if family!="":
            if family in merged_tt:
                family_found = True
            else:
                family_found = False
        else:
            family_found = False
        if manu_found and model_found:
            return 1
        if manu_found and family_found:
            return 0
        return -1

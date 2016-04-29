#!/usr/bin/python3
"""
.. moduleauthor:: Albert Heinle<albert.heinle@gmail.com>
"""

#import threading
import multiprocessing
import constants
from nltk.tokenize import word_tokenize
import os
import logging

logging.basicConfig(level = logging.DEBUG,
                    handlers = [logging.FileHandler("Matcher.log", mode="w")])


class Matcher(multiprocessing.Process):
    """
    This is one of an army of in parallel running Threads.
    It receives a reference to a complete dictionary of products
    (hashed by the manufacturer), and a subset of the listings.
    It tries to match the listings to the products and writes a file
    representing the successful matches.
    """

    def __init__(self, beginIndex, products_dict,
                 listings_chunk,result_path = constants.result_path):
        """
        The constructor of Matcher. It gets passed a beginIndex
        (unique for each thread; will not be checked),
        which represents the index (with
        respect to the total number of listings) of the
        first listing it tries to match, a dictionary of products
        (hashed by manufacturer) and a list of listings it tries
        to match. The beginindex is also part of a filename that is
        written, which contains all the found matches.
        As an optional parameter, the Matcher gets a path to a folder
        where the final results should be stored.

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
        :param result_path: The path to the resulting files
        :type  result_path: String
        """
        multiprocessing.Process.__init__(self)
        self.__beginIndex = beginIndex
        self.__products_dict = products_dict
        self.__listings_chunk = listings_chunk
        self.__matches_dict = {}
        self.__result_path = result_path

    
    def __findPositionInHashTable(self,listing):
        """
        Given a listing of type Listing, this function finds the
        respective position of possible products (based on the
        manufacturer) in the given products dictionary.
        It returns an empty string if no such position can be
        determined, or the key-value.

        :param listing: The listing we try to find a position for
        :type  listing: Listing
        """
        manu_lower = listing.getManufacturer().lower()
        if manu_lower =="":
            #In this case, we should "try" to find a possible
            #manufacturer based on Heuristics
            count = 0
            tempRes = ""
            title_tt = word_tokenize(listing.getTitle())
            title_tt = list(map(lambda x: x.lower, title_tt))
            for p in self.__products_dict:
                if p in title_tt:
                    count += 1
                    tempRes = p
            if count != 1:
                #don't risk ambiguity
                return ""
            return tempRes
        if manu_lower in self.__products_dict:
            return manu_lower
        else:
            manu_lower_wt = word_tokenize(manu_lower)
            matches = []
            for m in manu_lower_wt:
                if m in self.__products_dict:
                    matches.append(m)
            if (len(matches)!=1):
                #we don't want to take the risk in case of ambiguity
                return ""
            return matches[0]
    

    def __getMatchingsForListing(self, listing):
        """
        Given a listing of type Listing, this function matches the
        listing to possible products in the internal dictionary of
        products. It returns a list of such products (or an empty list
        if there are none).

        :param listing: The listing we try to find a position for
        :type  listing: Listing
        """
        hashEntry = self.__findPositionInHashTable(listing)
        if hashEntry == "":
            return []
        potProducts = self.__products_dict[hashEntry]
        matches = []
        for p in potProducts:
            match_outp = Matcher.is_match(p,listing)
            if match_outp>=1:
                matches.append((match_outp,p))
        return matches
    

    def __filterMatchings(self, matchings):
        """
        This function gets called when there is more than one matching
        in the list of matchings in the run function, and it tries to
        filter out one specific matching out of it. If all the
        matchings had a matching factor of 1, empty list is returned.

        ASSUMPTIONS:
        - There is more than one matching in the list
        
        :param matchings: The list of matchings
        :type  matchings: list((Int, Product))
        """
        twoMatches = list(filter(lambda x: x[0] == 2,matchings))
        if len(twoMatches)<=1:
            #Easy case: we already found it, or there was no clear match
            return twoMatches
        #find the most sound match
        result = []
        for i in range(len(twoMatches)):
            for j in range(i+1,len(twoMatches)):
                if (twoMatches[i][1].getModel() in
                    twoMatches[j][1].getModel()):
                    result.append(twoMatches[j])
                elif (twoMatches[j][1].getModel() in
                      twoMatches[i][1].getModel()):
                    result.append(twoMatches[i])
        if result == []:
            return twoMatches
        else:
            return result
        
    
    def run(self):
        """
        Tries to find matches of different products with listings.
        When done, for each product name s, if the product had
        matches, it writes a file named s_i.txt, where i is the class
        variable representing the begin index (unique to the thread),
        where a record of the match is given.
        """
        for l in self.__listings_chunk:
            matching = self.__getMatchingsForListing(l)
            if len(matching)!=1:
                matching = self.__filterMatchings(matching)
                if (len(matching)!=1):
                    if (len(matching)==0):
                        logging.debug("Could not find match for\
 listing %s"%str(l))
                    else:
                        logging.debug("More than one match for listing\
 %s:"%str(l))
                        for p in matching:
                            logging.debug(str(p[1]))
                    continue #in this case, ambiguity was there 
            newId = matching[0][1].getName()
            if newId in self.__matches_dict:
                self.__matches_dict[newId].append(l)
            else:
                self.__matches_dict[newId] = [l]
        self.__writeMatchesToFiles()
        

    def __writeMatchesToFiles(self):
        """
        Assuming that the matches internal dictionary has already been
        filled, this function writes the files containing the matches
        for each product. In particular, for each product name s, a
        file named s_i.txt, where i is the unique begin index of this
        thread, will be generated containing all the listings that
        match s. This file will only be generated if s had a matching
        though.
        """
        for s in self.__matches_dict:
            l_matchings = self.__matches_dict[s]
            l_matchings = ",".join(map(lambda x: x.toJSON(), l_matchings))
            f = open(os.path.join(self.__result_path,
                                  "%s_%d.txt"%(s,self.__beginIndex)),
                     encoding='utf-8',
                     mode='w')
            f.write(l_matchings)
            f.close()

    
    def isInTokenizedString(s,ts):
        """
        This function takes in a string s and a list of strings ts and
        determines if s can be found in ts (maybe by even merging some
        consecutive tokens).

        Assumptions:
        - the elements in ts are all lowercase and don't have the
          symbols '-',' ' and '_'

        :param s:  The string we want to find
        :type  s:  String
        :param ts: The list of tokens where we want to find s
        :type  ts: [String]
        """
        s = s.lower()
        s = "".join(list(filter(lambda x: not x in "_- ",s)))
        if s in ts:
            return True
        tempString = ""
        for i in range(len(ts)):
            tempString += ts[i]
            if tempString==s:
                return True
            if not (tempString in s):
                tempString = ""


    def is_match(product, listing):
        """
        This function is passed a variable product of type Product,
        a variable listing of type Listing. It returns several possible
        values.
        -1 - No way it is a match
         0 - It could or could not be a match
         1 - Manufacturer and Model are given
         2 - Manufacturer, Model and family are found
        
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
          manufacturer and the model, and, if available, the family
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
        merged_tt = list(map(lambda x:
                             "".join(list(filter(lambda y: not y in "_- ",x))),
                             token_title_lc))
        #Now we try to find the model
        model = product.getModel().lower()
        # model = "".join(list(filter(lambda x: not x in "_- ",model)))
        # if model in merged_tt:
        #     model_found = True
        # else:
        #     model_found = False
        model_found = Matcher.isInTokenizedString(model,merged_tt)
        #Now we try to find the manufacturer
        manufacturer = product.getManufacturer().lower()
        # if manufacturer in merged_tt:
        #     manu_found = True
        # else:
        #     manu_found = False
        manu_found = Matcher.isInTokenizedString(manufacturer,merged_tt)
        #if the family is given, we also try to find it:
        family = product.getFamily().lower()
        #family = "".join(list(filter(lambda x: not x in "_- ",family)))
        if family!="":
            # if family in merged_tt:
            #     family_found = True
            # else:
            #     family_found = False
            family_found = Matcher.isInTokenizedString(family,merged_tt)
        else:
            family_found = False
        if (family_found and
            model_found and
            manu_found):
            return 2
        if (manu_found and
            model_found):
            return 1
        if manu_found and family_found:
            return 0
        return -1

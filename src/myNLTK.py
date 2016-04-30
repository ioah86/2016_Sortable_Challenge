#!/usr/bin/python3
"""
.. moduleauthor:: Albert Heinle<albert.heinle@gmail.com>
"""

import re

def word_tokenize(s):
    """
    This function does a very primitive adaptation of the tokenizer
    for NLTK and is only created in case someone has trouble
    installing NLTK on his/her machine. It returns a list of strings
    tokenizing the given string s.

    :param s: The string we want to tokenize
    :type  s: String
    :returns: A list of words contained in s
    :rtype:   [String]
    """
    res = re.split("; |\(|\)| |, |\.|\*|\n",s)
    res = list(map(lambda x: x.strip(),res))
    res = list(filter(lambda x: x!='', res))
    return res
    

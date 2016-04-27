#!/usr/bin/python3
"""
.. moduleauthor:: Albert Heinle<albert.heinle@gmail.com>
"""

"""
For the Matcher class, there are certain separator words like "for" and
"with", which indicate that anything that comes after that in a title
of a listing has nothing to do with the product. This list collects
all these words.
Assumption:
- all words must be given as lower-case
- The languages given are English, German, French
"""
separator_words = ["for", "with","pour","avec","mit","für","fuer"]

#!/usr/bin/python3
# coding=utf-8
"""
.. moduleauthor:: Albert Heinle<albert.heinle@gmail.com>
"""

import os


separator_words = ["for", "with","pour","avec","mit","für","fuer"]
"""
For the Matcher class, there are certain separator words like "for" and
"with", which indicate that anything that comes after that in a title
of a listing has nothing to do with the product. This list collects
all these words.
Assumption:
- all words must be given as lower-case
- The languages given are English, German, French
"""

number_of_threads = 4
"""
This variable encodes the number of threads running at most
in parallel.
"""

chunk_size = 1000
"""
This variable encodes the size of chunks of listings that are
handled by each thread
"""

result_path = os.path.join("..","results")
"""
This variable provides the path where result files and logs
should be stored.
"""

if not os.path.isdir(result_path):
    os.mkdir(result_path)


result_file = "results.txt"
"""
This variable describes the final result file name where all
the results are stored.
"""

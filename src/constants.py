#!/usr/bin/python3
"""
.. moduleauthor:: Albert Heinle<albert.heinle@gmail.com>
"""

import os

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


"""
The following variable encodes the number of threads running at most
in parallel.
"""
number_of_threads = 4

"""
The following variable encodes the size of chunks of listings that are
handled by each Thread
"""
chunk_size = 1000


"""
The following variable provides the path where result files and logs
should be stored.
"""
result_path = os.path.join("..","results")

"""
The following variable describes the final result file name where all
the results are stored.
"""
result_file = "results.txt"

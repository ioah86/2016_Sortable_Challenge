Welcome to Sortable Challenge 2016 README
=========================================

This is Albert Heinle's submission to the challenge as given by the
company "Sortable" (http://sortable.com/challenge/).

System requirements
-------------------

I programmed this submission in Python 3. The version I tested it with
is 3.4.3. As additional package(s) that might be installed via `pip3`, I
made use of

- nltk (http://www.nltk.org/) - Natural language processing for Python.
  Steps to install::

        $> pip3 install nltk
        $> python3
        Python 3.4.3 (default, Oct 14 2015, 20:28:29) 
        [GCC 4.8.4] on linux
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import nltk
        >>> nltk.download()
        NLTK Downloader
        ---------------------------------------------------------------------------
        d) Download   l) List    u) Update   c) Config   h) Help   q) Quit
        ---------------------------------------------------------------------------
        Downloader> d all
        
  and wait. Afterwards, exit the downloader and Python.
- Sphinx (http://www.sphinx-doc.org/en) for the generation of the
  documentation (optional)

**Remark:** The `d all` command downloads the whole nltk
functionality, and that might take a moment (depending on your
internet connection).

**Another Remark:** If you have trouble to install nltk, I have
written my own primitive tokenizer in the branch `without_nltk` of
this repository. However, this tokenizer is not as accurate, and one
might have less sound results compared to the results we would
get with nltk.


A Quick Test:
-------------

All modules have respective test modules. If you have `nosetests3`
installed, you can run::

        $> nosetests3 -v

inside the `src` folder of this project and if everything is OK, your system is properly
set up.


How to run:
-----------

You need two files to run the given script, namely a file containing
listings, and a file containing products. I included the sortable
challenge files into the project:

 - `test_files/sortable_listings.txt` (The listings)
 - `test_files/sortable_products.txt` (The products)

The script that tries to do the matchings is called `run_matching.py`
in the folder `src`. In order to run it with the sortable challenge
files, go to the folder `src` and type::

        $> python3 run_matching.py -p ../test_files/sortable_products.txt -l ../test_files/sortable_listings.txt

After that, there will be a folder `results` generated, with a
subfolder named after the timestamp when the `run_matching.py` script
was started. The script generates a couple of threads, each working on
a chunk of the listings at a time and writing their results into this
folder. In the end, there will be one `results.txt` file left (and a
log file), which contains the results of the computation.


**Remark:** There are certain parameters that can be set for the
project (like number of threads, size of the chunk that each thread
is working on, output folder path etc.). These parameters can be set
in `src/constants.py`.


Generating the Documentation
----------------------------

I used Sphinx to auto-generate the documentation of the project. In
order to obtain a documentation, go to the subfolder `doc` and run::

        $> make html

to get a documentation in HTML format. One can find the root
documentation file afterwards in `doc/_build/html/index.html`.

**REMARK:** Make sure your Sphinx version uses Python3 to interpret
  the module files. Otherwise, there might be errors when running the
  above command. 

Results:
--------

I ran the script ran on my machine (Intel core i5, ~2.4GHz, 16GB RAM)
on both versions that I have (with NLTK and without).

- With NLTK, it took about 2 minutes total time for the challenge data. The
  results file produced was about 1.4MB big.
- Without NLTK, the computation took 30s and created a same size
  result file as with NLTK.

TODOs:
------

 - Make script more robust against corrupt files (the challenge files
   were fortunately not corrupted)
 - Currently, NLTK is not used in its full potential. Introduce
   language recognition of postings and adapt algorithm accordingly
   (like information separator words we are currently using, e.g. 'for')

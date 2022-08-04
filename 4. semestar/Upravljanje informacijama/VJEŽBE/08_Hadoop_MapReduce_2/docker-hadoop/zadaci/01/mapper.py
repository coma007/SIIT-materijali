#!/usr/bin/python

import sys

# Input takes from standard input
for myline in sys.stdin:
    # Remove whitespace either side
    myline = myline.strip()
    # Break the line into words
    words = myline.split()
    # Iterate the words list
    for myword in words:
        # Write the results to standard output
        print('%s\t%s' % (myword, 1))

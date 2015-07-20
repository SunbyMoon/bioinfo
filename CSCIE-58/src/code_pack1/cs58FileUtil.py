# s50FileUtil
#
# Jeff Parker        Feb 2009
#
# File Handling utilities
# Other programs can use these utilities

import string
import sys

# Remove white space, change to upper case
def prepare(text):
    text = string.replace(text, " ", "")
    text = string.replace(text, "\n", "")
    text = string.replace(text, "\t", "")
    text = text.upper()
    return text

def readFastaFile(fileName):
    f = open(fileName, 'r')

    # First line in Fasta format is header
    line = f.readline()
    # print "Saw", line

    text = f.read()
    f.close()
    
    # Remove end of lines
    text = prepare(text)
    return text
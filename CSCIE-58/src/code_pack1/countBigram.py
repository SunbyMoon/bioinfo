# countBigram.py
# Ashkan Bigdeli
#
# Assignemnt 2 - Question 6
#
# This program will read in a Fasta file and
# count the number of bigrams in teh sequence. 
#
# Bugs: no validation that the file is a Fasta DNA file.
#       This program will not count overlapping Bigrams
# 
# Usage: To run on the Fasta file "NAMEOFFILE.fasta", type
#       % python tataat.py NAMEOFFILE.fasta

import sys
# check for correct command line arguemnt and present usage if needed
if (len(sys.argv) !=2):
    print "Usage: python", sys.argv[0], "<filename>"
else:
    # open file, read & print first line
    fileName = sys.argv[1]
    f = open(fileName, 'r')
    text = f.readline()
    print "Fasta info: ", text
    
    # read remainder of file, remove carriage returns, convert to lower case
    text = f.read()
    text = text.replace("\n", "")
    text = text.lower()
    
    # I found the useful count function, so I skipped a sperate method
    # and went right to printing them... formatting is as sensical as possible.  
    print ("    A        T       G       C" )
    print ("A " + str(text.count("aa")) +"  "+ str(text.count("at"))
            +"  "+ str(text.count("ag")) +"  "+ str(text.count("ac")) )
    
    print ("T " + str(text.count("ta")) +"  "+ str(text.count("tt"))
            +"  "+ str(text.count("tg")) +"  "+ str(text.count("tc")) )

    print ("G " + str(text.count("ga")) +"  "+ str(text.count("gt"))
            +"  "+ str(text.count("gg")) +"  "+ str(text.count("gc")) )

    print ("C " + str(text.count("ca")) +"  "+ str(text.count("ct"))
            +"  "+ str(text.count("cg")) +"  "+ str(text.count("cc")) )
            
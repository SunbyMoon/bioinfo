# tataat.py
# Ashkan Bigdeli
#
# Assignment 2 - Question 5
#
# This program will read in a Fasta file and find
# the first, last and number of TATAAT box occurences. 
#
# Bugs: no validation that the file is a Fasta DNA file.
# 
# Usage: To run on the Fasta file "EcoliK12.fasta", type
#       % python tataat.py EcoliK12.fasta


# import sys to take command line arguements, regex for regular expressions
import sys, re

# function to determine the # & index of TATAAT boxes in sequence
# I opted for regular expressions, might be my java background.
def findTATAAT (text):
    for x in re.finditer("tataat", text):
        boxes.append(x.start())
    return boxes

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
    
    # create array to store results, run find method
    boxes = []
    findTATAAT(text)
    
    # check to list has TATAAT, if no print message, if so print indexes. 
    if(len(boxes) < 1 ):
       print("Your file has no TATAAT boxes")
    else:
        print( "There are " + str(len(boxes)) + " TATAAT boxes." )
        print( "The first TATAAT is found at index: " + str(boxes[0]))
        print( "The last TATAAT is found at index : " + str(boxes[-1]) )
    
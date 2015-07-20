# repeat.py
# Ashkan Bigdeli
# Assignment 4
#
#This program finds the longest repeat in a string. 
#
# Bugs: no validation that the file is a Fasta DNA file.
#       Assumes contents are a, c, g, and t.
#       Long run times, unable to run for large sequences.
# 
# Usage: To run on the Fasta file "FILENAME.fasta", type
#       % python findTata.py FILENAME.fasta 

import sys
import cs58FileUtil


# longest_repeat
#
# @param1 = string to be tested for repeats
# @return1 = string that contains the longest repeat
#
#This method will take a string as input, parse it into
#all possible sub_strings and return said string if it is repeated.
#Note: This method will return the longest repeated string, not the longest string
# repeated the most often
def longest_repeat ( text ) :
    #instance variables
    longest = ""
    text_len = len(text)
    #itterate through the string and create substrings
    for i in range (0, text_len):
        for j in range (0, text_len):
            sub = text[i:j]
            # Use count to determine if the string is seen multiple times
            # if so, is it the longest we've found. if so record it. 
            if text.count(sub) > 1 and len(sub) > len(longest):
                longest = sub               
    return longest


#longest_repeat_index
#
#@param1 = string of original text
#@param2 = string of repeat
#param3 = list to be appended with indexes
#@return = a list of the indexes where the repeat is found

#This method will find all the indexes of a given sub-string in a string
def repeat_index(text, repeat):
    index = 0
    #incrementing the while loop by length of the repeat
    # so precalculate for efficiency
    len_text = len(text)
    repeat_len = len(repeat)
    indexes = []
    while index < len_text:
        index = text.find(repeat,index)
        #if the index is not found, itterate
        if index == -1:
            break
        #if this index is not contained in our list, add it
        if index not in indexes:
            indexes.append(text.find(repeat, index))
        #incremement by the length of our repeat to check for next index
        index += repeat_len
    return indexes
    
if (len(sys.argv) !=2):
    print "Usage: python", sys.argv[0], "<filename>"
else:

    fileName =sys.argv[1]
    text = cs58FileUtil.readFastaFile(fileName)
    
    repeat = longest_repeat(text)
    indexes = repeat_index(text,repeat)
    
    print fileName
    print "The length of the longest repeat is: ", len(repeat)
    print "This repeat is seen at locations: ", indexes
    print "The longest repeat sequence is: ", repeat[:100]

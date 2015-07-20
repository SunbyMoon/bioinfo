# AB_orf_finder.py  
# Assignment 3 2/25/15
#
#
# This program finds the longest orf in the forward direction
# based upon the limit provided by the user. 
#
# Starting Point for program to find Open Reading Frames
#and provided by:
#  
# Jeff Parker        Dec 2010
#
# You should have a copy of cs58FileUtil.py in view
# It is simplest to place it in the same directory as this source

import string
import sys
import cs58FileUtil

# We can override this value with a Command Line Parameter
limit = 300    # How many base pairs long must an ORF be?

# findAllORF
#This search routine only looks for ORFs in the forward direction
#No overlapping orfs are recorded and results are returned as a list.
#PRINTS FROM ROUNTINE FOR CLEANER OUTPUT THAN LIST STORAGE
def findAllOrf(text, limit):

    # create a set to test for stop codons
    stops = ["TAA","TAG","TGA"]
    
    #itterate over each reading frame
    for x in range ( 0, 3):
        
        # flag to determine if in orf
        in_orf = False
        seq_len = len(text)
        
        #start loop at first char of reading frame(indicted as x), increment +3
        for i in range (x, seq_len, 3):
            
            #if no start recorded => search
            if in_orf is False :
                if text[i:i+3] =='ATG':
                    start = i +1
                    #set flag that start is found
                    in_orf = True
                    
            else:#found start, look for stop        
                if text[i:i+3] in stops:
                    in_orf= False
                    
                    #set stop codon index to account for end of stop codon
                    stop = i + 3
                    orf_len = stop - start + 1
                    
                    # is this orf greater is greater than limit, print stats
                    if orf_len >= limit :
                        print 'Frame', x + 1, 'Start:', start, 'Stop:', stop, "Orf Length:", orf_len, "Sequence:", text[start+1:start+46]
                       
if ((len(sys.argv) < 2) or (len(sys.argv) > 3)):
    print "Usage: python", sys.argv[0], "<filename> [<min ORF length>]"
else:
    fileName = sys.argv[1]
    if (len(sys.argv) > 2):             # This should be an integer
        try:
            limit = int(sys.argv[2])    # Convert string to integer
        except ValueError:              # try-except catches errors
            print "\n\tExpecting an integer to define min ORF length, found",
            print sys.argv[2]
            exit()

    print "ORF must be at least", limit, "Base pairs long"
    
    text = cs58FileUtil.readFastaFile(fileName)
    
    # Time to start finding ORFs!
    findAllOrf(text, limit)
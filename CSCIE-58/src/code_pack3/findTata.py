#findTata.py
#Ashkan Bigdeli 
# Assignment 4 2/25/15
#
# This program provides base counts for all Tata boxes found inside an orf
# of the user set length. 
#
# Bugs: no validation that the file is a Fasta DNA file.
#       Assumes contents are a, c, g, and t. Only finds orfs in forward direction.
# 
# Usage: To run on the Fasta file "FILENAME.fasta" and orf length, type
#       % python findTata.py FILENAME.fasta 100

import sys
import cs58FileUtil



#findAllOrfStarts
#
#@param1 = text of the sequence
#@param2 = minimum orf length
#@return = list of start codons
#
#This method will find all orfs of the minimum length in the forward direction
def findAllOrfStarts(text, limit):

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
                    start = i 
                    #set flag that start is found
                    in_orf = True
                    
            else:#found start, look for stop        
                if text[i:i+3] in stops:
                    in_orf= False
                    
                    #set stop codon index to account for end of stop codon
                    stop = i + 3
                    orf_len = stop - start
                    
                    # is this orf greater is greater than limit, print stats
                    if orf_len >= limit :
                        starts.append(start)
    print len(starts)
    return starts


#findTATA
#@param1 = the text of the sequence
#@param2 = a list of start codons
#@return = a list of all relevant tata boxes
#
#This method will take a start codon position and return
#the tata box(if any) closest to the -10 position and with 
#a hemming distance of greater 2 or less.                     
def findTATA ( text, starts ):
    print len(starts)
    boxes = []                   
    # itterate through array of starts and create substrings
    for i in range (0, len(starts)):
        #variables for intitial locations of tataa check
        x = 10
        y = 4
        lowest_hem = 0
        #incremenet each substring to walk promoter region
        for j in range (0,4):
            count = 0
            start = text[starts[i] - (x - j) : starts[i] - (y-j)]
            #series of conditionals to check for tataat
            if start[0] == 'T':
                count +=1
            if start[1] == 'A':
                count +=1
            if start[2] == 'T':
                count +=1
            if start[3] == 'A':
                count +=1
            if start[4] == 'A':
                count +=1
            if start[5] == 'T':
                count +=1
            # if we have a hemming distance of greater than 4, is tata, add to list
            if count > 3 and count > lowest_hem:
                lowest_hem = count
                boxes.append(start)
    return boxes

#printBoxBaseCount
#@param1 = a list of tata boxes
#
#This method will analyze each tata box and store base
#counts in a base specific array. Each array is then PRINTED.
def printBoxBaseCount ( boxes ):
    #create arrays for each base
    a = [0,0,0,0,0,0]
    g = [0,0,0,0,0,0]
    t = [0,0,0,0,0,0]
    c = [0,0,0,0,0,0]
    for i in range (0, len(boxes)):
        tata = boxes[i]
        for j in range (0,len(tata)):
            if tata[j] == 'A':
                a[j] += 1
            if tata[j] == 'G':
                g[j] += 1
            if tata[j] == 'T':
                t[j] += 1            
            if tata[j] == 'C':
                c[j] += 1 
    print "A", a
    print "C", c
    print "G", g
    print "T", t
                
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
    starts = []
    findAllOrfStarts(text, limit, starts)
    boxes = findTATA(text, starts)
    printBoxBaseCount( boxes )
    
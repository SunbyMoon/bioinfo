# Ashkan Bigdeli
# Assignment 3
# findPalindrome.py
#
#
#
import string
import sys
import cs58FileUtil

# I found this method of creating a complimentary strand
# in a biopython thread. Uses A dictionary to find and
# replace values in sequence. I tried if, elses and replace
# for replacement and even found a nice translate method
# in python 3, but this was the only version I was able
# to get working. 
def comp_strand( seq ): 
    #create a dictionary of bases to replace
    comps = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    #create a list of characters in sequence
    letters = list(seq)
    #itterate of letters of sequence and replace values
    letters = [comps[base] for base in letters]
    #join and return as string
    return ''.join(letters) 
    
# This method will itterate over the first string, and then the second
# submitting the substrings to the recusirve method isPalindrome
# if a True result is returned, and is longer than the previous result
# the result will be logged and returned as a string.
def find_palindromes ( seq, comp_seq ):
    
    #Instance Variables
    seq_length = len(seq)
    rev_comp = comp_seq[::-1]
    rev_comp_seq_length = len(comp_seq)
    longest_pal =""
    pos = 0
    # Itterate through each character of sequence
    for i in range (0, seq_length-2):       
        #submit corresponding char to isPalindrome to verify
        for j in range (0, rev_comp_seq_length-2):
            #if true and longer than previous, record
            if isPalindrome (seq[i:], rev_comp[j:]):
                if (len(seq[i:]) > len(longest_pal)):
                    longest_pal = seq[i:]
                    pos = i +1
                    
    longest_pal = "Longest Palindrome @ Position: ", pos, "Sequence:", longest_pal               
    return longest_pal


#This a recursive method I previously developed for checking
# palindromes of a single small string. I thought
# to use it to submit substrings to here and return true
# if indeed the substring is a palindrome
def isPalindrome (sub_seq, sub_comp ):
    sub_seq_length= len(sub_seq)
    sub_comp_length= len(sub_comp)
    # base case for recursion
    if sub_seq_length<=1 or sub_comp_length <=1 :
        return True
    #if first char equals last char, call method again
    if sub_seq[0] == sub_comp[0]:
        return isPalindrome(sub_seq[1:], sub_comp[1:])
        
    # if this statement is reached, it cannot be a palindrome
    return False
        
if (len(sys.argv) !=2):
    print "Usage: python", sys.argv[0], "<filename>"
else:
    fileName =sys.argv[1]
    seq = cs58FileUtil.readFastaFile(fileName)
    comp_seq =comp_strand(seq)
    print find_palindromes(seq, comp_seq)
    

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

def find_palindromes ( seq, comp_seq ):
    seq_length = len(seq)
    #create the reverse compliment
    rev_comp = comp_seq[::-1]
    longest_pal =""
    pos = 0
    count = 0
    for i in range (0, seq_length):
        for j in range (0, seq_length-2):
            if seq[i]==rev_comp[j]:
                count = count +1
                if (count > count2):
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
    # base case for recursion
    if sub_seq_length<=1 :
        return True
    #if first char equals last char, call method again
    if sub_seq[0] == sub_comp[-1:]  :
        return isPalindrome(sub_seq[1:], sub_comp[:-1])
        
    # if this statement is reached, it cannot be a palindrome
    return False
        
if (len(sys.argv) !=2):
    print "Usage: python", sys.argv[0], "<filename>"
else:
    fileName =sys.argv[1]
    seq = cs58FileUtil.readFastaFile(fileName)
    seq = "GCATGGTTATGCATAACCATG"
    print seq
    comp_seq =comp_strand(seq)
    print comp_seq[::-1]
    print find_palindromes(seq, comp_seq)
    

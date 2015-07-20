# Turn DNA sequence to Amino Acid Sequence
# Jeff Parker      Jan 2010
# 
# Starting point for counting codons to test Grantham's Genome Hypothesis

import sys        # Command Line argument

# Remove \n, change to lower case
def prepare(text):
    text = text.replace("\n", "")
    text = text.lower()
    return text

# Read a fasta file into a string
def readFastaFile(fileName):
    f = open(fileName, 'r')

    # First line in Fasta format is header
    line = f.readline()
    # print "Saw", line

    text = f.read()
    text = prepare(text)
    return text

# Dictionary holding the code to life: Codon to Amino Acid map
code = {     'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
             'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
             'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
             'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
             'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
             'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
             'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
             'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
             'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
             'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
             'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
             'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
             'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
             'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
             'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
             'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
        }

# Function to translate a DNA string to an AA string
# It is faster to use a list and join, but the time
# saved is less than 10%
def translate(text):
    result = ""

    # Starting at 0, run until end, skipping 3
    for i in xrange(0, len(text) + 1 - 3, 3):
        codon = text[i:i+3]
        if (codon in code):
            result = result + code[codon]

    return result

if (len(sys.argv) < 2):
    print "Usage:   python", sys.argv[0], "<filename>"
else:
    fileName = sys.argv[1]
    print fileName
    
    text = readFastaFile(fileName)

    protein = translate(text)
    
    print protein
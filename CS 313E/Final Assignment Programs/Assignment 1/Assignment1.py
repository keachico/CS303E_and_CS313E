# File: Assignment1.py
#
# Description: Reads text from an existing file then filters certain words to a new text file. 
#
# Student's Name: Kevin Achico
#
# Student's UT EID: ka6893
#
# Course Name: CS 313E 
#
# Date Created: September 15, 2012
#
# Date Last Modified: September 17, 2012

import string

def main():

    filterFile('newwordlist.txt', 'wordsOfLength7.txt', hasLength7)
    filterFile('newwordlist.txt', 'LWords.txt', firstLetterL)
    filterFile('newwordlist.txt', 'wordsQ.txt', findLetterQ)
    filterFile('newwordlist.txt', 'palindromes.txt', findPalindrome)

def filterFile(inputFileName, outputFileName, f):
    
    myinputFile = open(inputFileName, 'r') #reads the file specified in the argument
    myoutputFile = open(outputFileName, 'w') #creates a new file
    
    input_count = 0
    output_count = 0
    
    for word in myinputFile:
        input_count += 1 #keeps track of input file words
        word = word.rstrip('\n') #disregards the extra space line for ever word in the input file
        
        if f(word):
            output_count += 1 #counts every word that passes through the filter function
            myoutputFile.write(word + "\n") #prints the words to the output file with a new line
 
    myoutputFile.write("There are %d words in the input file and %d words that passed to this file." % (input_count, output_count)) #writes total number of words in input file

    myinputFile.close()
    myoutputFile.close()

def hasLength7(word):
    return len(word) == 7 #returns true if word has length of 7

def firstLetterL(word):
    word = str.lower(word)
    return word[0] == 'l' #returns true if first index is 'l'

def findLetterQ(word):
    return str.find(word, 'q') != -1 #returns true if word has 'q' in it
    
def findPalindrome(word):
    Palin = word[-1::-1]
    return word == Palin #returns true if word is a palindrome



    
main()

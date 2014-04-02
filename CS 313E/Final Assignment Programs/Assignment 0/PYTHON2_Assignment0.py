# File: Assignment0.py
#
# Description: Prompt user for a line of text and return the same line but modified. Also displays letter count. 
#
# Student's Name: Kevin Achico
#
# Student's UT EID: ka6893
#
# Course Name: CS 313E 
#
# Date Created: September 2, 2012
#
# Date Last Modified: September 9, 2012

import string

def main():
    str1 = raw_input("Please enter a string: ")

    while (str1 != ''):
        modify(str1)
        str1 = raw_input("Please enter a string: ")
        
def modify(str1):
    print "User's input: ", str1
    print "In Uppercase: ", string.upper(str1)
    print "In Lowercase: ", string.lower(str1)
    count_letter(str1)
    cipher(str1)

def count_letter(str1):
    list_letters = "abcdefghijklmnopqrstuvwxyz"
    lower_string = string.lower(str1)
    for ch in list_letters:
        count = 0
        for ch2 in lower_string:
            if ch == ch2:
                count = count + 1
        print ch, ":", count

def cipher(str1):
    
    alpha = "abcdefghijklmnopqrstuvwxyz"
    str1 = string.lower(str1) #change str1 to all lowercase letters
    new_string = ''

    for ch in str1:  #goes through every letter in str1
        if ch == ' ': #case when ch is a space
            new_string = new_string   
        else:
            letter_index = string.find(alpha, ch) #index of ch in the alphabet
            if (letter_index == 25): # special case - 'z'
                new_letter = "a"
                new_string = new_string + new_letter
            elif (letter_index == -1): # special case - non-letters
                new_string = new_string
            else: 
                new_letter = alpha[(letter_index)+ 1 ] #change ch to next letter in alphabet
                new_string = new_string + new_letter
    print new_string
    
main()

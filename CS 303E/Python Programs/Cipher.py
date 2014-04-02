# File: Cipher.py
# Description: Program that prompts the user for a string and implements a Caesar Cipher.
# Assignment Number: 6
#
# Name: Kevin Achico
# EID: ka6893
# Course Name: CS303E
#
# Unique Number: 52770
#
# Date created: March 19, 2012
# Date last modified: March 20, 2012
#
# Slip days used this assignment: 0
# Total slip days used: 0

import string

def main():
    message = raw_input("Please enter a string to be decoded: ")
    key_value = input("Please enter the key value: ")
    print "Should the encoded message be in lower case, upper case, or as is?"
    message_format = raw_input('Please enter "lower", "upper", or "as is": ')

    if (message_format == "lower"):
        print string.lower(message)
    elif (message_format == "upper"):
        print string.upper(message)
    elif (message_format == "as is"):
        print message
main()

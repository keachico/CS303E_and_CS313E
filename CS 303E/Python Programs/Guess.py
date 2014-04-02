# File: Guess.py
# Description: Game designed to ask a user to guess a number between 1 and 100.
# Assignment Number:4
#
# Name: Kevin Achico
# EID: ka6893
# Course Name: CS 303E
#
# Unique Number: 52770
#
# Date created: February 20, 2012
# Date last modified: February 21, 2012
#
# Slip days used this assignment: 0
# Total slip days used: 0

import random

def main():

    number=random.randint(1,100) #get a random integer between 1 and 100

    print "Welcome to the High-Low Guessing Game! \
    \nTry to guess the number I've chosen between 1 and 100."

    guess = input("\nWhat is your guess? ") 
    count = 1 #keeps track of how many times the user guesses

    while (guess != number) and (guess != -1): #a while loop that will repeat until the user guesses the correct number or enters -1 to quit
        if (guess > number): #prints statement if guess is too high
            print "%d is high." % guess
        elif(guess < number): #prints statement if guess is too low
            print "%d is low." % guess
        guess = input("What is your guess? ")
        count = count + 1 #adds 1 to the count everytime the user guesses wrong
    
    if (guess != -1): #decides whether or not to print out the 'correct' statement if the guess is anything other than -1
        print "Correct! You only needed %d guesses to get it!" % count
        
main()



##TEST CASE 1:
##
##Welcome to the High-Low Guessing Game!     
##Try to guess the number I've chosen between 1 and 100.
##
##What is your guess? 50
##50 is high.
##What is your guess? 25
##25 is high.
##What is your guess? 10
##10 is high.
##What is your guess? 5
##5 is low.
##What is your guess? 8
##8 is low.
##What is your guess? 9
##Correct! You only needed 6 guesses to get it!




##TEST CASE 2:
##
##Welcome to the High-Low Guessing Game!     
##Try to guess the number I've chosen between 1 and 100.
##
##What is your guess? 75
##75 is high.
##What is your guess? 25
##25 is low.
##What is your guess? 50
##50 is high.
##What is your guess? 45
##45 is high.
##What is your guess? 99
##99 is high.
##What is your guess? 98
##98 is high.
##What is your guess? 97
##97 is high.
##What is your guess? 96
##96 is high.
##What is your guess? 40
##40 is high.
##What is your guess? 35
##35 is low.
##What is your guess? 38
##38 is low.
##What is your guess? 39
##Correct! You only needed 12 guesses to get it!




##TEST CASE 3: Enter -1 to quit the game.
##
##Welcome to the High-Low Guessing Game!     
##Try to guess the number I've chosen between 1 and 100.
##
##What is your guess? 100
##100 is high.
##What is your guess? 0
##0 is low.
##What is your guess? 50
##50 is high.
##What is your guess? 75
##75 is high.
##What is your guess? 25
##25 is low.
##What is your guess? -1




##TEST CASE 4:
##
##Welcome to the High-Low Guessing Game!     
##Try to guess the number I've chosen between 1 and 100.
##
##What is your guess? 1
##1 is low.
##What is your guess? 2
##2 is low.
##What is your guess? 50
##50 is low.
##What is your guess? 88
##88 is high.
##What is your guess? 75
##75 is high.
##What is your guess? 60
##60 is low.
##What is your guess? 65
##65 is low.
##What is your guess? 69
##69 is high.
##What is your guess? 68
##Correct! You only needed 9 guesses to get it!




##TEST CASE 5:
##
##Welcome to the High-Low Guessing Game!     
##Try to guess the number I've chosen between 1 and 100.
##
##What is your guess? 91
##91 is high.
##What is your guess? 73
##73 is high.
##What is your guess? 50
##50 is high.
##What is your guess? 42
##42 is high.
##What is your guess? 31
##31 is low.
##What is your guess? 40
##40 is high.
##What is your guess? 35
##35 is low.
##What is your guess? 38
##Correct! You only needed 8 guesses to get it!

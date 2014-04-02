#  Files: Card.py, Deck.py, Hand.py, Poker.py
#
# Description: Program which imitates a deck of cards playing poker. 
#
# Student's Name: Kevin Achico
#
# Student's UT EID: ka6893
#
# Course Name: CS 313E 
#
# Date Created: September 28, 2012
#
# Date Last Modified: October 1, 2012

"""This is the driver routine for my Poker playing program.
It is interactive with the user supplying a positive number of
hands to ’play.’ These are generated and evaluated, with the result
printed for each hand. We generate a new deck every time we run
short on cards in the current deck.
"""
from Deck import *
from Hand import *
from Card import *

def dealSomeHands():
    
    # Generate the initial deck and shuffle it.
    d = Deck()
    d.shuffle()
    
    # Find out from the user how many hands to generate.
    while True:
        # Run this while loop until we get a legal (positive
        # integer) answer from the user.
        nStr = input("How many hands should I deal? ")
        if not nStr.isdigit():
            print (" Positive number required. Try again!")
        else:
            n = int( nStr ); break

    # Generate n hands.
    for i in range( n ):
        # If there are not enough cards left in the deck
        # to deal a hand, generate and shuffle a new deck.  
        if ( len(d) < 5 ):
            print("\nDealing a new deck.")
            d = Deck()
            d.shuffle()
        # Generate a new hand, print it, and evaluate it.
        h = Hand(d)
        print("\nHand drawn (", i + 1, "): ", sep="")
        print(h)
        print( h.evaluateHand() )

# This is a trick to allow executing this if we’re at the
# "top level" and not otherwise. This keeps this code from
# being run when I just import this class.

if __name__ == '__main__':
    dealSomeHands()



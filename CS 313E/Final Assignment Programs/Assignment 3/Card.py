# Files: Card.py, Deck.py, Hand.py, Poker.py
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


import random

class Card:
    
    """A card object with a suit and rank."""
    # These are class attributes, not instance attributes

    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    SUITS = ("Spades", "Diamonds", "Hearts", "Clubs")

    # This is called as Card(rank, suit).

    def __init__(self, rank, suit):
    #"""Create a Card object with the given rank and suit."""
    
        if (not rank in Card.RANKS or not suit in Card.SUITS ):
            print ("Not a legal card specification.")
            return

        self._rank = rank
        self._suit = suit

    def getRank(self):
    #"""Return my rank."""
    
        return self._rank
    
    def getSuit(self):
    #"""Return my suit."""
    
        return self._suit
    
    def __str__(self):
    #"""Return a string that is the print representation
    #of this Card’s value."""
        # Create a dictionary for the special cases.
        translate = { 1:"Ace", 11:"Jack", 12:"Queen", 13:"King" }
        r = self._rank
        # See if r is a special case (printwise).
        if r in [1, 11, 12, 13]:
            myrank = translate[r]
        else:
            myrank = str( r )
        return myrank + " of " + self._suit



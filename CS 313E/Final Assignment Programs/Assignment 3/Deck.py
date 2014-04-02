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


import random
from Card import *

class Deck:
    """Definition of the Deck class. Each Deck is just a list of
    cards. It is initialized to contain the full deck of 52 cards."""
    
    def __init__(self):
    #"""Return a new deck of cards."""
        self._cards = []
        # For each suit and each rank, generate a card and add it to the deck.
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                c = Card(rank, suit)
                self._cards.append(c)

    def shuffle(self):
    #"""Shuffle the cards in place."""
        # Note that random.shuffle is a method on Lists,
        # not on Decks. If we want to shuffle a Deck, we
        # have to define it ourselves.
        
        random.shuffle(self._cards)

    def deal(self):
    #"""Remove and return the top card, or None
    #if the deck is empty."""

        # The following only works because we’ve
        # defined __len__ below.
        
        if len(self) == 0:
            return None
        else:
            
        # Removes the top card from the deck and
        # returns it.
            return self._cards.pop(0)


    def __len__(self):
    #"""Returns the number of cards left in the deck."""
        return len(self._cards)

    def __str__(self):
        result = ""
        for c in self._cards:
            result = result + str(c) + "\n"
        return result

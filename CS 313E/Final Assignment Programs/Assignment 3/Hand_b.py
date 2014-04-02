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


import Card
from Deck import *

class Hand:
    """A hand is simply a list of 5 cards, dealt from the deck."""

    # Note that we have to pass in a Deck because we need
    # a place from which to draw the cards.
    def __init__(self, deck):
        """A hand is simply the first five cards in the deck, if there are
        five cards available.  If not, return None."""
        self._hand = []
        for i in range(5):
            self._hand.append(deck.deal())

        self.ranks = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        for card in self._hand:
            cardRank = card.getRank()
            self.ranks[cardRank-1] += 1

        self.suits = [0,0,0,0]
        for card in self._hand:
            cardSuit = card.getSuit()
            if cardSuit == "Spades":
                self.suits[0] += 1
            elif cardSuit == "Diamonds":
                self.suits[1] += 1
            elif cardSuit == "Hearts":
                self.suits[2] += 1
            else:
                self.suits[3] += 1
            
    def __str__(self):
        """The string representation of the Hand, which is just the
        five cards."""
        result = ""
        for i in self._hand:
            result += str(i) + "\n"
        return result

    def hasRoyalFlush(self):
        return (5 in self.suits and 1 in self.ranks[9:] and 1 in self.ranks[0])

    def hasStraightFlush(self):
        for i in range(len(self.ranks)):
            if self.ranks[i] == 1:
                for j in self.ranks[i:i+5]:
                    if j == 0:
                        return False
                return (5 in self.suits)

    def hasFourOfAKind(self):
        return (4 in self.ranks)

    def hasFullHouse(self):
        return (3 in self.ranks and 2 in self.ranks)

    def hasFlush(self):
        return (5 in self.suits)

    def hasStraight(self):
        for i in range(len(self.ranks)):
            if self.ranks[i] == 1:
                for j in self.ranks[i:i+5]:
                    if j == 0:
                        return False
                return True

    def hasThreeOfAKind(self):
        return (3 in self.ranks)

    def hastwoPair(self):
        return (self.ranks.count(2) == 2)
        
    def hasPair(self):
        """Return a boolean indicating whether
        the current hand contains a pair."""
        return (2 in self.ranks)
    

    def evaluateHand(self):
        if self.hasRoyalFlush():
            return "Royal Flush"
        elif self.hasStraightFlush():
            return "Straight Flush"
        elif self.hasFourOfAKind():
            return "Four of a kind"
        elif self.hasFullHouse():
            return "Full House"
        elif self.hasFlush():
            return "Flush"
        elif self.hasStraight():
            return "Straight"
        elif self.hasThreeOfAKind():
            return "Three of a Kind"
        elif self.hastwoPair():
            return "Two Pair"
        elif self.hasPair():
            return "Pair"
        else:
            return "Nothing"

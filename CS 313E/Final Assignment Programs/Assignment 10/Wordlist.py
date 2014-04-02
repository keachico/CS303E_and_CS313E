#  File: Wordlist.py
#
#  Description: This module contains the Wordlist class.
#
#  Student's Name: Kevin Achico, Nadeem Abha
#
#  Student's UT EID: ka6893, na4333
#
#  Course Name: CS 313E 
#
#  Date Created: 12/1/12
#
#  Date Last Modified: 12/4/12

from Trees import *

# Check length of the word: 5-6 characters
def lengthCheck(word):
    return (len(word) == 6 or len(word) == 5)

# insertion code from the notes
def insertionSort(lst):
    for index in range(1, len(lst)):
        v = lst[index]
        flag = False
        for j in range(index):
            if lst[j] >= v:
                ind = j
                flag = True
                break
        if flag:
            lst.pop(index)
            lst.insert(ind, v)
    return lst

def binarySearch(lst, x, lo=0, hi=None):
    """This implements a binary search for x on a
    list lst, between indices lo and hi.  The index
    is returned if x is found, else -1 is returned."""
    comparisons = 0
    if hi == None:
        hi = len(lst)
    while lo < hi:
        comparisons += 1
        mid = (lo + hi)//2
        midval = lst[mid]
        if midval < x:
            lo = mid+1
        elif midval > x: 
            hi = mid
        else:
            return (mid, comparisons)
    return (False, comparisons)

class Wordlist:

    # generate a wordlist, and a counter variable to keep track of length. 
    def __init__(self):
        self._WL = []
        self._count = 0

    def __len__(self):
        return self._count

    def isEmpty(self):
        return self._WL == []

    def addWord(self, word):
        if lengthCheck(word):
            self._WL.append(word)
            self._count += 1

    def addWordsFromFile(self, filename):
        count = 0
        for word in filename:
            word = word.rstrip('\n')
            
            if lengthCheck(word):
                self.addWord(word)
                count += 1
        return count

    def removeWord(self, word):
        self._WL.remove(word)
        self._count -= 1

    # take into account that lines in external list have '\n' at the end.
    # return count for statistical purposes.
    def findWord(self, word):
        count = 0
        for line in self._WL:
            count += 1
            if line == (word):
                return (True, count)
        return (False, count)

    # added str function for tests of functionality.
    def __str__(self):
        return str(self._WL)


class BinaryTreeWordlist (Wordlist):

    #generates a BinarySearchTree
    def __init__(self):
        Wordlist.__init__(self)
        self._wordtree = BinarySearchTree()

    #checks the length, creates a node for the word, and inserts it itno the wordtree
    def addWord(self, word):
        if lengthCheck(word):
            node = BinaryTreeNode(word)
            self._wordtree.insert(word)

    #Uses the findWord method to see if the word is in the wordtree. If not, then insert in correct place.
    def findWord(self, word):
        return self._wordtree.inTree(word)

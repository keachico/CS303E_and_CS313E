#  Files: Permutations.py, Wordlist.py, Solver.py
#
#  Description:
#
#  Student's Name: Kevin Achico
#
#  Student's UT EID: ka6893
#
#  Course Name: CS 313E 
#
#  Date Created: 10/23/12
#
#  Date Last Modified:

def lengthCheck(word):
    return (len(word) == 6 or len(word) == 5)

class Wordlist:

    def __init__(self):
        self._wordlist = []

    def __len__(self):
        return len(self._wordlist)

    def isEmpty(self):
        return not len(self._wordlist)

    def addWord(self, word, lengthCheck):
        if lengthCheck(word):
            self._wordlist.append(word)
        
    def addWordsFromFile(self, filename, lengthCheck):
        
        theFile = open(filename, 'r')
        
        for word in theFile:
            word = word.rstrip('\n')
            
            if lengthCheck(word):
                self._wordlist.append(word)

    def removeWord(self, word):
        if word in self._wordlist:
            self._wordlist.remove(word)

    def findWord(self, word):
        count = 0
        for x in self._wordlist:
            count += 1
            if x == word:
                return (word in self._wordlist, count)
        return (False, count)
        
    def __str__(self):
        print (self._wordlist)

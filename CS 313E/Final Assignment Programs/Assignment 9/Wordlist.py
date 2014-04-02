#  File: Wordlist.py
#
#  Description: This module contains the Wordlist class and the
#               the HashedWordlist class that inherits methids from
#               Wordlist(ADT)
#
#  Student's Name: Nadeem Abha, Kevin Achico
#
#  Student's UT EID: na4333, ka6893
#
#  Course Name: CS 313E 
#
#  Date Created: 11/25/12
#
#  Date Last Modified: 11/28/12

# Check length of the word: 5-6 characters
def lengthCheck(word):
    return (len(word) == 6 or len(word) == 5)

# Wordlist(ADT)
class Wordlist:
    # Initialze a list
    def __init__(self):
        self._wordlist = []
        
    # get the length of the list
    def __len__(self):
        return len(self._wordlist)
    
    # check if the list is empty
    def isEmpty(self):
        return not len(self._wordlist)
    
    # add a word to the list if the word is 5-6 characters
    def addWord(self, word):
        if lengthCheck(word):
            self._wordlist.append(word)
            
    # Open the text file and read in each word into the list    
    def addWordsFromFile(self, filename):
        
        theFile = open(filename, 'r')
        count = 0
        for word in theFile:
            word = word.rstrip('\n')
            
            if lengthCheck(word):
                self.addWord(word)
                count += 1
        return count
    
    # remove a word form the list
    def removeWord(self, word):
        if word in self._wordlist:
            self._wordlist.remove(word)
            
    # See if a word exists in the list and find the occurance of it
    def findWord(self, word):
        count = 0
        for x in self._wordlist:
            count += 1
            if x == word:
                return (True, count)
        return (False, count)
    
    # print the list
    def __str__(self):
        lst = print(self._wordlist)
        return (lst)
        

def computeHash ( word, tableSize ):
        """For this version, compute the index i of the character
        in the range [a..z]. Then multiply by the ith prime.  This
        hash will have the attribute that it is indifferent to
        permuations.
        """
        
        PRIMES2=[  2,  3,  5,  7, 11, 13, 17, 19, 23, 29,
                  31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
                  73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
                  127, 131, 137, 139, 149, 151, 157, 163, 167, 173 ]
        
        hash = 1
        for ch in word:
            i = ord(ch) - ord('a')
            hash *=  PRIMES2[i]
        return hash % tableSize

class HashedWordlist (Wordlist):
    
    # Initialize a hashed wordlist using a prime number: 10007
    def __init__(self):
        Wordlist.__init__(self)
        self._HT = []
        for i in range(10007):
            self._HT.append([])

    # add a word to the hashed list    
    def addWord(self, word):
        h = computeHash(word, 10007)
        self._HT[h].append(word)

    # find a permutation of a word based on the hashed word list    
    def findPerm(self, word):
        count = 0
        key = computeHash(word, 10007)
        if self._HT[key] == []:
            return (False, 0)
        elif self._HT[key] != [None]:
            for i in self._HT[key]:
                count += 1
                if sorted(i) == sorted(word):
                    return (i, count)
                    break
            else:
                return (False, count)

    # find the number of empty buckets and the
    # average number of items in the hashtable
    def loadFactor(self):
        count = 0
        avg = 0
        for i in range(len(self._HT)):
            if len(self._HT[i]) != 0:
                count += 1
                avg += len(self._HT[i])
        if count > 0:
            avg = avg/count
        emptyCount = (len(self._HT)) - count
        return (emptyCount, avg)
                
            
        


    
    

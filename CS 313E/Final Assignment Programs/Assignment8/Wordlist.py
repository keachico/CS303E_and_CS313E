#  Files: Permutations.py, Wordlist.py, Solver.py, README.txt
#
#  Description: The Wordlist(ADT) and SortedWordlist(ADT)
#               generates a list of words from UnorderedWordlist.txt
#
#  Student's Name: Kevin Achico, Nadeem Abha
#
#  Student's UT EID: ka6893, na4333
#
#  Course Name: CS 313E 
#
#  Date Created: 11/9/12
#
#  Date Last Modified: 11/13/12



# Check length of the word: 5-6 characters

def lengthCheck(word):
    return (len(word) == 6 or len(word) == 5)
    

def binarySearch(lst, x, lo = 0, hi = None):
    """This implements a binary search for x on a
    list lst, between indices lo and hi.  The index
    is returned if x is found, else -1 is returned."""
    comparisons = 0
    if hi is None:
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
    return (-1, comparisons)



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
        
        for word in theFile:
            word = word.rstrip('\n')
            
            if lengthCheck(word):
                #self._wordlist.append(word)
                self.addWord(word)
        
        #insertionSort(self._wordlist)
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


class SortedWordlist(Wordlist):
    # Overide the intitializer
    def __init__(self):

        Wordlist.__init__(self)
        self._wordlist = []
        
    # Create an insertionSort method for
    # SortedWordlist(ADT)
    def insertionSort(self, lst, word):

        if self.isEmpty():
            lst.append(word)


        elif not self.isEmpty():
            
            for current_word in lst:
                if word < current_word:
                    index = lst.index(current_word)
                    lst.insert(index, word)
                    break
            if lst[-1] < word:
                lst.append(word)
               
    def addWord(self, word):
        
        if lengthCheck(word):
            self.insertionSort(self._wordlist, word)

        

    def findWord(self, word):
        return(binarySearch(self._wordlist, word, lo = 0, hi = None))
        


    

        
        











#  Files: Permutations.py, Wordlist.py, Solver.py, README.txt
#
#  Description: Use flat and sorted word lists
#
#  Student's Name: Nadeem Abha, Kevin Achico
#
#  Student's UT EID: na4333, ka6893 
#
#  Course Name: CS 313E 
#
#  Date Created: 11/9/12
#
#  Date Last Modified: 11/13/12

from Permutations import *
from Wordlist import *
import time
import sys

def main():

    # The next if fakes command line arguments by setting sys.argv explicitly.

    line = input('')
    sys.argv = line.split()
    
    if len( sys.argv ) == 1:
        # The user didn't supply any command line args, so we have to set
        # them manually.
        # Change this if you need to 
        sys.argv = ["Solver.py", "flat"]

    while len( sys.argv ) < 2:
        print("Please supply a command line argument: flat or sort.")
        print("Re-enter command.")
        line = input('')
        sys.argv = line.split()
        
    if sys.argv[1] == "flat":
        word_lst = Wordlist()
        print("Using flat unsorted wordlist.")
        
    elif sys.argv[1] == "sort":
        word_lst = SortedWordlist()
        print("Using sorted wordlist.")
        
    start = time.time()
    word_lst.addWordsFromFile("UnorderedWordlist.txt")
    

    # stop timer
    end = time.time()

    # Print the name of the list, the number of words in the list, and
    # the time it took to generate that word list
    #print ("Using sorted wordlist")
    print ("The Wordlist contains " + str(len(word_lst)) + " words.")
    print ("Building the Wordlist took %2.3f seconds." % (end - start))
    print ("")

    
    while True:
        
        # Ask user to input a word
        word = input("Enter a scrambled word (or EXIT): ")

        # If the user types "exit", break the program
        if word.lower() == "exit":
            print("Thanks for playing! Goodbye.")
            break
        # If the word if less than 5 letters or more than 6 letters,
        # ask the user to input a 5 or 6 letter word
        if (len(word)<5 or len(word)>6):
            print("You did not enter a 5 or 6 letter word, try again")
            print("")
            continue
            
        # find the number of total and unique permutations of the users word
        x, y = howManyPerms(word)
        print ("Found %d permutations; %d unique permutations" % (x,y))

        # start timer for comparing the permutations generated, with the
        # list of words from Wordlist(ADT)
        start2 = time.time()

        # Initialize a count for the number of permutations checked, before
        # a match is found in the Wordlist(ADT)
        count = 0
        comparisonsMade = 0
        found = False

        
        for perm in allPerms(word):
            count += 1
            # If the permutation generated matches a word from the Wordlist(ADT)
            # print the word found
            if perm in word_lst._wordlist:
                index, comparisons = word_lst.findWord(perm)
                comparisonsMade += comparisons
                # stop timer for comparing the permutations with words
                # from Wordlist(ADT)
                end2 = time.time()
                print ("Found word: " + perm)
                found = True
                break
        if not found:
            end2 = time.time()
            print ("Word not found. Try again.")
            
                
            #index, comparisons = word_lst.findWord(perm)
        # stop timer if no permutations are found
        #end2 = time.time()
            
        
        # Print the time it took to find a permutation of the word, the number
        # of permutations chaecked, and number of comparisons made
        print ("Solving this jumble took %2.5f seconds." % (end2 - start2))
        print ("Checked %d permutations" % (count))
        print ("Made %d comparisons" % (comparisonsMade))
        print("")
    
main()
    

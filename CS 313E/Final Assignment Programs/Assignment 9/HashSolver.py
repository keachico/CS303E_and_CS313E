#  File: HashSolver.py
#
#  Description: This program generates a list of words from a file,
#  adds them to a hashed Wordlist, generates hash keys, 
#  searches corresponding buckets in the table, and gives the 
#  statistics of each search. 
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

import string
import time
from Wordlist import *

def main():

    #create hashed wordlist ADT
    word_lst = HashedWordlist()

    print("Using hash table wordlist.")
    print("Creating wordlist \n")

    # start timer
    start = time.time()

    count = word_lst.addWordsFromFile("UnorderedWordlist.txt")
    print 

    empty_buckets, avg = word_lst.loadFactor()

    # stop timer
    end = time.time()

    print ("The Wordlist contains ",count," words.")
    print ("There are %d empty buckets" % empty_buckets)
    print ("Non-empty buckets have an average length of %3.11f" % avg)
    print ("Building the Wordlist took %2.3f seconds. \n" % (end - start))

    while True:

        # Ask user to input a word
        word = input("Enter a scrambled word (or EXIT): ")

        word = word.lower()

        # If the user types "exit", break the program
        if word == "exit":

            print ("Thanks for playing! Goodbye. \n")

            break

        # start the timer for word search. 
        start = time.time()

        # Return a Tuple of the count and a permurtation
        # if the users word is found within the data
        foundWord, count = word_lst.findPerm(word)

        if foundWord != False:
            # start timer
            end = time.time()

            print("Found word:", foundWord)

            print("Solving this jumble took %2.5f seconds" % (end - start))

            print("Made %d comparisons \n" % count)

            continue           
        # stop timer    
        end = time.time()

        print("Word not found. Try again")

        print("Search took %2.9f seconds. \n" % (end - start))
       
main()


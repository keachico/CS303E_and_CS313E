#  File: Solver.py
#
#  Description: This program generates a list of words from an external file,
#  adds them to a binary search tree Wordlist, accepts strings, generates all
#  permutations of user-given strings, checks if any permutations are in the
#  Wordlist, and gives
#  statistics of each search. 
#
#  Student's Name: Kevin Achico, Nadeem Abha
#
#  Student's UT EID: ka6893, na4333
#
#  Course Name: CS 313E 
#
#  Date Created: 12/01/12
#
#  Date Last Modified: 12/4/12

import string
import time
import sys
from Permutations import *
from Wordlist import *
from Trees import *

def TreeSort(lst):
    if lst == []:
        return []
    tree = BinarySearchTree()
    for i in lst:
        tree.insert(i)
    tree.inorder()

def main():

    print("Using binary tree wordlist.")

    # Create an instance of BinaryTreeWordlist and then start timer. 
    word_tree = BinaryTreeWordlist()
    start = time.time()
    file = open("scrambledwordslist.txt", 'r')
    count = word_tree.addWordsFromFile(file)
    end = time.time()
    # End timer. 

    # Stats how many words are put into the wordlist and how long it took to generate
    print ("The Wordlist contains",count,"words.")
    print ("Building the Wordlist took %2.3f seconds." % (end - start))

    while True:

        inputStr = input("Enter a scrambled word (or EXIT): ")
        inputStr = inputStr.lower()

        if inputStr == "exit":
            print ("Thanks for playing! Goodbye. \n")
            break

        # start the timer for word search. 
        start = time.time()
        perms = allPerms(inputStr)
        

        # Keep track of permutations checked and comparisons made.
        # Create a variable to see whether or not the word has been found. 
        count1 = 0
        count2 = 0
        word_found = 0

        # for each permutation of user's input, check if in the wordlist.
        # if so, print stats, break nested loop, and continue main loop.
        # if not found, continue loop until all permutations are checked.
        for word in perms:

            count1 += 1
            findword = word_tree.findWord(word)
            count2 += findword[1]

            if findword[0] != False:
                end = time.time()
                found_P, unique_P = howManyPerms(inputStr)

                print("Found %d permutations; %d unique permutations" % (found_P,unique_P))
                print("Found word:", word)
                print("Solving this jumble took %2.5f seconds" % (end - start))
                print("Checked %d permutations" % count1)
                print("Made %d comparisons \n" % count2)

                word_found = 1
                break           
            
        if word_found == 1:
            continue
            
        end = time.time()
        found_P, unique_P = howManyPerms(inputStr)

        print("Found %d permutations; %d unique permutations" % (found_P,unique_P))
        print("Word not found.")
        print("Search took %2.5f seconds." % (end - start))
        print("Checked %d permutations" % count1)
        print("Made %d comparisons \n" % count2)
       
main()


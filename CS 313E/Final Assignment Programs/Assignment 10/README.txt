#  Files:  Trees.py, Wordlist.py, Solver.py, README
#
#  Description: BinaryTreeWordlist (ADT) and BinaryTree(ADT)
#               generates a list of words from UnorderedWordlist.txt
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

The flat unsorted list took longer to generate than the sorted word list. The difference between the flat unsorted and the sorted word list was 12.758. 
However, the search for the users permutation of the word using a binary search tree was on average a hundredth of a second faster than then using the permutation method in flat unsorted list.

The hash table word list took more time to generate the word list compared to the flat unsorted wordlist. 
The difference between the two were 2.58511440221 seconds. 
Although, the hash table took much less of a time when compared to the sorted word list. The difference between the two were 10.17288559779 seconds. 
However, the hash table took on average about a few hundredth thousandths of a second to search for a permutation of the users word, which is quicker in respect to the flat unsorted word list and sorted word list. 
The hash table is more efficient than the recursive permutation method in the flat unsorted word list and the binary search method in the sorted word list.

The binary tree wordlist may have taken a bit longer to generate the wordlist when compared using flat unsorted wordlist.The difference between the two was .440 seconds. 
It also made many more word comparisons than the flat sorted and hash table wordlists. But the use of a binary tree wordlist did surpass the search time of flat sorted and unsorted wordlist searching.
All of the searches took less than .0100 seconds. Even though searching for a word through a binary tree is not as fast as the hash table method, binary tree wordlists are still extremely efficient when compared to flat searching. 

---------------------------------------------------------------------------

Solver.py flat


Using flat unsorted wordlist.
The Wordlist contains 22633 words.
Building the Wordlist took 0.129 seconds.

Enter a scrambled word (or EXIT): danys
Found 120 permutations; 120 unique permutations
Found word: sandy
Solving this jumble took 0.05323 seconds.
Checked 89 permutations
Made 3 comparisons

Enter a scrambled word (or EXIT): ptyna
Found 120 permutations; 120 unique permutations
Found word: panty
Solving this jumble took 0.06670 seconds.
Checked 111 permutations
Made 2 comparisons

Enter a scrambled word (or EXIT): torll
Found 120 permutations; 60 unique permutations
Found word: troll
Solving this jumble took 0.00460 seconds.
Checked 6 permutations
Made 8272 comparisons

Enter a scrambled word (or EXIT): nadeem
Found 720 permutations; 360 unique permutations
Found word: demean
Solving this jumble took 0.09560 seconds.
Checked 150 permutations
Made 2086 comparisons

Enter a scrambled word (or EXIT): zhepyr
Found 720 permutations; 720 unique permutations
Found word: zephyr
Solving this jumble took 0.00768 seconds.
Checked 13 permutations
Made 82 comparisons

Enter a scrambled word (or EXIT): denrt
Found 120 permutations; 120 unique permutations
Found word: trend
Solving this jumble took 0.06992 seconds.
Checked 115 permutations
Made 809 comparisons

Enter a scrambled word (or EXIT): gewhit
Found 720 permutations; 720 unique permutations
Found word: weight
Solving this jumble took 0.08486 seconds.
Checked 130 permutations
Made 14908 comparisons

Enter a scrambled word (or EXIT): valely
Found 720 permutations; 360 unique permutations
Found word: valley
Solving this jumble took 0.05948 seconds.
Checked 91 permutations
Made 11802 comparisons

Enter a scrambled word (or EXIT): valley
Found 720 permutations; 360 unique permutations
Found word: valley
Solving this jumble took 0.00184 seconds.
Checked 1 permutations
Made 11802 comparisons

Enter a scrambled word (or EXIT): kevin
Found 120 permutations; 120 unique permutations
Word not found. Try again.
Solving this jumble took 0.07257 seconds.
Checked 120 permutations
Made 0 comparisons

Enter a scrambled word (or EXIT): exit
Thanks for playing! Goodbye.

----------------------------------------------------------------------
Solver.py sort


Using sorted wordlist.
The Wordlist contains 22633 words.
Building the Wordlist took 12.887 seconds.

Enter a scrambled word (or EXIT): danys
Found 120 permutations; 120 unique permutations
Found word: sandy
Solving this jumble took 0.06512 seconds.
Checked 89 permutations
Made 14 comparisons

Enter a scrambled word (or EXIT): ptyna
Found 120 permutations; 120 unique permutations
Found word: panty
Solving this jumble took 0.08073 seconds.
Checked 111 permutations
Made 14 comparisons

Enter a scrambled word (or EXIT): torll
Found 120 permutations; 60 unique permutations
Found word: troll
Solving this jumble took 0.00513 seconds.
Checked 6 permutations
Made 14 comparisons

Enter a scrambled word (or EXIT): nadeem
Found 720 permutations; 360 unique permutations
Found word: demean
Solving this jumble took 0.12017 seconds.
Checked 150 permutations
Made 13 comparisons

Enter a scrambled word (or EXIT): zehrpy
Found 720 permutations; 720 unique permutations
Found word: zephyr
Solving this jumble took 0.21511 seconds.
Checked 271 permutations
Made 11 comparisons

Enter a scrambled word (or EXIT): denrt
Found 120 permutations; 120 unique permutations
Found word: trend
Solving this jumble took 0.08411 seconds.
Checked 115 permutations
Made 14 comparisons

Enter a scrambled word (or EXIT): gewhit
Found 720 permutations; 720 unique permutations
Found word: weight
Solving this jumble took 0.10272 seconds.
Checked 130 permutations
Made 14 comparisons

Enter a scrambled word (or EXIT): valely
Found 720 permutations; 360 unique permutations
Found word: valley
Solving this jumble took 0.07087 seconds.
Checked 91 permutations
Made 10 comparisons

Enter a scrambled word (or EXIT): valley
Found 720 permutations; 360 unique permutations
Found word: valley
Solving this jumble took 0.00149 seconds.
Checked 1 permutations
Made 10 comparisons

Enter a scrambled word (or EXIT): kevin
Found 120 permutations; 120 unique permutations
Word not found. Try again.
Solving this jumble took 0.08776 seconds.
Checked 120 permutations
Made 0 comparisons

Enter a scrambled word (or EXIT): exit
Thanks for playing! Goodbye.

--------------------------------------------------------------------------

HashSolver.py

Using hash table wordlist.
Creating wordlist 

The Wordlist contains  22633  words.
There are 1668 empty buckets
Non-empty buckets have an average length of 2.71411440221
Building the Wordlist took 0.234 seconds. 

Enter a scrambled word (or EXIT): danys
Found word: sandy
Solving this jumble took 0.00003 seconds
Made 1 comparisons 

Enter a scrambled word (or EXIT): ptyna
Found word: panty
Solving this jumble took 0.00003 seconds
Made 1 comparisons 

Enter a scrambled word (or EXIT): torll
Found word: troll
Solving this jumble took 0.00004 seconds
Made 3 comparisons 

Enter a scrambled word (or EXIT): nadeem
Found word: demean
Solving this jumble took 0.00004 seconds
Made 2 comparisons 

Enter a scrambled word (or EXIT): zehrpy
Found word: zephyr
Solving this jumble took 0.00003 seconds
Made 1 comparisons 

Enter a scrambled word (or EXIT): denrt
Found word: trend
Solving this jumble took 0.00003 seconds
Made 1 comparisons 

Enter a scrambled word (or EXIT): gewhit
Found word: weight
Solving this jumble took 0.00005 seconds
Made 4 comparisons 

Enter a scrambled word (or EXIT): valely
Found word: valley
Solving this jumble took 0.00003 seconds
Made 1 comparisons 

Enter a scrambled word (or EXIT): valley
Found word: valley
Solving this jumble took 0.00003 seconds
Made 1 comparisons 

Enter a scrambled word (or EXIT): kevin
Word not found. Try again
Search took 0.00003 seconds. 

Enter a scrambled word (or EXIT): exit
Thanks for playing! Goodbye. 


--------------------------------------------------------------------------

Solver.py using BinaryTreeWordlist

Using binary tree wordlist.
The Wordlist contains 22633 words.
Building the Wordlist took 0.569 seconds.


Enter a scrambled word (or EXIT): danys
Found 120 permutations; 120 unique permutations
Found word: sandy
Solving this jumble took 0.00500 seconds
Checked 89 permutations
Made 1649 comparisons 

Enter a scrambled word (or EXIT): ptyna
Found 120 permutations; 120 unique permutations
Found word: panty
Solving this jumble took 0.00600 seconds
Checked 111 permutations
Made 2001 comparisons 

Enter a scrambled word (or EXIT): torll
Found 120 permutations; 60 unique permutations
Found word: troll
Solving this jumble took 0.00100 seconds
Checked 6 permutations
Made 124 comparisons 

Enter a scrambled word (or EXIT): nadeem
Found 720 permutations; 360 unique permutations
Found word: demean
Solving this jumble took 0.00800 seconds
Checked 150 permutations
Made 3063 comparisons 

Enter a scrambled word (or EXIT): zhepyr
Found 720 permutations; 720 unique permutations
Found word: zephyr
Solving this jumble took 0.00100 seconds
Checked 13 permutations
Made 282 comparisons 

Enter a scrambled word (or EXIT): denrt
Found 120 permutations; 120 unique permutations
Found word: trend
Solving this jumble took 0.00700 seconds
Checked 115 permutations
Made 2270 comparisons 

Enter a scrambled word (or EXIT): gewhit
Found 720 permutations; 720 unique permutations
Found word: weight
Solving this jumble took 0.00900 seconds
Checked 130 permutations
Made 3346 comparisons 

Enter a scrambled word (or EXIT): valely
Found 720 permutations; 360 unique permutations
Found word: valley
Solving this jumble took 0.00500 seconds
Checked 91 permutations
Made 1816 comparisons 

Enter a scrambled word (or EXIT): valley
Found 720 permutations; 360 unique permutations
Found word: valley
Solving this jumble took 0.00000 seconds
Checked 1 permutations
Made 15 comparisons 

Enter a scrambled word (or EXIT): kevin
Found 120 permutations; 120 unique permutations
Word not found.
Search took 0.00700 seconds.
Checked 120 permutations
Made 2610 comparisons 

Enter a scrambled word (or EXIT): exit
Thanks for playing! Goodbye. 

# File: DNA.py
# Description: Prompts user for 2 strands of DNA and returns all common subsequences one line at a time.
# Assignment Number: 8 
#
# Name 1: Kevin Achico
# EID 1: ka6893
# Name 2: Maria Aviles
# EID 2: mea922
#
#
# Course Name: CS303E
#
# Unique Number 1: 52770
# Unique Number 2:  52760
#
# Date created: April 6, 2012
# Date last modified: April 10, 2012
#
# Slip days used this assignment: 0
# Total slip days used for ka6893: 0
# Total slip days used for mea922: 1

#Partner Log:
#4-6, 10:00 - 12:00 Kevin, 2 hours
#4-6, 10:30 - 11:30, Maria, 1 hour
#4-7,  5:00- 7:30, Kevin and Maria, 2 hours and 30 minutes
#4-8, 8:00- 11:00 Kevin and Maria, 3 hours
#4-9, 9:00-12:00 Kevin and Maria, 3 hours
#4-10, 5:00-10:50, Kevin and Maria 5 hours, 50 minutes 
#total time 17 hours and 20 minutes, 14 hours of pair programming

#Kevin is driving.
import string

def main():
    x = raw_input("Please enter a strand of DNA: ")
    y = raw_input("Please enter another strand of DNA: ")
    printCommonSubseqs(x,y,(longestCommonSubseq(x,y)))
    while (x and y != ''):
        x,y = getStrands()
        longestCommonSubseq(x,y)
        printCommonSubseqs(x,y,(longestCommonSubseq(x,y)))


#Maria is driving now.
def getStrands():
    strand1 = raw_input("Pleease enter a strand of DNA: ")
    strand2 = raw_input("Please enter another strand of DNA: ")
    return strand1, strand2
   


#Kevin is now driving.
def longestCommonSubseq(stnd1, stnd2):
    longestStrand = 0
    s1 = string.upper(stnd1) #convert both strands to uppercase
    s2 = string.upper(stnd2)
    for i in range(len(s1)):
        for j in range(len(s1)):#nested loop used to test every case of strand combinations
            st = s1[i:len(s1)-j] #string splicing used in order to break down the strand
            #print st
            if len(st) > 1: #condition used to check all combos of 2 letters or more
                if st in s2: #checks if the spliced string is in string2
                    if (len(st) > longestStrand): #checks for the longest length of common subsequence
                        longestStrand = len(st)
    return longestStrand
                    




#Maria driving now
def printCommonSubseqs(stnd1, stnd2, length):
    while (stnd1 and stnd2 != ''): #program exits program if user enters empty strings
        if length > 0:
            s1 = string.upper(stnd1)
            s2 = string.upper(stnd2)
            print "Common subsequence(s): "
            #Kevin driving now
            for i in range(len(stnd1)):
                st = s1[i:length+i] #splice with i as beginning of string and length + i as the end
                if len(st) == length: #the length of the string must match the length of the given length
                    if st in s2:
                        print st
            print
            return

        #Maria driving now
        else:
            print "No common subsequence was found for " + stnd1 + " and " + stnd2
            print
            return
        
main()

##TEST CASES:
##
##1.
##Please enter a strand of DNA: ATCGAGTCAGACT
##Please enter another strand of DNA: GATCACAT
##Common subsequence(s): 
##ATC
##TCA
##
##2.
##Pleease enter a strand of DNA: AAGGCCTTAACCAAGG
##Please enter another strand of DNA: GGCCTTAAGGAA
##Common subsequence(s): 
##GGCCTTAA
##
##3.
##Pleease enter a strand of DNA: AACCGGTT
##Please enter another strand of DNA: TTGGCCAA
##Common subsequence(s): 
##AA
##CC
##GG
##TT
##
##4.
##Pleease enter a strand of DNA: ATAGAC
##Please enter another strand of DNA: GCGTGCGT
##No common subsequence was found for ATAGAC and GCGTGCGT
##
##5.
##Pleease enter a strand of DNA: 
##Please enter another strand of DNA:


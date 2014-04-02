# File: Goldbach.py
# Description: Program that verifies Goldbach's conjucture in the range of 4 to a number entered by the user.
# Assignment Number: 7
#
# Name: Kevin Achico
# EID: ka6893
# Course Name: CS303E
#
# Unique Number: 52770
#
# Date created: March 27, 2012
# Date last modified: March 29, 2012
#
# Slip days used this assignment: 0
# Total slip days used: 0


import string
import sys

def main():
    print "This program will verify Goldbach's Conjecture from 4 to a number of your choosing."

    
    numRange = input("What should the top end of the range be? ")

    for i in range(4, numRange + 1, 2): #prints out every even number from 4 to the number entered by the user and also the prime numbers up to the input
        sys.stdout.write(str(i) + " = ")
        sys.stdout.write(findPrimeAddends(i))


def findPrimeAddends(k): #a function that finds the prime numbers within the range of 2 to the user input
    allPrimes = ""
    for i in range(2,k):
        truth = isPrime(i)
        if truth == True:
            allPrimes = allPrimes + str(i) + " "
    print allPrimes
    
def isPrime(x): #a function which decides whether a number is prime or not.
    if (x == 2 or x == 3 or x == 5 or x == 7):
        return True
    elif x % 2 == 0:
        return False
    elif x % 3 == 0:
        return False
    elif x % 5 == 0:
        return False
    elif x % 7 == 0:
        return False
    else:
        return True
main()


##TEST CASES
##
##Test Case 1:
##
##This program will verify Goldbach's Conjecture from 4 to a number of your choosing.
##What should the top end of the range be? 10
##4 = 2 3 
##6 = 2 3 5 
##8 = 2 3 5 7 
##10 = 2 3 5 7
##
##Test Case 2:
##
##This program will verify Goldbach's Conjecture from 4 to a number of your choosing.
##What should the top end of the range be? 20
##4 = 2 3 
##6 = 2 3 5 
##8 = 2 3 5 7 
##10 = 2 3 5 7 
##12 = 2 3 5 7 11 
##14 = 2 3 5 7 11 13 
##16 = 2 3 5 7 11 13 
##18 = 2 3 5 7 11 13 17 
##20 = 2 3 5 7 11 13 17 19 
##
##Test Case 3:
##
##This program will verify Goldbach's Conjecture from 4 to a number of your choosing.
##What should the top end of the range be? 15
##4 = 2 3 
##6 = 2 3 5 
##8 = 2 3 5 7 
##10 = 2 3 5 7 
##12 = 2 3 5 7 11 
##14 = 2 3 5 7 11 13 
##
##Test Case 4:
##
##This program will verify Goldbach's Conjecture from 4 to a number of your choosing.
##What should the top end of the range be? 30
##4 = 2 3 
##6 = 2 3 5 
##8 = 2 3 5 7 
##10 = 2 3 5 7 
##12 = 2 3 5 7 11 
##14 = 2 3 5 7 11 13 
##16 = 2 3 5 7 11 13 
##18 = 2 3 5 7 11 13 17 
##20 = 2 3 5 7 11 13 17 19 
##22 = 2 3 5 7 11 13 17 19 
##24 = 2 3 5 7 11 13 17 19 23 
##26 = 2 3 5 7 11 13 17 19 23 
##28 = 2 3 5 7 11 13 17 19 23 
##30 = 2 3 5 7 11 13 17 19 23 29 
##
##Test Case 5:
##
##This program will verify Goldbach's Conjecture from 4 to a number of your choosing.
##What should the top end of the range be? -1

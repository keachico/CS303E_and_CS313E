#  Files: Assignment7.py
#
#  Description: Generate a list of 200 random numbers and them sort them in order. 
#
#  Students' Name: Kevin Achico
#
#  Students' UT EID: ka6893
#
#  Course Name: CS 313E 
#
#  Date Created: November 3, 2012
#
#  Date Last Modified: November 6, 2012

import random

def main():
   # This will generate a list of 200 numbers randomly generated
   # in the range 0..999.
   input = [ random.randint(0, 999) for i in range(200) ]

   # You have to write the printList function to print the list, k = 20
   # numbers per line.
   print ("The input list is: ")
   printList(input, 20)

   # This is the function that actually sorts the list, using k = 3
   # rounds 
   output = radixSort(input, 3)

   # Print the sorted result.
   print ("\nThe sorted list is: ")
   printList(output, 20)


def printList(input, k): #function that prints out the unsorted and sorted list
    count = 0
    
    for num in input: #iterate through the list of numbers
        count += 1
        if count % k != 0:
           
           if len(str(num)) == 1: #case for 1 digit numbers
              print("%3d"%(num), end= " ") #prints the number on the same line in a nice fashion
                 
           elif len(str(num)) == 2: #case for 2 digit numbers
              print("%3d"%(num), end = " ") #prints the number on the same line in a nice fashion
              
           else:
              print(num, end= " ")
              
        elif count % k == 0 and count != 200: #for every k_th entry, print num on a new line
            print(num)
            
        elif count == 200:
            print(num)


def radixSort(input, passes):

    matrix1 = [ [], [], [], [], [], [], [], [], [], [] ] 

    for num in input: #iterate through unsorted list
        newNum = str(num) #convert num to a string
        matrix1[int(newNum[-1])].append(num) #index last character and append that to the last character bin

    
    matrix2 = [ [], [], [], [], [], [], [], [], [], [] ]
    
    for lst in matrix1: #iterate through the list of lists in matrix1
        for num in lst: 
            newNum = str(num)
            if len(newNum) == 1: #case when num is 1 digit
                    matrix2[0].append(num)
            else:
                    matrix2[int(newNum[-2])].append(num) #append to the 2nd to last character list. 
                    
    matrix3 = [ [], [], [], [], [], [], [], [], [], [] ]
    
    for lst in matrix2:
        for num in lst:
            newNum = str(num)
            if len(newNum) == 1:
                    matrix3[0].append(num)
            elif len(newNum) == 2:
                    matrix3[0].append(num)
            else:
                    matrix3[int(newNum[-3])].append(num)

    sorted_list = []
    for lst in matrix3:
       for num in lst:
          sorted_list.append(num)


    #Code for specific number of passes if user chooses 3 or less passes.
    #If user enters 1 for passes, only prints out lists from round 0.
    #If user enters 2 for passes, only prints out lists from round 0 and 1. 
    #If user enters 2 for passes, only prints out lists from round 0, 1, and 2. 
          
    if passes == 1:
       print(" ")
       print('After round 0:')
       count = 0
       
       for lst in matrix1: 
           str1 = ""  
           for num in lst:
             str1 += str(num) +" "
           print(str(count) + " : [ " + str1 + " ]") #print out the string full of entries from matrix1
           count += 1   
       print ('')
              
    elif passes == 2:
       print(" ")
       print('After round 0:')
       count = 0
       
       for lst in matrix1:
           str1 = ""  
           for num in lst:
             str1 += str(num) +" "
           print(str(count) + " : [ " + str1 + " ]")
           count += 1
           
       print ('')
       print('After round 1:')
       count = 0
       
       for lst in matrix2:
           str1 = ""  
           for num in lst:
             str1 += str(num) +" "
           print(str(count) + " : [ " + str1 + " ]")
           count += 1
           
       print('')


    else:
       print(" ")
       print('After round 0:')
       count = 0
       
       for lst in matrix1:
           str1 = ""  
           for num in lst:
             str1 += str(num) +" "
           print(str(count) + " : [ " + str1 + " ]")
           count += 1
           
       print ('')
       print('After round 1:')
       count = 0
       
       for lst in matrix2:
           str1 = ""  
           for num in lst:
             str1 += str(num) +" "
           print(str(count) + " : [ " + str1 + " ]")
           count += 1

       print ('')
       print('After round 2:')
       count = 0
       
       for lst in matrix3:
           str1 = ""  
           for num in lst:
             str1 += str(num) +" "
           print(str(count) + " : [ " + str1 + " ]")
           count += 1

    return (sorted_list)
     
main()

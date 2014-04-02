# File: ISBN.py
# Description: Validates whether a series of characters counts as an ISBN.
# Assignment Number: 10
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
# Date created: April 21, 2012
# Date last modified: April 27, 2012
#
# Slip days used this assignment: 3
# Total slip days used for ka6893: 3
# Total slip days used for mea922: 4

#Schedule: 
#4-21, 8:00-9:30, Maria, 1hour, 30 minutes
#4-22, 4:00-5:30, Kevin, 1 hour, 30 minutes
#4-23, 5:00-8:00, Kevin and Maria, 3 hours
#4-25, 9:00-12:00, Kevin and Maria, 3 hours
#4-26, 9:00-12:30, Kevin and Maria, 3 hours, 30 minutes
#4-27, 12:00-1:00, Kevin and Maria, 1 hour 
#Total Time 13 hours and 30 minutes, 10 hours and 30 minutes Pair Programming

import string

def main():

    write_isbnValid(getData('isbn.txt'))
    print
    print '5 Test Cases:'
    testCases()


def getData(fileName):
    myFile = open(fileName, 'r')

    total = []
    for line in myFile:
        remove_space = string.find(line, '\n')
        
        if remove_space != -1: #disregards the \n in the txt file
            line = line[0:-1]

        wholeLine = line + ' ' + str(getWeightedsums(checkValidity(removeHyphens(line))))
        total.append(wholeLine)
        #print line + ' ' + str(getWeightedsums(checkValidity(removeHyphens(line))))
    return total


def removeHyphens(line):

    newLine = ''
    for ch in line:
        if ch != '-':
            newLine = newLine + ch #creates a new string while skipping all the -'s 
    return newLine



def checkValidity(newLine):
    chars = '0123456789xX'

    if string.find(chars, newLine[-1]) == -1: #checks if the last character is not a digit from 0 to 9, 'x' or 'X'
        return 0


    for ch in newLine[0:len(newLine)-1]: #checks if there is an 'x' or 'X' before the last character
        if ch == 'x':
            #return 'INVALID "x" before the last character', ch
            return 0
        if ch == 'X':
            #return 'INVALID "X" before the last character', ch
            return 0

    
    if (len(newLine)-1) != 9: #checks if there is exactly 9 digits before the last character
        #return 'NOT EQUAL TO 9 characters'
        return 0

        
    for ch in newLine: #checks if there are characters other than the digits 0 to 9, 'x' or 'X'
        if string.find(chars, ch) == -1:
            #return 'invalid character', ch
            return 0

    else:
        return newLine
        
    
    
def getWeightedsums(line):
    if line == 0:
        #print 'invalid' #if the line does not pass the checkValidity function, then it is already invalid
        return 'invalid'
    
    if line[-1] == 'x': #checks the case of when x is the last character in the line
        sum1 = [0]*10
        sum1_total = 0
        for i in range(len(line)-1):
            sum1_total = int(line[i]) + sum1_total
            sum1[i] = sum1_total
            sum1[-1] = sum1[-2] + 10 #replaces the last element in the list to the second to last element plus 10

        sum2 = [0] * 10
        sum2_total = 0
        for i in range(len(sum1)):
            sum2_total = int(sum1[i]) + sum2_total
            sum2[i] = sum2_total

        if sum2[9] % 11 == 0:
            
            return 'valid'
            
        else:
            
            return 'invalid'

    elif line[-1] == 'X': #checks the case of when X is the last character in the line
        sum1 = [0]*10
        sum1_total = 0
        for i in range(len(line)-1):
            sum1_total = int(line[i]) + sum1_total
            sum1[i] = sum1_total
            sum1[-1] = sum1[-2] + 10 #replaces the last element in the list to the second to last element plus 10

        sum2 = [0] * 10
        sum2_total = 0
        for i in range(len(sum1)):
            sum2_total = int(sum1[i]) + sum2_total
            sum2[i] = sum2_total

        if sum2[9] % 11 == 0:
            
            return 'valid'
        else:
            
            return 'invalid'

    else:
        sum1 = [0]*10
        sum1_total = 0
        for i in range(len(line)):
            sum1_total = int(line[i]) + sum1_total
            sum1[i] = sum1_total

        sum2 = [0] * 10
        sum2_total = 0
        for i in range(len(sum1)):
            sum2_total = int(sum1[i]) + sum2_total
            sum2[i] = sum2_total

        if sum2[9] % 11 == 0:
            
            return 'valid'
        else:
            
            return 'invalid'     


def testCases():
    isbn = ['0-3161-26691-', '031-60!686-3', '031-6056-86?', '023-74-2756-37', '0-37x27-563-7']

    for line in isbn:
        print line + ' ' + str(getWeightedsums(checkValidity(removeHyphens(line))))


def write_isbnValid(data):

    outFile = open("isbnValid.txt", "a")

    for line in data:
        outFile.write(str(line)+'\n')
    outFile.write('\n')

    outFile.close()

main()




##TEST CASES:


##5 Test Cases:
##0-3161-26691- valid
##031-60!686-3 invalid
##031-6056-86? invalid
##023-74-2756-37 invalid
##0-37x27-563-7 invalid

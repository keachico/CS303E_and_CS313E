
import string

def main():

    getData('cases_assignment10.txt')
    print
    print '5 Test Cases:'
    testCases()


def getData(fileName):
    myFile = open(fileName, 'r')
    
    for line in myFile:
        remove_space = string.find(line, '\n')
        
        if remove_space != -1:
            line = line[0:-1]
        
        print line,
        getWeightedsums(checkValidity(removeHyphens(line)))


def removeHyphens(line):

    newLine = ''
    for ch in line:
        if ch != '-':
            newLine = newLine + ch
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
        print 'invalid'
        return
    
    if line[-1] == 'x':
        sum1 = [0]*10
        sum1_total = 0
        for i in range(len(line)-1):
            sum1_total = int(line[i]) + sum1_total
            sum1[i] = sum1_total
            sum1[-1] = sum1[-2] + 10
        #print str(sum1)

        sum2 = [0] * 10
        sum2_total = 0
        for i in range(len(sum1)):
            sum2_total = int(sum1[i]) + sum2_total
            sum2[i] = sum2_total
        #print sum2

        if sum2[9] % 11 == 0:
            print 'valid'
        else:
            print 'invalid'

    elif line[-1] == 'X':
        sum1 = [0]*10
        sum1_total = 0
        for i in range(len(line)-1):
            sum1_total = int(line[i]) + sum1_total
            sum1[i] = sum1_total
            sum1[-1] = sum1[-2] + 10
        #print str(sum1)

        sum2 = [0] * 10
        sum2_total = 0
        for i in range(len(sum1)):
            sum2_total = int(sum1[i]) + sum2_total
            sum2[i] = sum2_total
        #print sum2

        if sum2[9] % 11 == 0:
            print 'valid'
        else:
            print 'invalid'

    else:
        sum1 = [0]*10
        sum1_total = 0
        for i in range(len(line)):
            sum1_total = int(line[i]) + sum1_total
            sum1[i] = sum1_total
        #print str(sum1)

        sum2 = [0] * 10
        sum2_total = 0
        for i in range(len(sum1)):
            sum2_total = int(sum1[i]) + sum2_total
            sum2[i] = sum2_total
        #print sum2

        if sum2[9] % 11 == 0:
            print 'valid'
        else:
            print 'invalid'     

def testCases():
    isbn = ['0316126691', '03160!6863', '031605686?', '02374275637', '037x275637']
    isbn2 = '03160!6863'
    isbn3 = '031605686?'
    isbn4 = '02374275637'
    isbn5 = '037x275637'

    for line in isbn:
        print line,
        getWeightedsums(checkValidity(removeHyphens(line)))

    
main()

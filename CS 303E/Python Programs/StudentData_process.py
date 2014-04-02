import string
def main():
    #print getLeadDigitCounts(getData('TexasCountyPop2010.txt'))
    print getLeadDigitCounts(getData('fuckthis.txt'))

def getData(fileName):
    myFile = open(fileName, 'r')
    total = []
    for line in myFile:
        total.append(line)
    return total


def getLeadDigitCounts(data):
    counts = [0]*9
    for line in data:
        if line != '\n':
            newLine = string.split(line, '\t')
            if newLine[1][0] == ' ':
                number = newLine[1]
                newNumber = number[1:len(number)]
                newLine[1] = newNumber
                print newLine[0],'\t',newLine[1]
            #print newLine
##        firstNumber = int(newLine[1][0])
##        print newLine[0], firstNumber
##        counts[firstNumber - 1] = counts[firstNumber - 1] + 1
    #return counts

main()

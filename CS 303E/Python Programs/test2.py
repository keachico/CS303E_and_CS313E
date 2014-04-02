import string
def main():
    printData(getData('isbn.txt'))

    


def getData(fileName):
    myFile = open(fileName, 'r')
    total = []
    for line in myFile:
        remove_space = string.find(line, '\n')
        if remove_space != -1:
            line = line[0:-1]
        total.append(line)
    return total

def printData(line):
    for i in line:
        print i
main()

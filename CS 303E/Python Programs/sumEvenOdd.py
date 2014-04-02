def main():
    number = input("Enter a number: ")
    sumEven = 0
    sumOdd = 0
    
    while (number != -1):
        if (number % 2 == 0):
            sumEven = number + sumEven
        else:
            sumOdd = number + sumOdd
        number = input("Enter a number: ")

    print "The sum of even numbers is %d" % sumEven
    print "The sum of odd numbers is %d" % sumOdd
    
main()

def main():
    value = input('Enter a value or -111 to quit: ')
    min1 = value
    max1 = value

    while (value != -111):
        if (value < min1):
            min1 = value
        elif (value > max1):
            max1 = value
        value = input('Enter a value or -111 to quit: ')

    print 'The max was %d and the min was %d' % (max1, min1)

main()

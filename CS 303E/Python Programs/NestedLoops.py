##def main():
##    sum1 = 0
##    for i in range(5):
##        for j in range(9):
##            sum1 = sum1 + 1
##    print sum1

##def main():
##    for i in range(10):
##        triangle_row = "*"
##        while i > 0:
##            triangle_row = triangle_row + "*"
##            i = i-1
##
##    print triangle_row

def main():
    for i in range(10):
        triangle_row = ""
        while i >= 0:
            triangle_row = triangle_row + str(i)
            i = i-1

        print triangle_row

main()

# File: EasterSunday.py
# Description: This program asks the user to input a year and then prints the date of Easter Sunday of that year.
# Assignment: 2
#
# Student Name: Kevin Achico
# EID: ka6893
# Course Name: CS 303E
#
# Unique Number: 52770
#
# Date Created: February 1, 2012
# Date Last Modified: February 7, 2012
#
# Slip days used this assignment: 0
# Total slip days used: 0

def main():
    y = input("Enter year:")

    a = y % 19
    b = y / 100
    c = y % 100
    d = b / 4
    e = b % 4
    g = (8 * b + 13) / 25
    h = (19 * a + b - d - g + 15) % 30
    j = c / 4
    k = c % 4
    m = (a + 11 * h) / 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) / 25
    p = (h - m + r + n + 19) % 32
    # n will signify the month
    # p will signify the day
    

    if(y > 2011):
        #put output statement here
        print "Easter Sunday will be on %d/%d/%d" % (n,p,y)#, n, "/", p, "/", y
    else:
        #put output statement here
        print "Easter Sunday was on %d/%d/%d" % (n,p,y)#, n, "/", p, "/", y
        
main()
#test case 1 (past year)
#Enter year:1983
#Easter Sunday was on 4 / 3 / 1983

#test case 2 (future year)
#Enter year:2024
#Easter Sunday will be on 3 / 31 / 2024

#test case 3 (current year)
#Enter year:2012
#Easter Sunday will be on 4 / 8 / 2012

#test case 4 (Easter falling in April)
#Enter year:2014
#Easter Sunday will be on 4 / 20 / 2014

#test case 5 (Easter falling in March)
#Enter year:1997
#Easter Sunday was on 3 / 30 / 1997

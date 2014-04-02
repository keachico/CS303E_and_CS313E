# File: Benford.py
# Description: Given a real world data set, this program proves Benford's Law.
# Assignment Number: 9 
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
# Date created: April 14, 2012
# Date last modified: April 17, 2012
#
# Slip days used this assignment: 0
# Total slip days used for ka6893: 0
# Total slip days used for mea922: 1

#Partner Log:
#4-14, 9:00 - 11:00 Kevin and Maria 2 hours
#4-15, 8:00 - 11:00, Kevin, 3 hours
#4-15,  7:00- 9:00, Maria, 2 hours
#4-16, 6:00- 10:00 Kevin and Maria,4 hours
#4-17, 1:00 - 5:00 Kevin and Maria, 4 hours
# total time 15 hours, 10 hours of pair programming

#Kevin is driving now.

import string

def main():

    print "Data for the 2012 Texas County Population."
    print
    processFile('TexasCountyPop2010.txt')
    print
    print "Data for top 298 largest cities in the USA."
    print
    processFile('StudentData.txt')



def processFile(name):
    showResults(getLeadDigitCounts(getData(name)))
    print
    digit = input("Enter leading digit: ")
    print
    showLeadingDigits(digit, getData(name))
    
#Maria is now driving.
    
def getData(fileName):
    myFile = open(fileName, 'r')
    total = []
    for line in myFile:
        total.append(line)
    return total


def getLeadDigitCounts(data):
    counts = [0]*9 #list consisting of 9 spots in accordance to the 9 beginning integers
    for line in data:
        newLine = string.split(line, '\t') #split each object that's seperated by the tab function, '\t'
        firstNumber = int(newLine[1][0]) #check the first character (which is a number) of the second object in the newLine
        counts[firstNumber - 1] = counts[firstNumber - 1] + 1 #add one count everytime the firstNumber is encountered
    return counts

#Kevin is driving.
#this segment of code took both of us a while to solve.

def showResults(counts):
    totalDatapts = 0.0
    for i in range(len(counts)):
        totalDatapts = totalDatapts + counts[i - 1] #calculates the total number of data points

    print 'number of data points: ', totalDatapts
    print
    print 'digit\tnumber\tpercentage'
    for i in range(len(counts)):
        percent = (counts[i]/totalDatapts)*100
        print i+1, '\t', counts[i], '\t %.1f' % percent #prints out the data table according to the assignment page


def showLeadingDigits(digit, data):
    print 'Showing data with a leading', digit
    print
    for line in data:
        newLine = string.split(line, '\t') #splits each line into a list of objects
        firstNumber = int(newLine[1][0]) #firstNumber is the leading number of the second object in the list
        if digit == int(newLine[1][0]): #if the number that was prompted by the user matches the firstNumber, print the line
            print newLine[0], newLine[1]
    

main()





##Test Cases:
##
##Test Case 1
##
##Data for the 2012 Texas County Population.
##
##number of data points:  254.0
##
##digit	number	percentage
##1 	80 	 31.5
##2 	38 	 15.0
##3 	41 	 16.1
##4 	26 	 10.2
##5 	15 	 5.9
##6 	15 	 5.9
##7 	17 	 6.7
##8 	13 	 5.1
##9 	9 	 3.5
##
##Enter leading digit: 9
##
##Showing data with a leading 9
##
##Archer County  9054
##
##Bowie County  92565
##
##Brewster County  9232
##
##Dimmit County  9996
##
##Jack County  9044
##
##Mitchell County  9403
##
##Roberts County  929
##
##Stephens County  9630
##
##Terrell County  984
##
##
##Data for top 298 largest cities in the USA.
##
##number of data points:  298.0
##
##digit	number	percentage
##1 	154 	 51.7
##2 	36 	 12.1
##3 	17 	 5.7
##4 	11 	 3.7
##5 	13 	 4.4
##6 	3 	 1.0
##7 	4 	 1.3
##8 	13 	 4.4
##9 	47 	 15.8
##
##Enter leading digit: 3
##
##Showing data with a leading 3
##
##Los Angeles  3,798,981
##
##Omaha  399,357
##
##Tulsa  391,908
##
##Honolulu CDP  378,155
##
##Minneapolis  375,635
##
##Miami  374,791
##
##Colorado Springs  371,182
##
##Wichita  355,126
##
##Arlington  349,944
##
##Santa Ana  343,413
##
##St. Louis  338,353
##
##Anaheim  332,642
##
##Pittsburgh  327,898
##
##Cincinnati  323,885
##
##Tampa  315,140
##
##Toledo  309,106
##
##Raleigh  306,944
##
##
##
##Test Case 2
##
##Data for the 2012 Texas County Population.
##
##number of data points:  254.0
##
##digit	number	percentage
##1 	80 	 31.5
##2 	38 	 15.0
##3 	41 	 16.1
##4 	26 	 10.2
##5 	15 	 5.9
##6 	15 	 5.9
##7 	17 	 6.7
##8 	13 	 5.1
##9 	9 	 3.5
##
##Enter leading digit: 5
##
##Showing data with a leading 5
##
##Anderson County  58458
##
##Cherokee County  50845
##
##Delta County  5231
##
##Fort Bend County  585375
##
##Hansford County  5613
##
##Hardin County  54635
##
##Haskell County  5899
##
##Hood County  51182
##
##Jim Hogg County  5300
##
##Lynn County  5915
##
##Maverick County  54258
##
##Rusk County  53330
##
##Van Zandt County  52579
##
##Wheeler County  5410
##
##Wise County  59127
##
##
##Data for top 298 largest cities in the USA.
##
##number of data points:  298.0
##
##digit	number	percentage
##1 	154 	 51.7
##2 	36 	 12.1
##3 	17 	 5.7
##4 	11 	 3.7
##5 	13 	 4.4
##6 	3 	 1.0
##7 	4 	 1.3
##8 	13 	 4.4
##9 	47 	 15.8
##
##Enter leading digit: 5
##
##Showing data with a leading 5
##
##Milwaukee  590,895
##
##Boston  589,281
##
##Charlotte  580,597
##
##El Paso  577,415
##
##Washington  570,898
##
##Nashville-Davidson  570,785
##
##Seattle  570,426
##
##Fort Worth  567,516
##
##Denver  560,415
##
##Portland  539,438
##
##Oklahoma  519,034
##
##Las Vegas  508,604
##
##Tucson  503,151
##
##
##
##Test Case 3
##
##Data for the 2012 Texas County Population.
##
##number of data points:  254.0
##
##digit	number	percentage
##1 	80 	 31.5
##2 	38 	 15.0
##3 	41 	 16.1
##4 	26 	 10.2
##5 	15 	 5.9
##6 	15 	 5.9
##7 	17 	 6.7
##8 	13 	 5.1
##9 	9 	 3.5
##
##Enter leading digit: 7
##
##Showing data with a leading 7
##
##Bailey County  7165
##
##Bastrop County  74171
##
##Brooks County  7223
##
##Childress County  7041
##
##Collin County  782341
##
##Coryell County  75388
##
##Goliad County  7210
##
##Henderson County  78532
##
##Hidalgo County  774769
##
##Liberty County  75643
##
##McMullen County  707
##
##Presidio County  7818
##
##Refugio County  7383
##
##Rockwall County  78337
##
##Swisher County  7854
##
##Winkler County  7110
##
##Yoakum County  7879
##
##
##Data for top 298 largest cities in the USA.
##
##number of data points:  298.0
##
##digit	number	percentage
##1 	154 	 51.7
##2 	36 	 12.1
##3 	17 	 5.7
##4 	11 	 3.7
##5 	13 	 4.4
##6 	3 	 1.0
##7 	4 	 1.3
##8 	13 	 4.4
##9 	47 	 15.8
##
##Enter leading digit: 6
##
##Showing data with a leading 6
##
##Austin  671,873
##
##Memphis  648,882
##
##Baltimore 638,614
##
##
##
##
##Test Case 4
##
##Data for the 2012 Texas County Population.
##
##number of data points:  254.0
##
##digit	number	percentage
##1 	80 	 31.5
##2 	38 	 15.0
##3 	41 	 16.1
##4 	26 	 10.2
##5 	15 	 5.9
##6 	15 	 5.9
##7 	17 	 6.7
##8 	13 	 5.1
##9 	9 	 3.5
##
##Enter leading digit: 8
##
##Showing data with a leading 8
##
##Angelina County  86771
##
##Castro County  8062
##
##Coleman County  8895
##
##El Paso County  800647
##
##Hamilton County  8517
##
##Hunt County  86129
##
##Kent County  808
##
##Loving County  82
##
##McCulloch County  8283
##
##Orange County  81837
##
##San Augustine County  8865
##
##Somervell County  8490
##
##Victoria County  86793
##
##
##Data for top 298 largest cities in the USA.
##
##number of data points:  298.0
##
##digit	number	percentage
##1 	154 	 51.7
##2 	36 	 12.1
##3 	17 	 5.7
##4 	11 	 3.7
##5 	13 	 4.4
##6 	3 	 1.0
##7 	4 	 1.3
##8 	13 	 4.4
##9 	47 	 15.8
##
##Enter leading digit: 2
##
##Showing data with a leading 2
##
##Chicago  2,886,251
##
##Houston  2,009,834
##
##Buffalo  287,698
##
##Aurora  286,028
##
##St. Paul 284,037
##
##Corpus Christi   278,520
##
##Newark   277,000
##
##Riverside   274,226
##
##Anchorage   268,983
##
##Lexington-Fayette   263,618
##
##Stockton   262,835
##
##Bakersfield   260,969
##
##Louisville   251,399
##
##St. Petersburg   248,546
##
##Jersey   240,100
##
##Birmingham   239,416
##
##Norfolk   239,036
##
##Plano   238,091
##
##Lincoln   232,362
##
##Glendale   230,564
##
##Greensboro   228,217
##
##Hialeah   228,149
##
##Baton Rouge   225,702
##
##Garland   219,646
##
##Rochester   217,158
##
##Scottsdale   215,779
##
##Madison   215,211
##
##Akron   214,349
##
##Fort Wayne   210,070
##
##Fremont   206,856
##
##Chesapeake   206,665
##
##Henderson   206,153
##
##Lubbock   203,715
##
##Modesto   203,555
##
##Chandler   202,016
##
##Montgomery   201,425
##
##
##
##
##Test Case 5
##
##Data for the 2012 Texas County Population.
##
##number of data points:  254.0
##
##digit	number	percentage
##1 	80 	 31.5
##2 	38 	 15.0
##3 	41 	 16.1
##4 	26 	 10.2
##5 	15 	 5.9
##6 	15 	 5.9
##7 	17 	 6.7
##8 	13 	 5.1
##9 	9 	 3.5
##
##Enter leading digit: 0
##
##Showing data with a leading 0
##
##
##Data for top 298 largest cities in the USA.
##
##number of data points:  298.0
##
##digit	number	percentage
##1 	154 	 51.7
##2 	36 	 12.1
##3 	17 	 5.7
##4 	11 	 3.7
##5 	13 	 4.4
##6 	3 	 1.0
##7 	4 	 1.3
##8 	13 	 4.4
##9 	47 	 15.8
##
##Enter leading digit: 0
##
##Showing data with a leading 0

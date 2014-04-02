# File: Fence.py
# Description: A program that determines the cost of a certain type of fence and then calculates the change.
# Assignment Number: Assignment 3
#
# Name: Kevin Achico
# EID: ka6893
# Course Name: CS 303E
#
# Unique Number: 52770
#
# Date created: February 9, 2012
# Date last modified: February 12, 2012
#
# Slip days used this assignment: 0
# Total slip days used: 0

def main():
    y = input("Please enter the length of the fence:")

    wood = y * 16.27 #this is the total cost of a wooden fence with the desired length
    iron = y * 37.89 #this is the total cost of an iron fence with the desired length

    print "The costs for the fences are:\
        \n\t 1. $%.2f for the wooden fence" % wood, \
        "\n\t 2. $%.2f for theiron fence" % iron #prints out the total costs

    fenceNum = input("Would you like fence 1 or fence 2? ") #asks which type of fence the user desires
    print "The fence company only accepts cash." 

    money = input("How much money do you plan to give the fence builder? ")
    
    if(fenceNum == 1): #a conditional is used to determine if the choice is wooden or iron fence
        changeWood = float(money - wood) #changeWood is the total amount of change in the amount of dollars
        changeWoodTotal = int(round(changeWood*100)) #convert the dollar amount into the amount of pennies

        dollarWood = changeWoodTotal / 100 #divide the total by 100 to obtain the amount of dollars. 100 pennies = 1 dollar
        dollarWoodRemainder = changeWoodTotal % 100 #a remainder function is used to calculate the leftover change

        quarterWood = dollarWoodRemainder / 25 #repeat the process with the remainder of change and quarters. 25 pennies = 1 quarter
        quarterWoodRemainder = dollarWoodRemainder % 25

        dimeWood = quarterWoodRemainder / 10 #repeat the process with dimes. 10 pennies = 1 dime
        dimeWoodRemainder = quarterWoodRemainder % 10

        nickelWood = dimeWoodRemainder / 5 #repeat the process with nickels. 5 pennies = 1 nickel
        nickelWoodRemainder = dimeWoodRemainder % 5

        pennieWood = nickelWoodRemainder / 1 #any integer remaining is the amount of pennies left over

        print "Your change, $%.2f, consists of:" %changeWood 
        print "\t %d dollars" %dollarWood, \
              "\n\t %d quarters" %quarterWood, \
              "\n\t %d dimes" %dimeWood, \
              "\n\t %d nickels" %nickelWood, \
              "\n\t %d pennies" %pennieWood #use the space tab and new line escape sequences to line up the output

    else: 
        changeIron = float(money - iron) #repeat the exact same process done with the wooden fence change
        changeIronTotal = int(round(changeIron*100)) 

        dollarIron = changeIronTotal / 100
        dollarIronRemainder = changeIronTotal % 100

        quarterIron = dollarIronRemainder / 25
        quarterIronRemainder = dollarIronRemainder % 25

        dimeIron = quarterIronRemainder / 10
        dimeIronRemainder = quarterIronRemainder % 10

        nickelIron = dimeIronRemainder / 5
        nickelIronRemainder = dimeIronRemainder % 5

        pennieIron = nickelIronRemainder / 1

        print "Your change, $%.2f, consists of:" %changeIron
        print "\t %d dollars" %dollarIron, \
              "\n\t %d quarters" %quarterIron, \
              "\n\t %d dimes" %dimeIron, \
              "\n\t %d nickels" %nickelIron, \
              "\n\t %d pennies" %pennieIron

main()


##TEST CASE 1: 60 feet, wooden, 991.54
##
##Please enter the length of the fence:60
##The costs for the fences are:        
##	 1. $976.20 for the wooden fence 
##	 2. $2273.40 for the iron fence
##Would you like fence 1 or fence 2? 1
##The fence company only accepts cash.
##How much money do you plan to give the fence builder? 991.54
##Your change, $15.34, consists of:
##	 15 dollars 
##	 1 quarters 
##	 0 dimes 
##	 1 nickels 
##	 4 pennies



##TEST CASE 2: 45 feet, iron, 1705.32
##
##Please enter the length of the fence:45
##The costs for the fences are:        
##	 1. $732.15 for the wooden fence 
##	 2. $1705.05 for the iron fence
##Would you like fence 1 or fence 2? 2
##The fence company only accepts cash.
##How much money do you plan to give the fence builder? 1705.32
##Your change, $0.27, consists of:
##	 0 dollars 
##	 1 quarters 
##	 0 dimes 
##	 0 nickels 
##	 2 pennies



##TEST CASE 3: 103 feet, wooden, 1677.64
##
##Please enter the length of the fence:103
##The costs for the fences are:        
##	 1. $1675.81 for the wooden fence 
##	 2. $3902.67 for the iron fence
##Would you like fence 1 or fence 2? 1
##The fence company only accepts cash.
##How much money do you plan to give the fence builder? 1677.64
##Your change, $1.83, consists of:
##	 1 dollars 
##	 3 quarters 
##	 0 dimes 
##	 1 nickels 
##	 3 pennies



##TEST CASE 4: 75 feet, iron, 2954.30
##
##Please enter the length of the fence:75
##The costs for the fences are:        
##	 1. $1220.25 for the wooden fence 
##	 2. $2841.75 for the iron fence
##Would you like fence 1 or fence 2? 2
##The fence company only accepts cash.
##How much money do you plan to give the fence builder? 2954.30
##Your change, $112.55, consists of:
##	 112 dollars 
##	 2 quarters 
##	 0 dimes 
##	 1 nickels 
##	 0 pennies



##TEST CASE 5: 155 feet, wooden, 2625.67
##
##Please enter the length of the fence:155
##The costs for the fences are:        
##	 1. $2521.85 for the wooden fence 
##	 2. $5872.95 for the iron fence
##Would you like fence 1 or fence 2? 1
##The fence company only accepts cash.
##How much money do you plan to give the fence builder? 2625.67
##Your change, $103.82, consists of:
##	 103 dollars 
##	 3 quarters 
##	 0 dimes 
##	 1 nickels 
##	 2 pennies

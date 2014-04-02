# File: MacDonaldSong.pnoise
# Description: Prints "Old MacDonald had a Farm" while using user inputs in the song.
# Assignment Number: 5
#
# Name: Kevin Achico
# EID: ka6893
# Course Name: CS303E
#
# Unique Number: 52770
#
# Date created: February 27, 2012
# Date last modified: March 1, 2012
#
# Slip days used this assignment: 0
# Total slip days used: 0

def main():
    print "Let's sing \"Old MacDonald had a Farm.\""

    for i in range(5): #for loop used to ask for input 5 times
        animal = raw_input("Please enter an animal: ") #input for a string
        noise = raw_input("Please enter a noise: ") #input for a string
        print
        printFirstLast() #calls the printFirstLine function
        printMiddleVerse(animal, noise) #calls the printMiddleVerse with 2 parameters
        printFirstLast() #calls the printFirstLine function
        print

def printFirstLast(): #define a function for the first and last line of the song
    print "Old MacDonald had a farm, E-I-E-I-O"

def printMiddleVerse(animal,noise): #define a function for the middle verse whose parameters are the users inputs
    print "And on that farm, he had some %ss, E-I-E-I-O" % animal 
    print "With a %s-%s here, a %s-%s there" % (noise, noise, noise, noise) 
    print "Here a %s, there a %s" % (noise,noise)
    print "Everywhere a %s-%s" % (noise,noise)

main()

##Test Case
##
##Let's sing "Old MacDonald had a Farm."
##Please enter an animal: pig
##Please enter a noise: oink
##
##Old MacDonald had a farm, E-I-E-I-O
##And on that farm, he had some pigs, E-I-E-I-O
##With a oink-oink here, a oink-oink there
##Here a oink, there a oink
##Everywhere a oink-oink
##Old MacDonald had a farm, E-I-E-I-O
##
##Please enter an animal: cow
##Please enter a noise: moo
##
##Old MacDonald had a farm, E-I-E-I-O
##And on that farm, he had some cows, E-I-E-I-O
##With a moo-moo here, a moo-moo there
##Here a moo, there a moo
##Everywhere a moo-moo
##Old MacDonald had a farm, E-I-E-I-O
##
##Please enter an animal: chicken
##Please enter a noise: cluck
##
##Old MacDonald had a farm, E-I-E-I-O
##And on that farm, he had some chickens, E-I-E-I-O
##With a cluck-cluck here, a cluck-cluck there
##Here a cluck, there a cluck
##Everywhere a cluck-cluck
##Old MacDonald had a farm, E-I-E-I-O
##
##Please enter an animal: dog
##Please enter a noise: woof
##
##Old MacDonald had a farm, E-I-E-I-O
##And on that farm, he had some dogs, E-I-E-I-O
##With a woof-woof here, a woof-woof there
##Here a woof, there a woof
##Everywhere a woof-woof
##Old MacDonald had a farm, E-I-E-I-O
##
##Please enter an animal: cat
##Please enter a noise: meow
##
##Old MacDonald had a farm, E-I-E-I-O
##And on that farm, he had some cats, E-I-E-I-O
##With a meow-meow here, a meow-meow there
##Here a meow, there a meow
##Everywhere a meow-meow
##Old MacDonald had a farm, E-I-E-I-O

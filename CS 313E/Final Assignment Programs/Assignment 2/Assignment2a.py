#  Files: Assignment2a.py
#
#  Description: Use turtle graphics to draw a house with a door, two windows, and a chimney.
#
#  Student's Name: Kevin Achico
#
#  Student's UT EID: ka6893
#
#  Course Name: CS 313E 
#
#  Date Created: September 20, 2012
#
#  Date Last Modified: September 23, 2012

from turtle import*

import math
import time

def drawSquare(turtle, x, y, length = 100):
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(270)
    turtle.down()
    for count in range(4):
        turtle.forward(length)
        turtle.right(90)


def drawRectangle(turtle, x, y, length, width, heading):
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(heading)
    turtle.down()
    
    for j in range(2):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)


def drawTrap(turtle, x, y, up_length = 300, lo_length = 500, side = 100):
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(180)
    turtle.down()
    turtle.forward(lo_length)
    turtle.right(135)
    turtle.forward(side)
    turtle.right(45)
    turtle.forward(up_length + side*math.cos(45))
    turtle.right(45)
    turtle.forward(side)
    turtle.right(135)
    turtle.forward(up_length + side*math.cos(45))
    turtle.up()
    turtle.goto(-250,0)


ttl = Turtle()
ttl.pencolor('red')
drawTrap(ttl, 250 ,0) #draws the roof
drawRectangle(ttl, -250, 0, 300, 500, 270) #draws the walls of the house
ttl.pencolor('blue')
drawRectangle(ttl, -90, 120, 50, 25, 270) #draws the chimney
drawRectangle(ttl, -100, 130, 10, 45, 270) #draws the top of chimney
drawSquare(ttl,-100,-50, 75)#draws windows
drawSquare(ttl, 175,-50, 75)
ttl.pencolor('green')
drawRectangle(ttl, 40, -300, 100, 60, 90)#draws the door

time.sleep(20)

    














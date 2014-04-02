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


ttl = Turtle()
ttl.pencolor('red')
drawSquare(ttl,0,0)
ttl.pencolor('blue')
drawSquare(ttl,50,50,50)
time.sleep(20)

def drawRectangle(turtle, x, y, length = 300, width = 100):
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(270)
    turtle.down()
    
    for j in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)


ttl = Turtle()
ttl.pencolor('red')
drawRectangle(ttl,-50,50)
time.sleep(20)



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
ttl.pencolor('blue')
#drawTrap(ttl, 250, -35)
drawTrap(ttl, 250 ,0)
time.sleep(4)

    














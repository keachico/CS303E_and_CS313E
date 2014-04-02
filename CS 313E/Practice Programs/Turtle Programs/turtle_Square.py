from turtle import *
import math
import time

def drawSquare(turtle, x, y, length=100):
	"""Draws a square with the given turtle, an
	upper-right corner point (x, y), and a side’s length"""
	turtle.up()
	turtle.goto(x, y)
	turtle.setheading(270)
	turtle.down()
	for count in range(4):
		turtle.forward(length)
	turtle.right(90)

	
ttl = Turtle()
ttl.pencolor("red")
drawSquare(ttl, -50, -50)
ttl.pencolor("blue")
drawSquare(ttl, 50, 50, 50)
time.sleep(20)

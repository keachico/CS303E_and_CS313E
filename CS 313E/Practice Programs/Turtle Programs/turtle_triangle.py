from turtle import*

import time

def drawTriangle(turtle, x, y, length = 100, heading = 60):
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(heading)
    turtle.down()
    for count in range(3):
        turtle.forward(length)
        turtle.right(120)

ttl = Turtle()
ttl.speed(0)

ttl.pencolor('purple')
for count in range(0, 200, 5):
    drawTriangle(ttl, (100-count), (100-count), 100-count)
    

ttl.pencolor('red')
for count in range(0, 200, 5):
    drawTriangle(ttl, -(100-count), -(100-count), 100-count, -60)
    
ttl.pencolor('green')
for count in range(0, 200, 5):
    drawTriangle(ttl, -(100-count), (100-count), 100-count)

ttl.pencolor('blue')
for count in range(0, 200, 5):
    drawTriangle(ttl, (100-count), -(100-count), 100-count)



    
time.sleep(4)

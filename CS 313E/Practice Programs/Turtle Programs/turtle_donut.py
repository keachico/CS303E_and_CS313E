def drawDonut(turtle, x, y):
"""Draw 36 circles in a donut shape. Each
circle has radius 45. Figure is centered
on (x, y)."""
    turtle.up()
    turtle.setheading(0)
    direction = turtle.heading()
    
    for i in range(36):
        turtle.setheading(direction)
        turtle.forward(55)
        x1, y1 = turtle.position()
        turtle.down()
        drawCircle(turtle, x1, y1, 45)
        turtle.up()
        turtle.goto(x, y)
        direction += 10

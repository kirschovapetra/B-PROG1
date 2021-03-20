import turtle


turtle.forward(100)
turtle.left(90)
turtle.forward(100)
for i in range(5):
    angle = turtle.towards(0,0)
    pos = turtle.position()
    turtle.goto(0,0)
    turtle.goto(pos)
    turtle.setheading(angle - 90)
    turtle.forward(100)

 


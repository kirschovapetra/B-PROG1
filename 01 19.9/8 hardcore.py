import math
import turtle

a=50
for i in range(5):
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(50)    
    turtle.left(180-math.degrees(math.atan(a/50)))
    a=(a*a+50*50)**(0.5)
    turtle.forward(a)
    turtle.left(180)
turtle.forward(a)
turtle.left(90)
turtle.forward(50)










#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: August 30, 2022
#This program draws a dodecagon (polygon with 12 sides).

import turtle
wn = turtle.Screen()

t = turtle.Turtle()

for i in range(12):
    t.forward(50)
    t.left(30)

wn.exitonclick()
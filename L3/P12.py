#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: September 08, 2022
#This program creates shades of pink and then goes back to black, first increasing in size then decreasing.

import turtle

turtle.colormode(255)
t = turtle.Turtle()
wn = turtle.Screen()

t.penup()
t.backward(200)
t.pendown()
for i in range(0, 255, 10):
    t.pensize(i)
    t.color(i, 0, i)
    t.forward(10)
    
for i in range(255, 0, -10):
    t.pensize(i)
    t.color(i, 0, i)
    t.forward(10)

wn.exitonclick()
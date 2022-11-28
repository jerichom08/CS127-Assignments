#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: September 08, 2022
#This program creates shades of cyan to the right and up.

import turtle

turtle.colormode(255)
t = turtle.Turtle()
wn = turtle.Screen()

t.penup()
t.backward(100)
t.left(90)
t.backward(100)
t.right(90)
for i in range(2):
    t.pendown()
    for j in range(0, 255, 10):
        t.pensize(j)
        t.color(0, j, j)
        t.forward(10)
    t.penup()
    t.backward(260)
    t.left(90)
t.right(90)

wn.exitonclick()
#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: September 08, 2022
#This program creates a brown triangle using a turtle and prints a turtle a each turn.

import turtle

turtle.colormode(255)
t = turtle.Turtle()
wn = turtle.Screen()

t.shape("turtle")
t.color(150, 75, 0)
for i in range(3):
    t.forward(100)
    t.left(120)
    t.stamp()

wn.exitonclick()
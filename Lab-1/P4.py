#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: September 01, 2022
#This program draws the purina logo using green, blue, cyan, and red.

import turtle

wn = turtle.Screen()

t= turtle.Turtle()
t.pensize(5)
t.shape("circle")

t.color("green")
t.forward(300)
for i in range(2):
    t.right(90)
    t.forward(100)
t.right(90)

t.color("blue")
t.forward(300)
for i in range(2):
    t.right(90)
    t.forward(100)
t.right(90)

t.color("cyan")
t.forward(300)
for i in range(2):
    t.right(90)
    t.forward(100)
t.right(90)

t.color("red")
t.forward(300)
for i in range(2):
    t.right(90)
    t.forward(100)
t.right(90)

wn.exitonclick()
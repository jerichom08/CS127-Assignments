#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: August 30, 2022
#This program follows the pseudocode for assignment 3
#It draws a flower.

import turtle
wn = turtle.Screen()

t = turtle.Turtle()

n = int(input("Enter number nine: "))

for i in range(n):
    t.forward(100)
    t.left(105)
    t.forward(52)
    t.left(105)
    t.forward(100)
    t.right(170)

wn.exitonclick()
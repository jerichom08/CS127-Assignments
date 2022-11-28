#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: November 10, 2022
#This program creates a flower petal using top down design.

import turtle

def petal(color, angle):
    t = turtle.Turtle(visible = False)
    turtle.colormode(255)
    t.left(angle)
    if(color == 'red'):
        for i in range(0, 255, 10):
            t.forward(10)
            t.pensize(i)
            t.pencolor(i, 0, 0)
    elif(color == 'green'):
        for i in range(0, 255, 10):
            t.forward(10)
            t.pensize(i)
            t.pencolor(0, i, 0)
    elif(color == 'blue'):
        for i in range(0, 255, 10):
            t.forward(10)
            t.pensize(i)
            t.pencolor(0, 0, i)
    elif(color == 'yellow'):
        for i in range(0, 255, 10):
            t.forward(10)
            t.pensize(i)
            t.pencolor(i, i, 0)
    elif(color == 'purple'):
        for i in range(0, 255, 10):
            t.forward(10)
            t.pensize(i)
            t.pencolor(i, 0, i)
    elif(color == 'cyan'):
        for i in range(0, 255, 10):
            t.forward(10)
            t.pensize(i)
            t.pencolor(0, i, i)
    else:
        for i in range(0, 255, 10):
            t.forward(10)
            t.pensize(i)
            t.pencolor(0, i, 0)
    
def flower(color, num):
    for i in range(num):
        petal(color, i * 360/num)
    
def main():
    flower('green', 9)
    
if __name__ == "__main__":
    main()
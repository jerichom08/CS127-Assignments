#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: November 06, 2022
#This program includes a recursive function that creates a flower petal.

def flowerRecursion(t, n):
    if n > 0:
        t.forward(100)
        t.left(105)
        t.forward(52)
        t.left(105)
        t.forward(100)
        t.right(170)
        flowerRecursion(t, n - 1)
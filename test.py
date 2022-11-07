import turtle
def setUp(t, dist, col):
    t.penup()
    t.forward(dist)
    t.pendown()
    t.color(col)
    
def nestedTriangle(t, side):
    if side > 10:
        for i in range(3):
            t.forward(side)
            t.left(120)
        nestedTriangle(t, side/2)

def fractalTriangle(t, side):
    if side > 10:
        for i in range(3):
            t.forward(side)
            t.left(120)
            fractalTriangle(t, side/2)
            
def main():
    wn = turtle.Screen()
    
    side = int(input('Enter side of a triangle: '))
    nessa = turtle.Turtle()
    setUp(nessa, 100, 'violet')
    nestedTriangle(nessa, side)
    
    frank = turtle.Turtle()
    setUp(frank, -100, 'red')
    fractalTriangle(frank, side)
    wn.exitonclick()
    
if __name__ == '__main__':
    main()
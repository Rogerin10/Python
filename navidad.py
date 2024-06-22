import turtle

turtle.title(" Navidad")
a=turtle.Turtle()
a.getscreen().bgcolor("black")
a.penup()
a.goto(-215,50)
a.pendown()
a.color("#AACDE2")
a.speed(25)

def star(turtle,size):
    if size<=10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.pensize(2)
            turtle.forward(size)
            star(turtle,size/3)
            turtle.left(216)
            turtle.end_fill()

star(a,380)
turtle.done()
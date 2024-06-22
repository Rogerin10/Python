import turtle
import random

def draw_triangle(size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

def draw_rectangle(width, height, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_star(size, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

def draw_bauble(color):
    turtle.penup()
    turtle.goto(random.randint(-70, 70), random.randint(-50, 100))
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

def draw_tree():
    turtle.speed(6)
    turtle.bgcolor("black")
    turtle.pencolor("white")

    # Tronco
    turtle.penup()
    turtle.goto(-20, -150)
    turtle.pendown()
    draw_rectangle(40, 60, "brown")

    # Copas del arbol
    turtle.penup()
    turtle.goto(-120, -90)
    turtle.pendown()
    draw_triangle(240, "forestgreen")

    turtle.penup()
    turtle.goto(-100, -10)
    turtle.pendown()
    draw_triangle(200, "forestgreen")

    turtle.penup()
    turtle.goto(-80, 60)
    turtle.pendown()
    draw_triangle(160, "forestgreen")


    # Bolitas de navidad
    for _ in range(10):
        draw_bauble(random.choice(["red",
                                    "blue",
                                    "gold"]))

    # Estrella
    turtle.penup()
    turtle.goto(-25, 190)
    turtle.pendown()
    draw_star(50, "yellow")

    turtle.hideturtle()
    turtle.done()

draw_tree()

import turtle

def draw_heart():
    turtle.color('pink')
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(180)
    turtle.circle(-90, 200)
    turtle.left(120)
    turtle.circle(-90, 200)
    turtle.forward(180)
    turtle.end_fill()

turtle.setup(width=800, height=600)
turtle.speed(5)
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()

draw_heart()

turtle.hideturtle()

turtle.exitonclick()

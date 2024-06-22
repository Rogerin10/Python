import turtle as t

# Configura la velocidad y el tamaño del lápiz
t.speed(5)
t.pensize(2)

# Dibuja un corazón estilizado
t.fillcolor("red")
t.begin_fill()
t.left(140)
t.forward(224)
for _ in range(200):
    t.right(1)
    t.forward(2)
t.forward(224)
t.end_fill()


 # Dibuja la palabra "Twice"
t.penup()
t.goto(-30, -50)
t.pendown()
t.write("hola", font=("Arial", 14, "normal"))
 
# Cierra la ventana al hacer clic
t.exitonclick()

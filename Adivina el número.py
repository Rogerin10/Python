import random

ganador = random.randint(1, 20)

while True:
    num = int(input("Adivina el número (entre 1 y 20): "))

    if ganador == num:
        print("¡Has ganado!")
        break
    if ganador < num:
        print("El número es menor")
    else:
        print("El número es mayor")
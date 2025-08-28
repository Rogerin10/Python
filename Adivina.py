import random

numero_secreto = random.randint(1, 20)
intento = -1
contador_intentos = 0

print("Adivina el numero entre 1 y 20 (escribe 0 para rendirte):")

while intento != numero_secreto:
    intento = int(input("Ingresa tu intento: "))

    if intento == 0:
        print("El numero secreto era :( ", numero_secreto)
        break

    contador_intentos += 1

    if intento < numero_secreto:
        print("Demasiado bajo. Intenta nuevamente.")
    elif intento > numero_secreto:
        print("Demasiado alto. Intenta nuevamente.")
    else:
        print("¡Felicidades! Adivinaste el número en", contador_intentos, "intentos :) .")

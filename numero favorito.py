import random

mi_numero = 10

bolas = list(range(1, 11))

bolas_final = bolas + [mi_numero] * 15

ganador = random.choice(bolas_final)

print("El número ganador es:", ganador)
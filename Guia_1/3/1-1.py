#Crear una matriz de 3x3 con numneros aleatorios entre 0 y 10

import numpy as np

# Generar matriz de 3x3 con números aleatorios entre 0 y 10
matriz = np.random.randint(0, 11, size=(3, 3))

print(matriz)

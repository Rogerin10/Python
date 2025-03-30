#Crear dos matrices de 2x2 con numeros aleatorios

import numpy as np

# Generar matriz de 2x2 con números aleatorios entre 0 y 10
matriz = np.random.randint(0, 11, size=(2, 2))

print(matriz)
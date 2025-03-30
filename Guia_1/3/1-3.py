#extrae la primera columna de la matriz

import numpy as np

#matriz 3x3
matriz = np.random.randint(0, 11, size=(3, 3))

#extraer la primera columna (0)
columna = matriz[:, 0]

print("Matriz:")
print(matriz)
print("\ncolumna 2:")
print(columna)
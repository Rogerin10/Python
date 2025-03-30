#Realiza la multiplicacion de matrices usando np-dot()

import numpy as np

# Crear dos matrices de ejemplo
matriz_a = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

matriz_b = np.array([[9, 8, 7],
                     [6, 5, 4],
                     [3, 2, 1]])

# Multiplicar las matrices usando np.dot()
resultado = np.dot(matriz_a, matriz_b)

print("Matriz A:")
print(matriz_a)
print("\nMatriz B:")
print(matriz_b)
print("\nResultado de la multiplicación:")
print(resultado)

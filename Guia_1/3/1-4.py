#Cambia el valor de la posicion [2, 1] por 99

import numpy as np

#generar matriz 3x3
matriz = np.random.randint(0, 11, size=(3, 3))

print("Matriz originar: ")
print(matriz)

#cambiar valor
matriz[2, 1] = 99 #tercera fila , segunda columna a 99

print("Matriz con valor cambiado: ") 
print(matriz)
#obten el numero en la posicion [1,2] de la matriz

import numpy as np

#generar matriz de 3x3

matriz = np.random.randint(0, 10, size=(3, 3))  

#obtener el numero en la posicion [1,2]
numero = matriz[1,2]

print("Matriz:")
print(matriz)   
print("El numero en la posicion [1,2] es: ", numero)
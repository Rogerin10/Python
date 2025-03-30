#Encuentra el valor maximo y minimo de un array

import numpy as np

# array entre 0 y 100
array = np.random.randint(0, 101, size=100)

valor_maximo = np.max(array)
valor_minimo = np.min(array)

print("array")
print(array)  # imprime el array
print("\nValor maximo", valor_maximo)  # imprime el valor maximo
print("\n Valor minimo", valor_minimo)  # imprime el valor minimo
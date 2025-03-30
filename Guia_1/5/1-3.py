#Calcula la medida y la mediana

import numpy as np

# array entre 0 y 100
array = np.random.randint(0, 101, size=100)

media = np.mean(array)
mediana = np.median(array)

print("array")
print(array)  # imprime el array
print("\nMedia", media)  # imprime el valor maximo
print("\nMediana", mediana)  # imprime el valor minimo
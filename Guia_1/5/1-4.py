#Encuentra la varianza y desviacion estandar 
import numpy as np

# Crear un array con 100 valores aleatorios entre 0 y 100
array = np.random.randint(0, 101, size=100)

# Calcular la varianza y la desviación estándar
varianza = np.var(array)
desviacion_estandar = np.std(array)

print("Array:")
print(array)
print("\nVarianza:", varianza)
print("Desviación estándar:", desviacion_estandar)

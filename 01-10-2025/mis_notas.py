import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


while True:
    try:
        num_datos_str = input("¿Cuántos pares de 'horas-nota' deseas ingresar? ")
        num_datos = int(num_datos_str)
        if num_datos > 1: 
            break
        else:
            print("Por favor, ingresa un número mayor a 1.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")

horas_ingresadas = []
notas_ingresadas = []
print("\nAhora, ingresa los datos correspondientes.")
for i in range(num_datos):
    print(f"--- Dato #{i + 1} ---")
    while True: 
        try:
            hora_str = input("Horas de estudio: ")
            horas_ingresadas.append(float(hora_str))
            break
        except ValueError:
            print("Valor inválido. Ingresa un número para las horas.")
    while True: 
        try:
            nota_str = input("Nota obtenida: ")
            notas_ingresadas.append(float(nota_str))
            break
        except ValueError:
            print("Valor inválido. Ingresa un número para la nota.")

horas = np.array(horas_ingresadas).reshape(-1, 1)
notas = np.array(notas_ingresadas) 

# Calcular promedio de las notas
promedio = np.mean(notas)
print(f"\nEl promedio de las notas es: {promedio:.2f}")

#crear y entrenar el modelo

modelo = LinearRegression()
modelo.fit(horas, notas)

#predicciones

predicciones = modelo.predict(horas)

#grafico
plt.scatter(horas, notas, color='blue', label='Datos reales')
plt.plot(horas, predicciones, color='red', label='Prediccion (regresion lineal)')
plt.xlabel('Horas de estudio')
plt.ylabel('Notas en la prueba')
plt.title('Predicción vs datos reales')
plt.legend()
plt.show()
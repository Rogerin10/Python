import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


#datos ficticios
horas = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
notas = np.array([2.0, 2.5, 3.0, 3.5, 4.2, 5.0, 5.8, 6.5])

#crear y entrenar el modelo

modelo = LinearRegression()
modelo.fit(horas, notas)

#predicciones

horas_nuevas = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
predicciones = modelo.predict(horas_nuevas)

#grafico
plt.scatter(horas, notas, color='blue', label='Datos reales')
plt.plot(horas, predicciones, color='red', label='Prediccion (regresion lineal)')
plt.xlabel('Horas de estudio')
plt.ylabel('Notas en la prueba')
plt.title('Predicción vs datos reales')
plt.legend()
plt.show()
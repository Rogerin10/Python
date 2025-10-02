import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos ficticios: Tamaño (m²) y Precio (millones de pesos)
X = np.array([40, 50, 60, 80, 100, 120, 140]).reshape(-1, 1)
y = np.array([55, 65, 75, 95, 130, 160, 200])

# Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Mostrar coeficientes del modelo
print("Pendiente (coef):", modelo.coef_[0])
print("Intercepto:", modelo.intercept_)

# Predicciones para graficar la recta
X_nuevo = np.linspace(40, 150, 100).reshape(-1, 1)
y_pred = modelo.predict(X_nuevo)

# Gráfico
plt.scatter(X, y, color="blue", label="Datos reales")
plt.plot(X_nuevo, y_pred, color="red", label="Recta de regresión")
plt.xlabel("Tamaño de la casa (m²)")
plt.ylabel("Precio (millones de pesos)")
plt.title("Predicción de precios de viviendas con Regresión lineal")
plt.legend()
plt.show()

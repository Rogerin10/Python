#librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression

# Crear dataset ficticio
np.random.seed(42)
n = 30
data = {
    "tamano_m2": np.random.randint(50, 200, n),
    "habitaciones": np.random.randint(1, 6, n),
    "antiguedad": np.random.randint(0, 30, n),
    "precio_millones": np.random.randint(50, 500, n)
}

df = pd.DataFrame(data)

# Regresión Lineal Simple
X_simple = df[["tamano_m2"]]
y = df["precio_millones"]

modelo_simple = LinearRegression()
modelo_simple.fit(X_simple, y)


#prediccion
y_pred_simple = modelo_simple.predict(X_simple)

# Gráfico 2D
plt.figure(figsize=(8, 5))
plt.scatter(X_simple, y, color='blue', label='Datos reales')
plt.plot(X_simple, y_pred_simple, color='red', label='Recta de regresión')
plt.xlabel('Tamaño de la casa (m2)')
plt.ylabel('Precio (millones de pesos)')
plt.legend()
plt.show()

#Regresion lineal multiple
x_multiple = df[["tamano_m2", "habitaciones", "antiguedad"]]

modelo_multiple = LinearRegression()
modelo_multiple.fit(x_multiple, y)

#predicciones
y_pred_multiple = modelo_multiple.predict(x_multiple)

# Gráfico 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df["tamano_m2"], df["habitaciones"], y, c='blue', label='Datos reales')
ax.set_xlabel("Tamaño de la casa (m2)")
ax.set_ylabel("habitaciones")
ax.set_zlabel("Precio millones")
ax.set_title("Regresión Lineal Múltiple (30)")
plt.show()

#--- scatter plot de prediccion vs real
plt.figure(figsize=(7, 5))
plt.scatter(y, y_pred_multiple, color='green')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2) #linea diagonal
plt.xlabel("precio real")
plt.ylabel("precio predicho")
plt.title("Predicción vs Real")
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# datos ficticios: tamaño (m2) y precio (milloes de pesos)
x = np.array([40, 50, 60, 80, 100, 120, 140]).reshape(-1, 1)
y = np.array([55, 65, 75, 95, 130, 160, 200])


modelo = LinearRegression()
modelo.fit(x, y)


print("pendiente (coef):", modelo.coef_[0])
print("intercepto:", modelo.intercept_)

x_nuevo = np.linspace(40, 150, 100).reshape(-1, 1)
y_pred = modelo.predict(x_nuevo)

#garafico

plt.scatter(x, y, color='blue', label='Datos reales')
plt.plot(x_nuevo, y_pred, color='red', label="Recta de regresión")
plt.xlabel('Tamaño de la casa (m2)')
plt.ylabel('Precio (millones de pesos)')
plt.legend()
plt.show()


#ejemplo de prediccion
nueva_casa = np.array([[100]])
precio_pred = modelo.predict(nueva_casa)
print(f"precio estimado para una casa de 100 m2: ${precio_pred[0]:.2f} millones de pesos")
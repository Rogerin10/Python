import numpy as np
from sklearn.linear_model import LinearRegression

#datos de ejemplo (x debe ser 2d para sklearn)

x = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

#crear el modelo

modelo = LinearRegression()

#entrenar (ajustar el modelo)
modelo.fit(x, y)

#hacer una prediccion
prediccion = modelo.predict([[6]]) # que pasa si x = 6

print("Coeficiente (pendiente):", modelo.coef_)
print("Intercepto:", modelo.intercept_)
print("prediccion para x=6:", prediccion)
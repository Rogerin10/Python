import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('notas.csv')

print("Primeras 5 filas del DataFrame:")
print(df.head())
print("\nInformación del DataFrame:")
df.info()
print("-" * 30)

promedio_por_estudiante = df.groupby('nombre')['nota'].mean()
print("\nPromedio de Notas por Estudiante:")
print(promedio_por_estudiante.round(2))
print("-" * 30)

promedio_por_asignatura = df.groupby('asignatura')['nota'].mean()
print("\nPromedio de Notas por Asignatura:")
print(promedio_por_asignatura.round(2))
print("-" * 30)

df_agrupado = df.groupby('nombre').agg(
    asignaturas=('asignatura', 'nunique'),
    promedio_nota=('nota', 'mean')
).reset_index()
mejor_estudiante = promedio_por_estudiante.idxmax()
mejor_promedio = promedio_por_estudiante.max()

print(f"\nEl estudiante con mayor promedio es: {mejor_estudiante} ({mejor_promedio:.2f})")
print(f"\n")

X = df_agrupado[['asignaturas']]    
y = df_agrupado['promedio_nota']    

modelo = LinearRegression()
modelo.fit(X, y)

print("Pendiente (coef):", modelo.coef_[0])
print("Intercepto:", modelo.intercept_)
print(f"\n")

X_nuevo = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_pred = modelo.predict(X_nuevo)

plt.figure(figsize=(10, 6))

df.boxplot(column='nota', by='asignatura', grid=False)
plt.title('Distribución de Notas por Asignatura')
plt.suptitle('')
plt.xlabel('Asignatura')
plt.ylabel('Nota')
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(X_nuevo, y_pred, color='red', label='Recta de regresión')
plt.xlabel('Cantidad de Asignaturas')
plt.ylabel('Promedio de Nota')
plt.title('Regresión lineal: Asignaturas vs Promedio de Nota')
plt.legend()
plt.show()

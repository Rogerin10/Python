import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from scipy.stats import randint

# =========================================================
# 1. Creación del Dataset (Simulación de Datos)
#    Se utiliza NumPy para generar 300 filas de datos sintéticos.
# =========================================================

np.random.seed(42) # Fija la semilla para que los datos generados sean reproducibles
N = 300            # Define la cantidad de registros (vuelos) a generar (cumple con N >= 250)

# Variables (Características X)
# Genera 300 números aleatorios para cada característica dentro de un rango realista
distancia = np.random.uniform(500, 10000, N) # Distancia del vuelo en km
duracion = np.random.uniform(1, 15, N)       # Duración del vuelo en horas
# Genera enteros aleatorios para las escalas (0, 1, 2, o 3)
escalas = randint.rvs(0, 4, N)
edad_flota = np.random.uniform(1, 20, N)     # Edad promedio de la flota en años

# Variable Objetivo (Precio Y)
precio_base = 100
# Fórmula lineal para simular el precio basado en las características,
# añadiendo ruido (varianza) para simular la realidad.
precio = (
    precio_base +
    0.05 * distancia +     # La distancia tiene un efecto positivo en el precio
    30 * duracion +        # La duración tiene un efecto positivo en el precio
    50 * escalas -         # Más escalas aumentan un poco el precio
    5 * edad_flota +       # Flotas más viejas pueden reducir ligeramente el precio
    np.random.normal(0, 75, N) # Añade un componente de ruido/aleatoriedad
)
precio[precio < 50] = 50 # Asegura que ningún precio sea irrealmente bajo

# Crea el DataFrame de Pandas
data = {
    'Distancia (km)': distancia.round(0),
    'Duracion (horas)': duracion.round(1),
    'Cantidad de escalas': escalas,
    'Edad promedio flota (años)': edad_flota.round(1),
    'Precio (USD)': precio.round(2) # Esta es la variable objetivo (Y)
}
df = pd.DataFrame(data)

print("Primeras 5 filas del Dataset:")
print(df.head())

# =========================================================
# 2. Visualización (Exploración de Datos - Requisito 1)
#    Se crean 4 gráficos de dispersión (scatter plots) en una sola figura.
# =========================================================

features = ['Distancia (km)', 'Duracion (horas)', 'Cantidad de escalas', 'Edad promedio flota (años)']
target = 'Precio (USD)'

# Crea la figura contenedora
# figsize=(15, 10) define el tamaño general de la imagen para que los 4 subplots se vean bien
plt.figure(figsize=(15, 10))

# Itera sobre cada característica para crear su propio gráfico vs. el precio
for i, col in enumerate(features):
    # Función CLAVE para los 4 gráficos juntos: plt.subplot(filas, columnas, posicion)
    # Crea una cuadrícula de 2 filas y 2 columnas (2, 2).
    # i + 1 define la posición: 1, 2, 3, y 4 en cada iteración.
    plt.subplot(2, 2, i + 1)

    # Crea el gráfico de dispersión
    plt.scatter(df[col], df[target], color='teal', alpha=0.7)

    # Configura los elementos del gráfico actual (título y etiquetas)
    plt.title(f'{col} vs. {target}')
    plt.xlabel(col)
    plt.ylabel(target)

# Ajusta el espaciado entre los subgráficos para evitar que se superpongan
plt.tight_layout()

# Muestra la figura completa con los 4 subgráficos
plt.show()
# Definir X e y
X = df[features]
y = df[target]

# Dividir en entrenamiento y prueba (Requisito 2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Escalar los datos con StandardScaler (Requisito 2)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Datos de entrenamiento escalados: {X_train_scaled.shape}")

# Encontrar el k óptimo (Requisito 2)
max_k = 20
k_range = range(1, max_k + 1)
mse_values = []

for k in k_range:
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    y_pred = knn.predict(X_test_scaled)
    mse_values.append(mean_squared_error(y_test, y_pred))

# Encontrar el k con el MSE más bajo
optimal_k = k_range[np.argmin(mse_values)]
min_mse = np.min(mse_values)

print(f"\nEl valor óptimo de n_neighbors (k) es: {optimal_k}")
print(f"El MSE mínimo asociado es: {min_mse:.2f}")

# Reentrenar el mejor modelo
knn_best = KNeighborsRegressor(n_neighbors=optimal_k)
knn_best.fit(X_train_scaled, y_train)
y_pred_best = knn_best.predict(X_test_scaled)

# Evaluación final (Requisito 3)
final_mse = mean_squared_error(y_test, y_pred_best)
final_r2 = r2_score(y_test, y_pred_best)

print("\n--- Evaluación del Modelo Óptimo (Escalado) ---")
print("Error Cuadrático Medio (MSE): {final_mse:.2f}")
print("Coeficiente de Determinación (R2 Score): {final_r2:.4f}")

plt.figure(figsize=(10, 5))
plt.plot(k_range, mse_values, marker='o', linestyle='-', color='red')
plt.axvline(x=optimal_k, color='green', linestyle='--', label=f'k óptimo={optimal_k}')
plt.title('MSE vs. n_neighbors (k)')
plt.xlabel('Número de Vecinos (k)')
plt.ylabel('Error Cuadrático Medio (MSE)')
plt.xticks(k_range)
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 8))
plt.scatter(y_test, y_pred_best, color='blue', alpha=0.6)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2, label='Línea Ideal')
plt.xlabel('Precios Reales (USD)')
plt.ylabel('Precios Predichos (USD)')
plt.title(f'Precios Reales vs. Predichos (k={optimal_k})')
plt.legend()
plt.grid(True)
plt.show()

# Análisis de correlación (Requisito 4)
correlation_matrix = df.corr()
price_correlation = correlation_matrix[target].sort_values(ascending=False)

print("\n--- Correlación de Variables con el Precio (USD) ---")
print(price_correlation)

most_correlated_feature = price_correlation[1:].abs().idxmax()
print(f"\nLa variable con mayor correlación (valor absoluto) con el Precio es: {most_correlated_feature}")

# Predicciones para 3 rutas nuevas (Requisito 4)
nuevas_rutas_data = {
    'Distancia (km)': [800, 5500, 9500],
    'Duracion (horas)': [1.5, 7.0, 14.0],
    'Cantidad de escalas': [0, 1, 3],
    'Edad promedio flota (años)': [15.0, 5.0, 10.0]
}
nuevas_rutas_df = pd.DataFrame(nuevas_rutas_data)

# Escalar los nuevos datos
X_new = nuevas_rutas_df[features]
X_new_scaled = scaler.transform(X_new)

# Hacer las predicciones
predicciones_nuevas = knn_best.predict(X_new_scaled).round(2)

# Mostrar resultados
nuevas_rutas_df['Precio Predicho (USD)'] = predicciones_nuevas

print("\n--- Predicciones para 3 Rutas Nuevas (k={optimal_k}) ---")
print(nuevas_rutas_df)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from scipy.stats import randint

# 1. Crear el dataset sintético (N >= 250)
np.random.seed(42)
N = 300

# Generar características (features)
distancia = np.random.uniform(500, 10000, N)
duracion = np.random.uniform(1, 15, N)
escalas = randint.rvs(0, 4, N) # 0, 1, 2, o 3 escalas
edad_flota = np.random.uniform(1, 20, N)

# Generar el Precio (Target) simulando relaciones:
# Precio = f(Distancia, Duración, Escalas) - g(Edad) + Ruido
precio_base = 100
precio = (
    precio_base +
    0.05 * distancia +
    30 * duracion +
    50 * escalas -
    5 * edad_flota +
    np.random.normal(0, 75, N)
)
# Asegurar un precio mínimo
precio[precio < 50] = 50

data = {
    'Distancia (km)': distancia.round(0),
    'Duracion (horas)': duracion.round(1),
    'Cantidad de escalas': escalas,
    'Edad promedio flota (años)': edad_flota.round(1),
    'Precio (USD)': precio.round(2)
}

df = pd.DataFrame(data)

# Mostrar las primeras filas del dataset
print("Primeras 5 filas del Dataset:")
print(df.head())
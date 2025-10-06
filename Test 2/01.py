import numpy as np
import pandas as pd   

df = pd.read_csv("fiestas.csv")

print("Primeras 10 filas del DataFrame:")
print(df.head(10))

# Obtener y mostrar el numero de filas y columnas
filas, columnas = df.shape
print(f"\nEl dataset tiene {filas} filas y {columnas} columnas.")

# Obtener y mostrar el numero de regiones distintas
regiones_distintas = df['region'].nunique()
print(f"Aparecen {regiones_distintas} regiones distintas en la columna 'region'.")

import numpy as np
import pandas as pd   

df = pd.read_csv("fiestas.csv")

promedio_alcohol = df['litros_bebida_alcoholica'].mean()
mediana_alcohol = df['litros_bebida_alcoholica'].median()

print(f"\nEl promedio de 'litros_bebida_alcoholica' es: {promedio_alcohol:.2f}")
print(f"La mediana de 'litros_bebida_alcoholica' es: {mediana_alcohol:.2f}")

max_carne = df['kg_carne'].max()
min_carne = df['kg_carne'].min()
promedio_carne = df['kg_carne'].mean()

print(f"\nEl maximo de 'kg_carne' es: {max_carne}")
print(f"El minimo de 'kg_carne' es: {min_carne}")
print(f"El promedio de 'kg_carne' es: {promedio_carne:.2f}")

# Edad promedio general de los asistentes
promedio_edad_general = df['edad_promedio_asistentes'].mean()
print(f"\nLa edad promedio general de los asistentes es: {promedio_edad_general:.0f} años.")
print("\n")

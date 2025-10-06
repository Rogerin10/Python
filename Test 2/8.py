import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("fiestas.csv")

# Crear nuevas columnas
df['consumo_alcohol_por_persona'] = df['litros_bebida_alcoholica'] / df['n_asistentes']
df['accidentes_por_1000'] = (df['accidentes_transito'] / df['n_asistentes']) * 1000
print("\n")

print("Promedio de consumo por persona:", df['consumo_alcohol_por_persona'].mean())
print("Promedio de accidentes por 1000 personas:", df['accidentes_por_1000'].mean())
print("Correlación entre consumo y accidentes:", df[['consumo_alcohol_por_persona', 'accidentes_por_1000']].corr().iloc[0, 1])
print("\n")

plt.figure(figsize=(8, 6))
plt.scatter(df['consumo_alcohol_por_persona'], df['accidentes_por_1000'], color='crimson', alpha=0.7, edgecolors='black')
plt.title("Consumo de Alcohol vs Accidentes por 1000 Personas")
plt.xlabel("Consumo de Alcohol por Persona (litros)")
plt.ylabel("Accidentes por cada 1000 Asistentes")
plt.grid(True)
plt.tight_layout()
plt.show()
print("\n")
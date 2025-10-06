import numpy as np
import pandas as pd   

df = pd.read_csv("fiestas.csv")

# eventos con mas de 2000 asistentes
eventos_masivos = df[df['n_asistentes'] > 2000]
print("1. Eventos con más de 2000 asistentes:")
print(f"(Mostrando las primeras 5 de {len(eventos_masivos)} filas encontradas)\n", eventos_masivos.head())

# eventos con mass de 500 litros de alcohol y al menos 1 fallecido
eventos_criticos = df[(df['litros_bebida_alcoholica'] > 500) & (df['fallecidos'] >= 1)]
print("\n\n2. Eventos con >500L de alcohol y al menos 1 fallecido:")
print(eventos_criticos)
print("total de eventos críticos encontrados:", len(eventos_criticos))

# eventos anteriores en condiciones de lluvia
eventos_criticos_lluviosos = eventos_criticos[eventos_criticos['condiciones_climaticas'] == 'Lluvioso']
cantidad_lluviosos = len(eventos_criticos_lluviosos)
print(f"\n\n3. De esos eventos críticos, {cantidad_lluviosos} se realizaron en condiciones de 'Lluvioso'.")
print("\n")

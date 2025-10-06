import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("fiestas.csv")

# columnas nuevas
df['consumo_alcohol_por_persona'] = df['litros_bebida_alcoholica'] / df['n_asistentes']
df['accidentes_por_mil_asistentes'] = (df['accidentes_transito'] / df['n_asistentes']) * 1000

regiones = df['region'].unique()
colores = plt.cm.tab20.colors 
color_map = {region: colores[i % len(colores)] for i, region in enumerate(regiones)}

plt.figure(figsize=(10, 6))
for region in regiones:
    datos = df[df['region'] == region]
    plt.scatter(
        datos['consumo_alcohol_por_persona'],
        datos['accidentes_por_mil_asistentes'],
        color=color_map[region],
        label=region,
        alpha=0.7,
        edgecolors='black'
    )

plt.title("Consumo de Alcohol vs Accidentes por 1000 Asistentes, según Región")
plt.xlabel("Consumo de Alcohol por Persona (litros)")
plt.ylabel("Accidentes por cada 1000 Asistentes")
plt.legend(title="Región", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

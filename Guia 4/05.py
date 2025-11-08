import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display

df = pd.read_csv("sernageomin.csv")


#Extraer el año desde la columna de fecha 
df['año'] = pd.to_datetime(df['fecha_evento']).dt.year

# por año y nivel de peligro 
actividad_por_año = df.groupby(['año', 'nivel_peligro']).size().reset_index(name='n_eventos')

#Mostrar las primeras filas
print("Número de eventos por año y nivel de peligro:")
display(actividad_por_año.head(10))
print("\n")

#estilo
sns.set(style="whitegrid")

# Crear la figura y el gráfico de líneas
plt.figure(figsize=(12,6))
sns.lineplot(
    data=actividad_por_año, 
    x='año', 
    y='n_eventos', 
    hue='nivel_peligro', 
    marker='o',
    palette='Set1' 
)

# Añadir títulos y etiquetas
plt.title('Tendencia de eventos volcánicos por nivel de peligro', fontsize=16)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Número de eventos', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Nivel de peligro')
plt.tight_layout()
plt.show()
print("\n")

#analisis

#Sumar los eventos por año
eventos_por_año = actividad_por_año.groupby('año')['n_eventos'].sum().reset_index()

#año con más eventos
año_max = eventos_por_año.loc[eventos_por_año['n_eventos'].idxmax()]
print(f"Año más activo: {año_max['año']} con {año_max['n_eventos']} eventos")
print("\n")

# Sumar los eventos por nivel de peligro
eventos_por_nivel = actividad_por_año.groupby('nivel_peligro')['n_eventos'].sum().reset_index()

# Nivel con mas eventos
nivel_max = eventos_por_nivel.loc[eventos_por_nivel['n_eventos'].idxmax()]
print(f"Nivel de peligro predominante: {nivel_max['nivel_peligro']} con {nivel_max['n_eventos']} eventos")
print("\n")

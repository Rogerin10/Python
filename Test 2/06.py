import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("fiestas.csv")

plt.figure(figsize=(10, 6))

plt.hist(df['kg_carne'], bins=30, color='skyblue', edgecolor='black')

plt.title('Distribución del Consumo de Carne (kg) en Eventos')
plt.xlabel('Kg de Carne Consumidos')
plt.ylabel('Frecuencia (Número de Eventos)')
plt.grid(axis='y', alpha=0.75)
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("fiestas.csv")

eventos_por_region = df['region'].value_counts()

plt.figure(figsize=(12, 7))

eventos_por_region.plot(kind='bar', color='coral', edgecolor='black')

plt.title('Cantidad de Eventos por Región', fontsize=16)
plt.xlabel('Región', fontsize=12)
plt.ylabel('Número de Eventos', fontsize=12)
plt.xticks(rotation=45, ha='right') 
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout() 
plt.show()

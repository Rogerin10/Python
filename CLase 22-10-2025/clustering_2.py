import pandas as pd 
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

#crear dataset

data = {
    'Edad': [23, 27, 29, 31, 35, 40, 45, 46, 48, 53],
    'Ingresos': [2500, 2700, 2900, 3100, 3500, 4200, 4800, 5000, 5200, 5500]
}
df = pd.DataFrame(data)
print("Datos iniciales:\n")
print(df)

#Aplicar el metodo de enlace jerarquico

z = linkage(df, method='ward')

#dibujar el dendrograma
plt.figure(figsize=(10, 5))
dendrogram(z, labels=df.index, color_threshold=2000)
plt.title('Dendrograma de clustering Jerarquico')
plt.xlabel('Indice de Observacion')
plt.ylabel('Distancia (Ward)')
plt.show()

#Crear los clusteres a partir del dendrograma

grupos = fcluster(z, t=3, criterion='maxclust')
df

print("\nAsignacion de clusteres")
print(df)
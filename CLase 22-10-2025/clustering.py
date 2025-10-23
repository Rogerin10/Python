import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#Crear dataset
data = {
    'Ingresos_anuales': [15, 16, 17, 18, 20, 40, 42, 43, 44, 60, 62, 63, 65, 80, 85, 87],
    'Gasto_anual': [39, 40, 42, 43, 45, 65, 66, 68, 70, 85, 87, 88, 90, 95, 98, 99]
}
df = pd.DataFrame(data)

print("Datos iniciales:\n")
print(df.head())

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(df)

# Agregar los resultados
df['Cluster'] = kmeans.labels_

#Visualizar los clusters
plt.figure(figsize=(8, 5))
plt.scatter(df['Ingresos_anuales'], df['Gasto_anual'], c=df['Cluster'], cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', s=200, marker='X',)
plt.title('Clusters de Clientes con K-Means')
plt.xlabel('Ingresos Anuales (miles $)')
plt.ylabel('Gasto Anual (miles $)')
plt.grid(True)
plt.savefig('clusters_clientes.png') # Añade esta línea para guardar el gráfico
plt.show()

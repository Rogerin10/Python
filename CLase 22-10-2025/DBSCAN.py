import pandas as pd
import seaborn as sns
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# 1. Generar el dataset tipo "moons"
X, _ = make_moons(n_samples=400, noise=0.05, random_state=0)

# 2. Crear un DataFrame para facilitar el manejo
df = pd.DataFrame(X, columns=['x', 'y'])

# 3. Visualizar los datos originales
sns.scatterplot(data=df, x='x', y='y', legend=False)
plt.title("Distribución original del dataset")
plt.show()

# 4. Instanciar el modelo DBSCAN con distancia máxima entre puntos (eps)
dbscan_model = DBSCAN(eps=0.2)

# 5. Entrenar el modelo y obtener etiquetas de clúster
df['Cluster'] = dbscan_model.fit_predict(X)

# Paleta K-pop vibes
kpop_palette = ['#BA55D3',  # púrpura eléctrico (EVERGLOW)
                '#00CED1',  # turquesa brillante (TWICE)
                '#FF4500']  # naranja neón (performance energy)

# Visualizar los clústeres con estilo K-pop
sns.scatterplot(data=df, x='x', y='y', hue='Cluster', palette=kpop_palette)
plt.title("Clústeres con estilo K-pop 💫")
plt.show()

import pandas as pd
import seaborn as sns
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# 1. Generar el dataset tipo "moons"
X, _ = make_moons(n_samples=400, noise=0.05, random_state=0)
df = pd.DataFrame(X, columns=['x', 'y'])

# 2. Estilo visual K-pop
sns.set_style("darkgrid")  # Fondo con líneas suaves
plt.figure(figsize=(8, 6))
plt.rcParams['axes.facecolor'] = '#1a1a2e'  # Fondo oscuro tipo escenario
plt.rcParams['figure.facecolor'] = '#0f3460'  # Fondo general vibrante

# 3. Aplicar DBSCAN
dbscan_model = DBSCAN(eps=0.2)
df['Cluster'] = dbscan_model.fit_predict(X)

# 4. Paleta K-pop personalizada
kpop_palette = ['#FF69B4', '#BA55D3', '#00CED1', '#FFD700', '#FF4500']

# 5. Visualizar con estilo
sns.scatterplot(data=df, x='x', y='y', hue='Cluster', palette=kpop_palette, s=60)
plt.title("✨ Clústeres con estilo K-pop 💜🎧", fontsize=14, color='white')
plt.xlabel("x", color='white')
plt.ylabel("y", color='white')
plt.xticks(color='white')
plt.yticks(color='white')
plt.legend(title='Cluster', loc='upper right', facecolor='#1a1a2e', edgecolor='white', labelcolor='white')
plt.show()

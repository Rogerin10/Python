import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("fiestas.csv")

# colores  
colores = {
    'Soleado': 'gold',
    'Nublado': 'grey',
    'Lluvioso': 'dodgerblue'
}

plt.figure(figsize=(8, 6))

for clima, color in colores.items():
    datos = df[df['condiciones_climaticas'] == clima]
    plt.scatter(
        datos['litros_bebida_alcoholica'],
        datos['accidentes_transito'],
        color=color,
        label=clima,
        alpha=0.7,
        edgecolors='black'
    )

plt.title("Alcohol vs Accidentes según Clima")
plt.xlabel("Litros de Bebida Alcohólica")
plt.ylabel("Número de Accidentes de Tránsito")
plt.grid(True)
plt.legend(title="Condición Climática")
plt.tight_layout()
plt.show()
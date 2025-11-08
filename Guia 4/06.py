import pandas as pd
import requests
import pandas as pd

import requests
import pandas as pd


# Cargar el archivo CSV 
df = pd.read_csv('pokemones.csv')
# Mostrar los primeros registros
print(df.head())

# Separar multiples tipos en filas individuales
df_exploded = df.copy()
df_exploded['type'] = df_exploded['type'].str.split(', ')
df_exploded = df_exploded.explode('type')

# Promedio de peso y altura por tipo
promedios = df_exploded.groupby('type')[['weight', 'height']].mean().round(2)
print("Promedio por tipo:")
print(promedios)

# Pokémon mas pesado
mas_pesado = df.loc[df['weight'].idxmax()]
print("\nPokémon más pesado:")
print(mas_pesado)

# Pokémon mas liviano
mas_liviano = df.loc[df['weight'].idxmin()]
print("\n🪶 Pokémon más liviano:")
print(mas_liviano)

df.to_csv('pokemones.csv', index=False)
# Cargar el archivo CSV




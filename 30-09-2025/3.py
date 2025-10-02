import pandas as pd
df = pd.read_csv('peliculas.csv')

print("Primeras 5 filas del DataFrame:")
print(df.head())
print("\nInformación del DataFrame:")
df.info()
print("-" * 30)

peliculas_filtradas = df[(df['votos'] > 1000) & (df['rating'] > 7)]

print("\nPelículas con más de 1000 votos y rating mayor a 7:")
print(peliculas_filtradas)

print(f"\nSe encontraron {len(peliculas_filtradas)} películas que cumplen con los criterios.")

promedio_de_rating = df['rating'].mean()
print(f"\nEl promedio de rating de las películas es: {promedio_de_rating:.2f}")

promedio_por_genero = df.groupby('genero')['rating'].mean()
print("\nPromedio de rating por género:")
print(promedio_por_genero.round(2))

print(f"\n")
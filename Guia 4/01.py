import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("autos.csv")

print("Primeras 5 filas del DataFrame:")
print(df.head())

print("Información general:")
print(df.info())

print("Valores nulos por columna:")
print(df.isnull().sum())

print("\n")
df.columns = df.columns.str.lower().str.replace(" ", "_")

df.drop(columns=["unnamed:0", "modelo"], inplace=True, errors='ignore')


num_filas = len(df)
df['kilometraje'] = np.random.randint(5000, 200000, size=num_filas)
print("\n")

print("\n'kilometraje':")
print(df.head())
print("\n")

print("\nEstadísticas generales (incluyendo kilometraje):")
print(df.describe())
print("\n")


print("Precio mínimo:", df["precio"].min())
print("Precio máximo:", df["precio"].max())
print("Año más antiguo:", df["año"].min())
print("Año más reciente:", df["año"].max())
print("Kilometraje mínimo:", df["kilometraje"].min())
print("Kilometraje máximo:", df["kilometraje"].max())
print("\n")


plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x="año", y="precio")
plt.title("Relación entre precio y año del auto")
plt.xlabel("Año del auto")
plt.ylabel("Precio")
plt.grid(True)
plt.show()
print("\n")


plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="kilometraje", y="precio", alpha=0.6)
plt.title("Relación entre precio y kilometraje del auto")
plt.xlabel("Kilometraje")
plt.ylabel("Precio")
plt.grid(True)
plt.show()

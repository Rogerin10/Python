import numpy as np
import pandas as pd   

df = pd.read_csv("fiestas.csv")

print("\n")
corr_alcohol_accidentes = df['litros_bebida_alcoholica'].corr(df['accidentes_transito'])
print("1. Correlación entre 'litros_bebida_alcoholica' y 'accidentes_transito':")
print(f"{corr_alcohol_accidentes:.4f}")

corr_asistentes_carne = df['n_asistentes'].corr(df['kg_carne'])
print("\n2. ¿Existe relación entre 'n_asistentes' y 'kg_carne' consumidos?")
print(f"Correlación: {corr_asistentes_carne:.4f}")
print("\n")

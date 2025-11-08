import pandas as pd
import matplotlib.pyplot as plt

horas_totales = 519
semanas_totales = 9.1 * 52  
promedio_semanal = horas_totales / semanas_totales  
promedio_diario = horas_totales / (semanas_totales * 7)  

print(f"Promedio semanal de horas: {promedio_semanal:.2f} horas/semana")
print(f"Promedio diario de horas: {promedio_diario:.2f} horas/día")

data = {
    "horas_trabajo": [0],
    "ingreso_mensual": [100000],
    "gasto_steam": [2250],
    "horas_juego": [promedio_semanal],
    "gasto_total_steam": [45960] 
}

df = pd.DataFrame(data)
print("Dataset:\n", df)

plt.scatter(df["ingreso_mensual"], df["gasto_steam"], color="blue", s=120)

for i in range(len(df)):
    plt.text(df["ingreso_mensual"][i] + 2000, df["gasto_steam"][i] + 100,
             f"Registro {i+1}")

plt.xlabel("Ingreso mensual (CLP)")
plt.ylabel("Gasto mensual en Steam (CLP)")
plt.title("Relación entre ingreso mensual y gasto en Steam")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

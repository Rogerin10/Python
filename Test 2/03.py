import numpy as np
import pandas as pd   

df = pd.read_csv("fiestas.csv")

fallecidos_heridos_por_region = df.groupby('region')[['fallecidos', 'heridos']].sum()
print("\n1. Total de fallecidos y heridos por región:")
print(fallecidos_heridos_por_region)

detenidos_por_region = df.groupby('region')['detenidos'].sum()
region_mas_detenidos = detenidos_por_region.idxmax()
total_detenidos = detenidos_por_region.max()
print(f"\n2. La región con más detenidos en total es '{region_mas_detenidos}' con {total_detenidos} detenidos.")

asistentes_por_evento = df.groupby('tipo_evento')['n_asistentes'].mean()
evento_mas_asistentes = asistentes_por_evento.idxmax()
promedio_asistentes = asistentes_por_evento.max()
print(f"\n3. El tipo de evento con más asistentes en promedio es '{evento_mas_asistentes}' con {promedio_asistentes:.0f} asistentes.")
print("\n")

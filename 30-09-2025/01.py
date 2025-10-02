import pandas as pd 

df = pd.read_csv('ventas.csv')

print("Primeras 5 filas del DataFrame:")
print(df.head())
print("\nInformación del DataFrame:")
df.info()
print("-" * 30)


df['Fecha'] = pd.to_datetime(df['Fecha'])

df['Mes'] = df['Fecha'].dt.strftime('%Y-%m')

ingresos_por_mes = df.groupby('Mes')['Ingreso'].sum()

print("\nIngreso Total por Mes:")
print(ingresos_por_mes)

mes_mayor_ingreso = ingresos_por_mes.idxmax()
mes_menor_ingreso = ingresos_por_mes.idxmin()

print(f"\nMes con mayor ingreso: {mes_mayor_ingreso} (Total: {ingresos_por_mes.max():.2f})")
print(f"Mes con menor ingreso: {mes_menor_ingreso} (Total: {ingresos_por_mes.min():.2f})")


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv("autos.csv")
df.columns = df.columns.str.lower().str.replace(" ", "_")
df = df.drop(columns=["unnamed:0", "id_auto", "modelo"], errors='ignore')

np.random.seed(42)
df['kilometraje'] = df.get('kilometraje', np.random.randint(5_000, 200_000, len(df)))
df['año'] = df.get('año', np.random.randint(2000, 2023, len(df)))
df['tipo_transmision'] = df.get('tipo_transmision', np.random.choice(['Manual', 'Automática'], len(df)))

df = pd.get_dummies(df, columns=['tipo_transmision'], drop_first=True)

y = df['precio']
X_s = df[['kilometraje']]
X_m = df[['año', 'kilometraje', 'tipo_transmision_Manual']]

X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X_s, y, test_size=0.2, random_state=42)
X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(X_m, y, test_size=0.2, random_state=42)

m_s = LinearRegression().fit(X_train_s, y_train_s)
m_m = LinearRegression().fit(X_train_m, y_train_m)

pred_s, pred_m = m_s.predict(X_test_s), m_m.predict(X_test_m)
r2_s, r2_m = r2_score(y_test_s, pred_s), r2_score(y_test_m, pred_m)
mse_s, mse_m = mean_squared_error(y_test_s, pred_s), mean_squared_error(y_test_m, pred_m)

print(f"R² simple: {r2_s:.3f} | múltiple: {r2_m:.3f}")
print(f"MSE simple: {mse_s:.2f} | múltiple: {mse_m:.2f}\n")
print("Coeficientes (modelo múltiple):", dict(zip(X_m.columns, m_m.coef_)))

plt.figure(figsize=(6, 4))
plt.scatter(y_test_m, pred_m, alpha=0.7)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.title("Precio real vs predicho")
plt.xlabel("Precio real"); plt.ylabel("Predicho"); plt.grid(True)
plt.show()

sns.histplot(y_test_m - pred_m, kde=True)
plt.title("Distribución de residuos")
plt.xlabel("Error"); plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("autos.csv")
df.columns = df.columns.str.lower().str.replace(" ", "_")
df = df.drop(columns=["unnamed:0", "id_auto", "modelo"], errors='ignore')

np.random.seed(42)
df['kilometraje'] = np.random.randint(5_000, 200_000, size=len(df))

X = df[['kilometraje']]
y = df['precio']

# --- División de datos ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = LinearRegression().fit(X_train, y_train)

y_pred = modelo.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Intercepto: {modelo.intercept_:.2f}")
print(f"Coeficiente (kilometraje): {modelo.coef_[0]:.4f}")
print(f"MSE: {mse:.2f}")
print(f"R²: {r2:.2f}")

plt.figure(figsize=(8, 5))
sns.scatterplot(x=X_test['kilometraje'], y=y_test, label='Datos reales')
plt.plot(X_test, y_pred, color='red', label='Línea de regresión')
plt.title('Precio vs. Kilometraje')
plt.xlabel('Kilometraje')
plt.ylabel('Precio')
plt.legend()
plt.grid(True)
plt.show()

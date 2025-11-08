import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv("veterinaria.csv")
df.columns = df.columns.str.lower().str.replace(' ', '_')

np.random.seed(42)
df['peso'] = df.get('peso', np.random.randint(1, 30, len(df)))

df['diagnostico'] = df['diagnostico'].fillna('Sano')

stats = df.groupby('especie')[['edad', 'peso']].agg(['mean', 'median', 'std'])
display(stats)

display(df['diagnostico'].value_counts().rename("Frecuencia"))

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.boxplot(data=df, x='especie', y='edad', ax=axes[0])
axes[0].set_title('Edad por especie')
sns.boxplot(data=df, x='especie', y='peso', ax=axes[1])
axes[1].set_title('Peso por especie')
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(data=df, y='diagnostico', order=df['diagnostico'].value_counts().index)
plt.title('Frecuencia de diagnósticos')
plt.xlabel('Cantidad de casos')
plt.show()

df = pd.get_dummies(df, columns=['especie'], drop_first=True, dtype=int)

cols_especie = [col for col in df.columns if col.startswith('especie_')]
X = df[['edad'] + cols_especie]
y = df['peso']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

modelo = LinearRegression().fit(X_train, y_train)
y_pred = modelo.predict(X_test)

r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"R²: {r2:.2f} | MSE: {mse:.2f}")

coef_df = pd.DataFrame({
    'Variable': X.columns,
    'Coeficiente': modelo.coef_.round(2)
})
display(coef_df.style.set_caption("Coeficientes del modelo"))

plt.figure(figsize=(6, 4))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.title('Peso real vs Predicho')
plt.xlabel('Peso real')
plt.ylabel('Peso predicho')
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

#datos ficticios: horas de estudio y notas obtenidas

horas = np.array([1, 2, 3, 4, 5, 6, 7, 8])
notas = np.array([2.0, 2.5, 3.0, 3.5, 4.2, 5.0, 5.8, 6.5])

#grafico scatter de datos reales

plt.scatter(horas, notas, color='blue', label='Datos reales')
plt.xlabel('Horas de estudio')
plt.ylabel('Notas')
plt.title('Relación entre horas de estudio y notas')
plt.legend()
plt.show()
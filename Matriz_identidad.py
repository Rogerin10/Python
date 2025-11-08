A = [
    [3, 8, 18],
    [4, 7, 2],
    [5, 15, 4]
]

# Obtener la dimensión de A
n = len(A)

# Crear la matriz identidad de tamaño n x n
I = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# Mostrar la matriz identidad
print("Matriz identidad de A:")
for fila in I:
    print(fila)

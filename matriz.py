a = [
    [3, 8, 18],
    [4, 7, 2],
    [5, 15, 4]
]


n = len(a)

identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

for fila in identidad:
    print(fila)

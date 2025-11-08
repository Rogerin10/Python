from fractions import Fraction

# Matriz A
A = [
    [3,  8, 18],
    [4,  7,  2],
    [5, 15,  4]
]

def det3x3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
          - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
          + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

def submatrix(M, i, j):
    # devuelve la submatriz 2x2 que resulta de quitar fila i y columna j
    return [ [row[col] for col in range(len(M)) if col != j]
             for r,row in enumerate(M) if r != i ]

def det2x2(M):
    return M[0][0]*M[1][1] - M[0][1]*M[1][0]

def cofactor_matrix(M):
    n = len(M)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sub = submatrix(M, i, j)            # 2x2
            C[i][j] = ((-1)**(i+j)) * det2x2(sub)
    return C

def transpose(M):
    n = len(M)
    return [[M[j][i] for j in range(n)] for i in range(n)]

def inverse_3x3(M):
    detM = det3x3(M)
    if detM == 0:
        raise ValueError("La matriz no tiene inversa (determinante = 0).")
    # matriz de cofactores
    C = cofactor_matrix(M)
    # adjunta = traspuesta de la matriz de cofactores
    adj = transpose(C)
    # inversa = adj / det
    # devolvemos fracciones exactas
    inv = [[Fraction(adj[i][j], detM) for j in range(3)] for i in range(3)]
    return inv

# calcular inversa y mostrar
invA = inverse_3x3(A)
print("Inversa de A (fracciones exactas):")
for fila in invA:
    print([str(x) for x in fila])

print("\nInversa de A (aprox. decimales):")
for fila in invA:
    print([float(x) for x in fila])

# comprobación A * invA = I (con tolerancia)
def matmul(X, Y):
    n = len(X)
    m = len(Y[0])
    p = len(Y)
    R = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            s = 0
            for k in range(p):
                s += X[i][k] * (Y[k][j] if not isinstance(Y[k][j], Fraction) else float(Y[k][j]))
            R[i][j] = s
    return R

res = matmul(A, [[float(x) for x in row] for row in invA])
print("\nA · A^{-1} (aprox.):")
for fila in res:
    print([round(x, 10) for x in fila])

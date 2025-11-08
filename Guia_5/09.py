def es_valida(lista):
     return sorted(lista) == list(range(1, 10))

def verificar_sudoku(matriz):
    # Verificar filas
    for fila in matriz:
        if not es_valida(fila):
            return "solucion invalida"

    # Verificar columnas
    for col in range(9):
        columna = [matriz[fila][col] for fila in range(9)]
        if not es_valida(columna):
            return "solucion invalida"

    # Verificar subcuadros 3x3
    for i in range(0, 9, 3):  # filas de subcuadros
        for j in range(0, 9, 3):  # columnas de subcuadros
            subcuadro = []
            for x in range(3):
                for y in range(3):
                    subcuadro.append(matriz[i + x][j + y])
            if not es_valida(subcuadro):
                return "solucion invalida"

    return "solucion valida"

sudoku_correcto = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]

print(verificar_sudoku(sudoku_correcto))
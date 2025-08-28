# Programa que pida al usuario ingresar notas de estudiantes una por una. 
# El ingreso termina cuando el usuario escriba el número -1. 
# El programa debe calcular y mostrar el promedio de todas las notas ingresadas. 
# Se debe validar que la cantidad de notas sea mayor a cero antes de calcular el promedio.

notas = []
while True:
    try:
        nota = float(input("Ingrese una nota (o -1 para terminar): "))
        if nota == -1:
            break
        elif 0 <= nota <= 7:  # rango típico de notas (puedes ajustarlo si quieres)
            notas.append(nota)
        else:
            print("Ingrese una nota válida (entre 0 y 7).")
    except ValueError:
        print("Entrada inválida. Debe ser un número.")

if len(notas) > 0:
    promedio = sum(notas) / len(notas)
    print(f"El promedio de las {len(notas)} notas ingresadas es: {promedio:.2f}")
else:
    print("No se ingresaron notas válidas, no se puede calcular el promedio.")

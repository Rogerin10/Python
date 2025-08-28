numero = int(input("Ingresa un número entero positivo: "))

if numero < 2:
    print("No hay números pares en el rango.")
else:
    print(f"Números pares desde 2 hasta {numero}:")
    for i in range(2, numero + 1, 2):
        print(i)

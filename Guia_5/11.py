while True:
    n = int(input("Ingrese un numero entero positivo: "))
    if n > 0:
        break
    print("El numero debe ser mayor que 0. Intente nuevamente.")

suma = n * (n + 1) // 2  

print(f"\nLa suma de todos los numeros enteros desde 1 hasta {n} es: {suma}")

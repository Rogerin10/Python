def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True

while True:
    limite = int(input("Ingrese un numero entero mayor que 1: "))
    if limite > 1:
        break
    print("El número debe ser mayor que 1. Intente nuevamente.")

print(f"\nNumeros primos entre 2 y {limite}:")
for num in range(2, limite + 1):
    if es_primo(num):
        print(num, end=" ")  # en una sola línea

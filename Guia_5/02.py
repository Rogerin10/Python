n = 0
while n <= 0:
    n = int(input("Ingresa un número positivo para encontrar sus múltiplos de 3: "))
    if n <= 0:
        print("Por favor, ingresa un número positivo mayor que 0.")

print(f"Los múltiplos de 3 hasta {n} son:")
for i in range(3, n + 1, 3):
    print(i)
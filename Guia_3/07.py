print("Ingresa 7 números enteros:")

num1 = int(input("Número 1: "))
maximo = num1
repeticiones = 1

num2 = int(input("Número 2: "))
if num2 > maximo:
    maximo = num2
    repeticiones = 1
elif num2 == maximo:
    repeticiones += 1

num3 = int(input("Número 3: "))
if num3 > maximo:
    maximo = num3
    repeticiones = 1
elif num3 == maximo:
    repeticiones += 1

num4 = int(input("Número 4: "))
if num4 > maximo:
    maximo = num4
    repeticiones = 1
elif num4 == maximo:
    repeticiones += 1

num5 = int(input("Número 5: "))
if num5 > maximo:
    maximo = num5
    repeticiones = 1
elif num5 == maximo:
    repeticiones += 1

num6 = int(input("Número 6: "))
if num6 > maximo:
    maximo = num6
    repeticiones = 1
elif num6 == maximo:
    repeticiones += 1

num7 = int(input("Número 7: "))
if num7 > maximo:
    maximo = num7
    repeticiones = 1
elif num7 == maximo:
    repeticiones += 1

print(f"\nEl número mayor es: {maximo}")
if repeticiones > 1:
    print(f"Hay empate: el número {maximo} se repite {repeticiones} veces.")
else:
    print("No hay empate.")

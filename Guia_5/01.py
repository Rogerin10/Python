num = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num > num2:
    print(f"El numero {num} es mayor que {num2}")
elif num < num2:
    print(f"El numero {num2} es mayor que {num}")
else:
    print(f"Los numeros {num} y {num2} son iguales")


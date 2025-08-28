saldo = 100.0

while True:
    print("\n1. Ver saldo")
    print("2. Retirar dinero")
    print("3. Salir")

    opcion = input("Opcion: ")

    if opcion == "1":
        print("Saldo actual: $", saldo)

    elif opcion == "2":
        cantidad = float(input("Cantidad a retirar: "))
        if cantidad > 0 and cantidad <= saldo:
            saldo -= cantidad
            print("Retiro exitoso de $", cantidad)
            print("Saldo restante: $", saldo)
        else:
            print("No se puede retirar esa cantidad. (cantidad maxima disponible  100.000) ")

    elif opcion == "3":
        print("Programa finalizado")
        break

    else:
        print("Opcion inválida.")

# Una empresa desea implementar como funcionaria un sistema de cajero automático, 
# para ello debe simular que se ingresa una tarjeta de banco pero luego de ello 
# se debe consultar cuál es su usuario y contraseña, para este caso existen 3 usuarios 
# distintos con distintas contraseñas cada uno, el usuario A tiene un monto de $50000, 
# el usuario B tiene un monto de $120000, y el usuario C tiene un monto de $700000. 
# Los usuarios A y B pueden retirar si desean todo su dinero en una sola transacción, 
# pero como el usuario C es un cliente especial, solo puede retirar sobre los $400000 
# si ingresa su “contraseña secreta”, por lo cual al momento de superar dicha cantidad 
# se debe de solicitar, si no se cumple no puede realizar la transacción. 
# Los usuarios solo pueden ingresar uno solo a la vez y el programa no puede terminar nunca, 
# solo los usuarios pueden salir y terminar sus tareas. 
# Recuerde que los usuarios pueden depositar, retirar y ver su saldo.

usuarios = {
    "A": {"password": "1234", "saldo": 50000},
    "B": {"password": "2345", "saldo": 120000},
    "C": {"password": "3456", "saldo": 700000, "clave_secreta": "9999"}
}

while True:
    print("\n--- Bienvenido al Cajero Automático ---")
    usuario = input("Ingrese su usuario (A, B o C) o 'salir' para terminar: ").upper()
    
    if usuario == "SALIR":
        print("Programa finalizado.")
        break
    
    if usuario not in usuarios:
        print("Usuario no válido.")
        continue

    password = input("Ingrese su contraseña: ")
    if password != usuarios[usuario]["password"]:
        print("Contraseña incorrecta.")
        continue
    
    # Menú de opciones
    while True:
        print(f"\nUsuario {usuario}, seleccione una opción:")
        print("1. Ver saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Cerrar sesión")
        opcion = input("Opción: ")
        
        if opcion == "1":
            print(f"Su saldo actual es: ${usuarios[usuario]['saldo']}")
        
        elif opcion == "2":
            try:
                monto = int(input("Ingrese el monto a depositar: "))
                if monto > 0:
                    usuarios[usuario]["saldo"] += monto
                    print(f"Depósito exitoso. Nuevo saldo: ${usuarios[usuario]['saldo']}")
                else:
                    print("Monto inválido.")
            except:
                print("Entrada inválida.")
        
        elif opcion == "3":
            try:
                monto = int(input("Ingrese el monto a retirar: "))
                if monto <= 0:
                    print("Monto inválido.")
                elif monto > usuarios[usuario]["saldo"]:
                    print("Fondos insuficientes.")
                else:
                    if usuario == "C" and monto > 400000:
                        clave_secreta = input("Ingrese su contraseña secreta: ")
                        if clave_secreta != usuarios["C"]["clave_secreta"]:
                            print("Contraseña secreta incorrecta. Transacción cancelada.")
                            continue
                    usuarios[usuario]["saldo"] -= monto
                    print(f"Retiro exitoso. Nuevo saldo: ${usuarios[usuario]['saldo']}")
            except:
                print("Entrada inválida.")
        
        elif opcion == "4":
            print(f"Sesión cerrada para usuario {usuario}.")
            break
        else:
            print("Opción inválida.")

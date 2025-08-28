"""
Debe crear un programa en la cual simule el avance con un dado al estilo Mario Party,
el dado posee los números del 1 al 10, si saca un 7 tres veces seguidas gana un item especial (Champiñón) 
en la cual puede lanzar un dado especial 3 veces seguidas, si al lanzar el dado especial saca tres 7 seguidos
gana automáticamente el juego y debe mostrar un mensaje que diga "Eres una super estrella!!! Haz ganado!!!".
"""
print("Bienvenido al Mario Party!")

contador_7 = 0
champiñon = False

while True:
    input("Presiona Enter para lanzar el dado...")
    tiro = int(input("Ingresa el número del dado (1 al 10): "))
    print(f"Has sacado un {tiro}.")

    if tiro == 7:
        contador_7 += 1
        print(f"Llevas {contador_7} siete(s) seguidos.")

        if contador_7 == 3:
            print("Has ganado un Champiñón especial.")
            champiñon = True
            break
    else:
        contador_7 = 0

if champiñon:
    print("Activar el dado especial. (3 lanzamientos)")
    contador_7_especial = 0

    for i in range(3):
        input(f"Lanzamiento {i + 1} del dado especial. Presiona Enter...")
        tiro = int(input("Ingresa el número del dado (1 al 10): "))
        print(f"Has sacado un {tiro}.")

        if tiro == 7:
            contador_7_especial += 1
        else:
            break

    if contador_7_especial == 3:
        print("Eres una super estrella!!! Has ganado!!!")
    else:
        print("No has sacado tres 7 seguidos en el dado especial. Inténtalo de nuevo.")

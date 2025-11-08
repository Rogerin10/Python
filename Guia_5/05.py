import datetime

def mostrar_menu():
    """
    Muestra un menú de opciones y ejecuta la acción seleccionada por el usuario.
    """
    while True:
        print("\n--- Menú Principal ---")
        print("1. Mostrar saludo")
        print("2. Mostrar fecha y hora actual")
        print("3. Salir")

        opcion = input("Por favor, elige una opción (1, 2, o 3): ")

        if opcion == '1':
            print("\n¡Hola! Bienvenido al programa.")
        
        elif opcion == '2':
            ahora = datetime.datetime.now()
            fecha_hora_formateada = ahora.strftime("%d/%m/%Y %H:%M:%S")
            print(f"\nLa fecha y hora actual es: {fecha_hora_formateada}")

        elif opcion == '3':
            print("\n¡Hasta luego! Gracias por usar el programa.")
            break
        
        else:
            print("\nOpción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()

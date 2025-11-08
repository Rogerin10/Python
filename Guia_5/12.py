def celsius_a_fahrenheit(celsius):
    """Convierte una temperatura de Celsius a Fahrenheit."""
    return (celsius * 1.8) + 32

def fahrenheit_a_celsius(fahrenheit):
    """Convierte una temperatura de Fahrenheit a Celsius."""
    return (fahrenheit - 32) / 1.8

def obtener_temperatura():
    """Solicita al usuario una temperatura y la valida."""
    while True:
        try:
            return float(input("Ingresa la temperatura que quieres convertir: "))
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

def mostrar_menu():
    """Muestra el menú de opciones y maneja la lógica principal del programa."""
    while True:
        print("\n--- Menú de Conversión de Temperatura ---")
        print("1. Convertir de Celsius a Fahrenheit")
        print("2. Convertir de Fahrenheit a Celsius")
        print("3. Salir")
        
        opcion = input("Elige una opción (1, 2, o 3): ")

        if opcion == '1':
            temp_celsius = obtener_temperatura()
            temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
            print(f"-> {temp_celsius}°C equivale a {temp_fahrenheit:.2f}°F")
        
        elif opcion == '2':
            temp_fahrenheit = obtener_temperatura()
            temp_celsius = fahrenheit_a_celsius(temp_fahrenheit)
            print(f"-> {temp_fahrenheit}°F equivale a {temp_celsius:.2f}°C")

        elif opcion == '3':
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")
if __name__ == "__main__":
    mostrar_menu()

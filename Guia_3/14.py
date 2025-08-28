"""
Se desea crear un programa que simule el funcionamiento de un quiosco de autoservicio de un restaurante de comida rápida (como las máquinas de McDonald's)
El programa debe iniciar mostrando un menú principal con diferentes categorías de productos: 1) Hamburguesas, 2) Bebidas, 3) Postres, 4) Finalizar pedido. 
Dentro de cada categoría, debe mostrar diferentes opciones con sus respectivos precios. El usuario podrá elegir múltiples productos,
y cada elección se debe ir sumando a una boleta que llevará el total del pedido. Además, cada producto debe tener un tiempo estimado de preparación 
(por ejemplo, hamburguesa = 7 minutos, bebida = 1 minuto, postre = 3 minutos). El programa debe calcular el tiempo total de espera considerando todos los productos seleccionados.
Una vez que el cliente elija "Finalizar pedido",
el sistema debe mostrar la lista de productos seleccionados, el precio total a pagar, 
el tiempo estimado de preparación y un número de boleta generado automáticamente. Si el usuario intenta elegir un número fuera de las opciones válidas,
debe aparecer un mensaje de error. El programa debe repetir el proceso de selección hasta que el cliente decida finalizar. Este ejercicio debe resolverse 
mezclando estructuras de decisión (if, elif, else), estructuras de repetición (while o for). 
Se recomienda organizar el código de manera clara, con indentación correcta y comentarios explicativos.
"""

import random

# Menu con productos, precios y tiempos
menu = {
    "Hamburguesas": [
        ("Hamburguesa con Queso", 2500, 7),
        ("Big Burger", 3500, 7),
        ("Doble Carne", 4000, 7)
    ],
    "Bebidas": [
        ("Coca-Cola", 1200, 1),
        ("Sprite", 1200, 1),
        ("Agua", 800, 1)
    ],
    "Postres": [
        ("Helado", 1500, 3),
        ("Sundae", 2000, 3),
        ("Pie de manzana", 1800, 3)
    ]
}

# Variables para almacenar el pedido
productos_seleccionados = []
total_pedido = 0
tiempo_total = 0

# Menu principal y selección de productos

print("Bienvenido al quiosco de autoservicio del restaurante de comida rápida!")

while True:
    print("\n---MENU  PRINCIPAL---")
    print("1) Hamburguesas")
    print("2) Bebidas")
    print("3) Postres")
    print("4) Finalizar pedido")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        categoria = "Hamburguesas"
    elif opcion == '2':
        categoria = "Bebidas"
    elif opcion == '3':
        categoria = "Postres"
    elif opcion == '4':
        break
    else:
        print("Opción no válida. Intente de nuevo.")
        continue

# Mostrar productos de la categoría elegida
    print(f"\n--- {categoria} ---")
    for i, (producto, precio, tiempo) in enumerate(menu[categoria], start=1):
        print(f"{i}) {producto} - ${precio} ({tiempo} min)")

    seleccion = input(f"Seleccione un producto de {categoria} (1-{len(menu[categoria])}): ")

    if seleccion.isdigit() and 1 <= int(seleccion) <= len(menu[categoria]):
        index = int(seleccion) - 1
        producto, precio, tiempo = menu[categoria][index]
        productos_seleccionados.append((producto, precio, tiempo))
        total_pedido += precio
        tiempo_total += tiempo
        print(f"Producto agregado: {producto} - ${precio} ({tiempo} min)")
    else:
        print("Selección no válida. Intente de nuevo.")

# Mostrar boleta final
print("\n=== BOLETA FINAL ===")
if not productos_seleccionados:
    print("No seleccionó ningún producto.")
else:
    for prod, precio, tiempo in productos_seleccionados:
        print(f"- {prod} : ${precio} ({tiempo} min)")
    print(f"\nTotal a pagar: ${total_pedido}")
    print(f"Tiempo estimado: {tiempo_total} minutos")
    print(f"Número de boleta: {random.randint(1000,9999)}")

print("\nGracias por su compra. ¡Vuelva pronto!")

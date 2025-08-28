insuficiente = 0
suficiente = 0
notable = 0
sobresaliente = 0
fuera_de_rango = 0

while True:
    entrada = input("Ingresa la nota del alumno (o escribe 'fin' para terminar): ")
    if entrada.lower() == 'fin':
        break
    try:
        nota = float(entrada)
        if 0 <= nota < 4.0:
            print("Insuficiente")
            insuficiente += 1
        elif 4.0 <= nota <= 5.4:
            print("Suficiente")
            suficiente += 1
        elif 5.5 <= nota <= 6.4:
            print("Notable")
            notable += 1
        elif 6.5 <= nota <= 7.0:
            print("Sobresaliente")
            sobresaliente += 1
        else:
            print("Nota fuera de rango")
            fuera_de_rango += 1
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número o 'fin'.")

print("\nResumen de categorías:")
print(f"Insuficiente: {insuficiente}")
print(f"Suficiente: {suficiente}")
print(f"Notable: {notable}")
print(f"Sobresaliente: {sobresaliente}")
print(f"Fuera de rango: {fuera_de_rango}")

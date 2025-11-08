positivos = 0
negativos = 0

print("Ingrese números enteros (escriba 0 para terminar):")

while True:
    numero = int(input("Número: "))

    if numero == 0:
        break  # termina el ciclo

    if numero > 0:
        positivos += 1
    else:
        negativos += 1

# Mostrar resultados
print("\n--- Resultados ---")
if positivos > 0:
    print(f"Cantidad de números positivos: {positivos}")
else:
    print("No se ingresaron números positivos.")

if negativos > 0:
    print(f"Cantidad de números negativos: {negativos}")
else:
    print("No se ingresaron números negativos.")

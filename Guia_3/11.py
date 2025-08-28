print("Contador de vocales en una cadena")

palabra = input("Ingrese una cadena de texto: ").lower()
vocales = ['a', 'e', 'i', 'o', 'u']
frecuencias = {v: 0 for v in vocales}

for x in palabra:
    if x in frecuencias:
        frecuencias[x] += 1

total_vocales = sum(frecuencias.values())
print('Total vocales:', total_vocales)

if total_vocales > 0:
    vocal_mas_frecuente = max(frecuencias, key=frecuencias.get)
    print(f"La vocal que más se repite es: '{vocal_mas_frecuente}' con {frecuencias[vocal_mas_frecuente]} apariciones.")
else:
    print("No se encontraron vocales en el texto.")

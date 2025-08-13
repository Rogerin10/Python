# Pedimos la frase al usuario
frase = input("Ingresa una frase: ")

# Inicializamos un diccionario para contar las vocales
vocales = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}

# Recorremos cada letra de la frase
for letra in frase.lower():  # convertimos todo a minúsculas
    if letra in vocales:
        vocales[letra] += 1

# Mostramos los resultados
total_vocales = sum(vocales.values())
print(f"\nTotal de vocales: {total_vocales}")
for vocal, cantidad in vocales.items():
    print(f"{vocal}: {cantidad}")

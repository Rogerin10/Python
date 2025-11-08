def es_palindromo(texto):
    texto = texto.lower()
    return texto == texto[::-1]

palabra = input("Introduce una palabra: ")

if es_palindromo(palabra):
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")
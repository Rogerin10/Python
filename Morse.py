# Diccionario con el código Morse
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': '/'  # Para separar palabras
}

def texto_a_morse(texto):
    texto = texto.upper()  # Convertir a mayúsculas
    morse = []
    for letra in texto:
        if letra in MORSE_CODE:
            morse.append(MORSE_CODE[letra])
        else:
            morse.append('?')  # Símbolo para caracteres no reconocidos
    return ' '.join(morse)

# Ejemplo de uso
entrada = input("Ingrese el texto a convertir a Morse: ")
resultado = texto_a_morse(entrada)
print("Código Morse:", resultado)

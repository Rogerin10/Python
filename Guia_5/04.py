import re
from collections import Counter

def analizar_frecuencia_palabras(texto):
    texto_minusculas = texto.lower()
    palabras = re.findall(r'\b[a-záéíóúüñ]+\b', texto_minusculas)
    frecuencia_palabras = Counter(palabras)
    palabras_mas_comunes = frecuencia_palabras.most_common()
    if not palabras_mas_comunes:
        print("No se encontraron palabras en el texto.")
        return

    palabra_mas_repetida = palabras_mas_comunes[0]
    print(f"La palabra más repetida es: '{palabra_mas_repetida[0]}' (aparece {palabra_mas_repetida[1]} veces)")

    print("\n--- Top 5 de palabras más frecuentes ---")
    top_5 = palabras_mas_comunes[:5]
    for i, (palabra, frecuencia) in enumerate(top_5, 1):
        print(f"{i}. '{palabra}' - {frecuencia} veces")

texto_ejemplo = """
Python es un lenguaje de programación interpretado cuya filosofía hace hincapié 
en la legibilidad de su código. Se trata de un lenguaje de programación multiparadigma, 
ya que soporta orientación a objetos, programación imperativa y, en menor medida, 
programación funcional.
"""

analizar_frecuencia_palabras(texto_ejemplo)

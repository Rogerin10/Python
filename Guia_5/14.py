import string

def contar_letras(frase):
    """
    Cuenta las vocales y consonantes en una frase dada.
    """
    vocales_cont = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    consonantes_cont = {}
    
    consonantes = "bcdfghjklmnpqrstvwxyz"

    for letra in frase.lower():
        if letra in vocales_cont:
            vocales_cont[letra] += 1
        elif letra in consonantes:
            # Si la consonante no está en el diccionario, la inicializamos
            consonantes_cont[letra] = consonantes_cont.get(letra, 0) + 1

    # Mostramos los resultados para las vocales
    total_vocales = sum(vocales_cont.values())
    print(f"\n--- Resumen de Vocales ---")
    print(f"Total de vocales: {total_vocales}")
    for vocal, cantidad in vocales_cont.items():
        print(f"{vocal}: {cantidad}")

    total_consonantes = sum(consonantes_cont.values())
    print(f"\n--- Resumen de Consonantes ---")
    print(f"Total de consonantes: {total_consonantes}")
    for consonante, cantidad in sorted(consonantes_cont.items()):
        print(f"{consonante}: {cantidad}")


 
frase_usuario = input("Ingresa una frase: ")
contar_letras(frase_usuario)
# - escribir un programa que muestre por consola (print) los numeros del 1 al 100
#   (ambos incluidos y con un salto de linea entre cada impresion), sustituyendo lo siguiente:
# * Multiplos de 3 por la palabra "fizz".
# * Multiplos de 5 por la palabra "buzz".
# * Multiplos de 3 y de 5 a la vez por la palabra "fizzbuz".
#

def fizz_buzz():
    for i in range (1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:    
            print(i)

fizz_buzz()    
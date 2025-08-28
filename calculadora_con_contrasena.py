# Calculadora básica con 5 operaciones usando match

# Contraseña
CONTRASENA = "python123"
clave = input("Ingrese la contraseña: ")

if clave != CONTRASENA:
    print("Contraseña incorrecta. Acceso denegado.")
    exit()

print("\nAcceso concedido\n")

# Pedir datos
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /, **): ")

# Operaciones con match
match operacion:
    case "+":
        print("Resultado:", num1 + num2)
    case "-":
        print("Resultado:", num1 - num2)
    case "*":
        print("Resultado:", num1 * num2)
    case "/":
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("Error: División por cero")
    case "**":
        print("Resultado:", num1 ** num2)
    case _:
        print("Operación no válida")
# Fin del programa

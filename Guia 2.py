# Imprimir nombre y asignatura favorita
print("Mi nombre es usuario y mi asignatura favorita es Python")

# Definir variables con datos personales
nombre = "usuario"
edad = 0
ciudad = "aaa"

print(f"Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}.")


# Definir dos números
numero1 = 15
numero2 = 7

# Calcular e imprimir la suma
resultado = numero1 + numero2
print(f"La suma de {numero1} y {numero2} es {resultado}")


# Solicitar edad al usuario
edad = int(input("Ingrese su edad: "))

# Determinar categoría según edad
if edad < 18:
    print("Eres menor de edad")
elif 18 <= edad <= 59:
    print("Eres adulto")
else:
    print("Eres mayor de edad")

    # Definir variable nota
nota = 4.5

if nota >= 4.0:
    print("Aprobado")
elif 3.0 <= nota < 4.0:
    print("Examen")
else:
    print("Reprobado")

    # Definir número entero
numero = 7

# Determinar si es par o impar usando módulo
if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")


# Semaforo. Definir variable color
color = "verde"

if color == "rojo":
    print("Detente")
elif color == "amarillo":
    print("Precaución")
elif color == "verde":
    print("Avanza")
else:
    print("Color inválido")


# Definir nota
nota = 6.2

# Evaluar rango de nota
if 1.0 <= nota <= 3.9:
    print("Insuficiente")
elif 4.0 <= nota <= 5.4:
    print("Suficiente")
elif 5.5 <= nota <= 6.4:
    print("Bueno")
elif 6.5 <= nota <= 7.0:
    print("Excelente")
else:
    print("Nota fuera de rango")


# Contraseña predefinida
contrasena_correcta = "Clave123"
contrasena_usuario = "Clave123"  # Esta variable vendría predefinida

# Verificar contraseña
if contrasena_usuario == contrasena_correcta:
    print("Acceso concedido")
else:
    print("Acceso denegado")


# Definir tres números
a = 15
b = 8
c = 23

# Determinar el mayor
if a >= b and a >= c:
    mayor = a
elif b >= a and b >= c:
    mayor = b
else:
    mayor = c

print(f"El mayor número es {mayor}")


# Definir monto de compra
monto = 25000

# Aplicar descuento si corresponde
if monto > 20000:
    total = monto * 0.9  # 10% de descuento
else:
    total = monto

print(f"Total a pagar: ${total:.2f}")


# Definir temperatura
temperatura = 18

# Evaluar rango de temperatura
if temperatura < 10:
    print("Hace frío")
elif 10 <= temperatura <= 25:
    print("Clima agradable")
else:
    print("Hace calor")


# Solicitar promedio y asistencia
promedio = float(input("Ingrese su promedio (0-7): "))
asistencia = float(input("Ingrese su porcentaje de asistencia (0-100): "))

# Evaluar condiciones para beca
if promedio >= 6.0 and asistencia > 85:
    print("Beca otorgada")
else:
    print("Beca no otorgada")
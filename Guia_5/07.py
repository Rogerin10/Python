def mostrar_tabla_multiplicar():
 
  while True:
    try:
      numero = int(input("Ingrese un número entero: "))
      if numero <= 0:
        print("Por favor, ingrese un número entero positivo.")
        continue
      break
    except ValueError:
      print("Por favor, ingrese un número entero válido.")

  print(f"Tabla de multiplicar del {numero}:")
  for i in range(1, 13):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

mostrar_tabla_multiplicar()

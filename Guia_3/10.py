def convertir_temperatura():
    try:
        temperatura = float(input("Ingresa la temperatura: "))
        unidad = input("Ingresa la unidad de temperatura (C, F, K): ").upper()

        if unidad == "C":
            fahrenheit = (temperatura * 1.8) + 32
            kelvin = temperatura + 273.15
            print(f"{temperatura} °C equivale a {fahrenheit:.2f} °F y {kelvin:.2f} K")

        elif unidad == "F":
            celsius = (temperatura - 32) / 1.8
            kelvin = celsius + 273.15
            print(f"{temperatura} °F equivale a {celsius:.2f} °C y {kelvin:.2f} K")

        elif unidad == "K":
            celsius = temperatura - 273.15
            fahrenheit = (celsius * 1.8) + 32
            print(f"{temperatura} K equivale a {celsius:.2f} °C y {fahrenheit:.2f} °F")

        else:
            print("Unidad de temperatura no válida. Usa C, F o K.")

    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar un número para la temperatura.")

convertir_temperatura()

import random
import time

buses = ["🚌 1", "🚌 2", "🚌 3"]


posiciones = [0 for _ in buses]

META = 70
ganadores = []

print("¡Comienza la carrera de buses!\n")

while True:
    for i, bus in enumerate(buses):
         
        avance = random.randint(1, 6)
        posiciones[i] += avance

        pista = "-" * posiciones[i] + bus
        print(pista)

         
        if posiciones[i] >= META and bus not in ganadores:
            ganadores.append(bus)

    print("\n--- Fin de turno ---\n")
    time.sleep(0.5)  

    if ganadores:   
        break

if len(ganadores) == 1:
    print(f"El ganador es {ganadores[0]} ")
else:
    print(f"¡Empate! Los ganadores son: {', '.join(ganadores)}")

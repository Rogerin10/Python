import threading
import time
import random

# Lista de filósofos
filosofos = ["Platón", "Aristóteles", "Friedrich Nietzsche", "Immanuel Kant", "Sócrates"]
N = len(filosofos)

# Crear 5 palillos (Lock por cada palillo)
palillos = [threading.Lock() for _ in range(N)]

# Diccionario para estadísticas
estadisticas = {nombre: {"pensó": 0, "comió": 0, "se levantó": 0} for nombre in filosofos}

# ---------------------- Funciones ----------------------

def pensar(nombre):
    """El filósofo piensa y se registra estadística"""
    print(f"{nombre} está pensando...")
    estadisticas[nombre]["pensó"] += 1
    time.sleep(random.uniform(0.2, 0.5))

def comer(i, nombre):
    """El filósofo intenta comer si consigue ambos palillos (pares no vecinos => deberían lograrlo)"""
    izq = palillos[i]
    der = palillos[(i + 1) % N]

    # Intentar tomar ambos palillos sin bloqueo infinito
    if not izq.acquire(timeout=1):
        print(f"{nombre} no pudo tomar el palillo izquierdo y sigue pensando.")
        return
    try:
        if not der.acquire(timeout=1):
            print(f"{nombre} no pudo tomar el palillo derecho y sigue pensando.")
            return
        try:
            print(f"{nombre} está comiendo con palillos {i} y {(i + 1) % N}")
            estadisticas[nombre]["comió"] += 1
            time.sleep(random.uniform(0.4, 0.7))
            print(f"{nombre} terminó de comer.")
        finally:
            der.release()
    finally:
        izq.release()

def filosofo_ronda(i, nombre, puede_comer):
    """Filósofo participa en una ronda: o solo piensa o piensa y come"""
    pensar(nombre)
    if puede_comer:
        comer(i, nombre)

# ---------------------- Planificador justo y aleatorio ----------------------

def generar_pares_equilibrados(n, rondas, rng=None):
    """
    Genera una lista de pares (índices) por ronda:
    - Siempre dos filósofos NO vecinos (no comparten palillo).
    - Distribución equilibrada a lo largo de todas las rondas.
    - Aleatorio en el orden de los pares por ciclo.
     """
    if rng is None:
        rng = random

    base = [(k, (k + 2) % n) for k in range(n)]

    pares = []
    ciclos = rondas // n
    resto = rondas % n

    # Cada ciclo usa todos los pares una vez, pero en orden aleatorio
    for _ in range(ciclos):
        tmp = base[:]
        rng.shuffle(tmp)
        pares.extend(tmp)

    if resto:
        tmp = base[:]
        rng.shuffle(tmp)
        pares.extend(tmp[:resto])

    return pares  # len == rondas

# ---------------------- Programa ----------------------

def main():
    rondas = int(input("¿Cuántas rondas de comida quieres simular? "))

    # Plan de rondas: exactamente 2 no vecinos por ronda, aleatorio pero equilibrado
    plan = generar_pares_equilibrados(N, rondas)

    for r in range(1, rondas + 1):
        par = plan[r - 1]
        print(f"\n--- Ronda {r} | Comerán (índices): {par} => ({filosofos[par[0]]}, {filosofos[par[1]]}) ---")

        hilos = []
        for i in range(N):
            puede_comer = (i == par[0] or i == par[1])
            hilo = threading.Thread(target=filosofo_ronda, args=(i, filosofos[i], puede_comer))
            hilos.append(hilo)
            hilo.start()

        for h in hilos:
            h.join()

    # Todos los filósofos se levantan al final
    for nombre in filosofos:
        estadisticas[nombre]["se levantó"] += 1
        print(f"{nombre} se ha levantado de la mesa.")

    # Resumen final
    print("\nResumen Final Del Banquete")
    print(f"{'Filósofo':<20}{'Pensó':<10}{'Comió':<10}{'Se levantó':<12}")
    print("-" * 52)
    for nombre, datos in estadisticas.items():
        print(f"{nombre:<20}{datos['pensó']:<10}{datos['comió']:<10}{datos['se levantó']:<12}")

if __name__ == "__main__":
    main()


import random

# -1 si pierde el agente, 1 si gana y 0 si empata
def premio(tablero):
    ganador = 0
    # filas
    for i in range(3):
        if tablero[i*3] == tablero[i*3+1] and tablero[i*3+1] == tablero[i*3+2]:
            ganador = tablero[i*3]
            if ganador == 1:
                return 1
            elif ganador == 2:
                return -1
    # columnas
    for i in range(3):
        if tablero[i] == tablero[3+i] and tablero[3+i] == tablero[6+i]:
            ganador = tablero[i]
            if ganador == 1:
                return 1
            elif ganador == 2:
                return -1
    # diagonales
    if tablero[0] == tablero[4] and tablero[4] == tablero[8]:
        ganador = tablero[0]
        if ganador == 1:
            return 1
        elif ganador == 2:
            return -1
    if tablero[2] == tablero[4] and tablero[4] == tablero[6]:
        ganador = tablero[2]
        if ganador == 1:
            return 1
        elif ganador == 2:
            return -1
    return 0

# Dado el estado del tablero, devuelve un número.
def codigoHash(tablero):
    suma = 0
    for i in range(len(tablero)):
        suma += tablero[i] * (3**i)
    return suma

# Comprueba si el tablero está lleno
def tablero_lleno(tablero):
    ceros = 0
    for elem in tablero:
        if elem == 0:
            ceros += 1
    return (ceros == 0)

# Decide si un tablero es terminal
def es_terminal(tablero):
    if tablero_lleno(tablero):
        return True
    recompensa = premio(tablero)
    return (recompensa != 0)

# devuelve una lista de casillas disponibles
def casillasDisponibles(tablero):
    disponibles = []
    for i in range(len(tablero)):
        if tablero[i] == 0:
            disponibles.append(i)
    return disponibles

# Dado un estado (del tablero) y una acción, devuelve los sucesores
def sucesoresTab(tablero, accion):
    if es_terminal(tablero):
        return []
    sucs = []
    tablero[accion] = 1
    if es_terminal(tablero):
        sucs.append(tablero)
    else:
        disp = casillasDisponibles(tablero)
        for casilla in disp:
            newtab = tablero.copy()
            newtab[casilla] = 2
            sucs.append(newtab)
    return sucs

# Dado un estado (en número) devuelve el tablero correspondiente
def hashInverso(estado):
    tablero = []
    while estado > 0:
        tablero.append(estado % 3)
        estado = estado // 3
    while len(tablero) < 9:
        tablero.append(0)
    return tablero

# Dado un estado y una acción, devuelve sus sucesores
def sucesores(estado, accion):
    tablero = hashInverso(estado)
    sucs1 = sucesoresTab(tablero, accion)
    sucs2 = []
    for tab in sucs1:
        sucs2.append(codigoHash(tab))
    return sucs2

# Dado un estado, decide si es terminal
def es_terminal2(estado):
    return es_terminal(hashInverso(estado))

# Dado un estado, devuelve la recompensa
def recompensa(estado):
    return premio(hashInverso(estado))

# Devuelve las posibles acciones, dado un estado
def acciones(estado):
    return casillasDisponibles(hashInverso(estado))

# Devuelve una acción aleatoria, dado un estado
def accionRand(estado):
    ac = acciones(estado)
    indice = random.randint(0, len(ac)-1)
    return ac[indice]

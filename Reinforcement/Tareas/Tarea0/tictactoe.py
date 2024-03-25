
import random

# recibe un número y devuelve un caracter que representa una ficha
def ficha(nf):
    if nf == 0:
        return ' '
    elif nf == 1:
        return 'X'
    elif nf == 2:
        return 'O'
    else:
        return ''

def imprimeTablero(tablero):
    print(ficha(tablero[0]),'|',ficha(tablero[1]),'|',ficha(tablero[2]))
    print("---------")
    print(ficha(tablero[3]),'|',ficha(tablero[4]),'|',ficha(tablero[5]))
    print("---------")
    print(ficha(tablero[6]),'|',ficha(tablero[7]),'|',ficha(tablero[8]))

# Devuelve 1 si gana el círculo, -1 si gana la cruz o 0 si hay empate o no ha terminado.
def premio(tablero):
    ganador = 0
    # filas
    for i in range(3):
        if tablero[i*3] == tablero[i*3+1] and tablero[i*3+1] == tablero[i*3+2]:
            ganador = tablero[i*3]
    # columnas
    for i in range(3):
        if tablero[i] == tablero[3+i] and tablero[3+i] == tablero[6+i]:
            ganador = tablero[i]
    # diagonales
    if tablero[0] == tablero[4] and tablero[4] == tablero[8]:
        ganador = tablero[0]
    if tablero[2] == tablero[4] and tablero[4] == tablero[6]:
        ganador = tablero[2]
    
    if ganador == 1:
        return -1
    elif ganador == 2:
        return 1
    else:
        return 0

# devuelve una lista de casillas disponibles
def casillasDisponibles(tablero):
    disponibles = []
    for i in range(len(tablero)):
        if tablero[i] == 0:
            disponibles.append(i)
    return disponibles

# la acción será un número del 0 al 8 y el turno 1 o 2.
def step(tablero, action, turno, disponibles):
    terminado = 0
    premAct = 0
    if disponibles == []:
        terminado = 1
        premAct = premio(tablero)
    else:
        tablero[action] = turno
        premAct = premio(tablero)
        if premAct != 0 or len(disponibles) == 1:
            terminado = 1
    return (premAct, terminado)

# el agente realiza una jugada aleatoria
def tira(tablero):
    disp = casillasDisponibles(tablero)
    premio = 0
    terminado = 0
    if disp:
        indice = random.randint(0, len(disp)-1)
        casilla = disp[indice]
        print("Agente tira en posición", casilla)
        premio, terminado = step(tablero, casilla, 2, disp)
    return (premio, terminado)

def partida():
    tab1 = [0,0,0,0,0,0,0,0,0]
    print("Las posiciones del tablero son las siguientes")
    print('0 | 1 | 2')
    print('---------')
    print('3 | 4 | 5')
    print('---------')
    print('6 | 7 | 8')
    juegoTerm = 0
    ganador = 0
    while juegoTerm == 0:
        imprimeTablero(tab1)
        disp = casillasDisponibles(tab1)
        if disp == []:
            break
        # tira el jugador
        print('Seleccione una casilla para tirar:', disp)
        casilla = int(input())
        if not (casilla in disp):
            print("Posición no disponible")
            continue
        ganador, juegoTerm = step(tab1, casilla, 1, disp)
        if juegoTerm == 1:
            break
        # tira el agente
        ganador, juegoTerm = tira(tab1)
    print("Juego terminado")
    imprimeTablero(tab1)
    if ganador == 0:
        print("Empate")
    elif ganador == -1:
        print("Gana jugador X")
    else:
        print("Gana jugador O")
    return ganador
        
    
def main():
    # juega 10 veces
    recompensa = 0
    for i in range(10):
        recompensa += partida()
    print("Recompensa total:", recompensa)

main()

import random

## Clase que modela el juego del gato
class Gato:
    tablero = [0,0,0,0,0,0,0,0,0]

    def __init__(self):
        self.tablero == [0,0,0,0,0,0,0,0,0]
        
    # recibe un número y devuelve un caracter que representa una ficha
    def ficha(self, nf):
        if nf == 0:
            return ' '
        elif nf == 1:
            return 'X'
        elif nf == 2:
            return 'O'
        else:
            return ''

    def imprimeTablero(self):
        print(self.ficha(self.tablero[0]),'|',self.ficha(self.tablero[1]),'|',self.ficha(self.tablero[2]))
        print("---------")
        print(self.ficha(self.tablero[3]),'|',self.ficha(self.tablero[4]),'|',self.ficha(self.tablero[5]))
        print("---------")
        print(self.ficha(self.tablero[6]),'|',self.ficha(self.tablero[7]),'|',self.ficha(self.tablero[8]))

    # Devuelve 1 si gana el círculo, -1 si gana la cruz o 0 si hay empate o no ha terminado.
    def premio(self):
        ganador = 0
        # filas
        for i in range(3):
            if self.tablero[i*3] == self.tablero[i*3+1] and self.tablero[i*3+1] == self.tablero[i*3+2]:
                ganador = self.tablero[i*3]
                if ganador == 1:
                    return 1
                elif ganador == 2:
                    return -1
        # columnas
        for i in range(3):
            if self.tablero[i] == self.tablero[3+i] and self.tablero[3+i] == self.tablero[6+i]:
                ganador = self.tablero[i]
                if ganador == 1:
                    return 1
                elif ganador == 2:
                    return -1
        # diagonales
        if self.tablero[0] == self.tablero[4] and self.tablero[4] == self.tablero[8]:
            ganador = self.tablero[0]
            if ganador == 1:
                return 1
            elif ganador == 2:
                return -1
        if self.tablero[2] == self.tablero[4] and self.tablero[4] == self.tablero[6]:
            ganador = self.tablero[2]
            if ganador == 1:
                return 1
            elif ganador == 2:
                return -1
        return 0

    # devuelve una lista de casillas disponibles
    def casillasDisponibles(self):
        disponibles = []
        for i in range(len(self.tablero)):
            if self.tablero[i] == 0:
                disponibles.append(i)
        return disponibles
    
    # la acción será un número del 0 al 8
    def step(self, action, turno):
        terminado = 0
        premAct = 0
        disponibles = self.casillasDisponibles()
        if disponibles == []:
            terminado = 1
            premAct = self.premio()
        else:
            self.tablero[action] = turno
            premAct = self.premio()
            if premAct != 0 or len(disponibles) == 1:
                terminado = 1
        # devuelve: observación, recompensa y si el juego terminó o sigue.
        return (self.tablero, premAct, terminado)

    # El rival hace una tirada aleatoria
    def tiraRival(self):
        disp = self.casillasDisponibles()
        premio = 0
        terminado = 0
        observacion = self.tablero
        if disp:
            indice = random.randint(0, len(disp)-1)
            casilla = disp[indice]
            observacion, premio, terminado = self.step(casilla, 2)
        return (observacion, premio, terminado)

    # Dado el estado del tablero, devuelve un número.
    def codigoHash(self):
        suma = 0
        for i in range(len(self.tablero)):
            suma += self.tablero[i] * (3**i)
        return suma
    
    def reinicia(self):
        for i in range(len(self.tablero)):
            self.tablero[i] = 0

    def juegoTerminado(self):
        return (self.premio() != 0) or (self.casillasDisponibles() == [])

# fin de clase Gato

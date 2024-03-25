
import Gato
import csv

## Juega 10 veces dada una política
def partida(politica):
    recompensa_total = 0
    tablero = Gato.Gato()
    for i in range(10):
        turno = 1
        terminado = 0
        while terminado != 1:
            if turno == 1: #turno del agente
                s = tablero.codigoHash()
                observacion, reward, terminado = tablero.step(politica[s], turno)
                recompensa_total += reward
                turno = 2
            else: #turno del rival
                observacion, reward, terminado = tablero.tiraRival()
                recompensa_total += reward
                turno = 1
            tablero.imprimeTablero()
            print() #para imprimir un salto de línea
        print("Reinicio de juego")
        tablero.reinicia()
    return recompensa_total

def main():
    # Para este punto ya deberían existir los archivos en CSV
    print("Elija una política:\n1. Por iteración de política.\n2. Por iteración de valor.")
    opcion = input()
    if opcion == "1":
        archivo = open("politicaIP.csv")
    else:
        archivo = open("politicaIV.csv")
    politica = {}
    csv_reader = csv.reader(archivo, delimiter=",")
    for row in csv_reader:
        politica[int(row[0])] = int(row[1])
    rt = partida(politica)
    print("Recompensa total:", rt)

main()
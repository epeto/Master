
import math
import random

## Recibe un estado y una acción.
# Los casos son: 0, 1 o 2, dependiendo del número de paredes que le pueden estorbar.
# @return recompensa promedio.
def recompensa(estado, accion):
    caso = 0
    if estado == 15:
        return 0
    if estado == 5 or estado == 6 or estado == 9 or estado == 10:
        caso = 0
    if estado == 4 or estado == 8:
        if accion == 2:
            caso = 0
        else:
            caso = 1
    if estado == 1 or estado == 2:
        if accion == 1:
            caso = 0
        else:
            caso = 1
    if estado == 7 or estado == 11:
        if accion == 0:
            caso = 0
        else:
            caso = 1
    if estado == 13 or estado == 14:
        if accion == 3:
            caso = 0
        else:
            caso = 1
    if estado == 0:
        if accion == 0 or accion == 3:
            caso = 2
        else:
            caso = 1
    if estado == 3:
        if accion == 3 or accion == 2:
            caso = 2
        else:
            caso = 1
    if estado == 12:
        if accion == 0 or accion == 1:
            caso = 2
        else:
            caso = 1
    if caso == 0:
        return -1
    elif caso == 1:
        return -(2/3)
    else:
        return -(1/3)

## devuelve los posibles sucesores del estado, dada una acción.
def sucesores(estado, accion):
    if estado == 15:
        return []
    fila = estado // 4
    columna = estado % 4
    lista_sucs = []
    if accion == 0:
        lista_sucs.append((fila, columna-1))
        lista_sucs.append((fila-1, columna))
        lista_sucs.append((fila+1, columna))
    elif accion == 1:
        lista_sucs.append((fila, columna-1))
        lista_sucs.append((fila+1, columna))
        lista_sucs.append((fila, columna+1))
    elif accion == 2:
        lista_sucs.append((fila-1, columna))
        lista_sucs.append((fila, columna+1))
        lista_sucs.append((fila+1, columna))
    else:
        lista_sucs.append((fila, columna-1))
        lista_sucs.append((fila-1, columna))
        lista_sucs.append((fila, columna+1))
    lista_sucs2 = [] # misma lista pero los estados serán solo un número
    for elem in lista_sucs:
        if elem[0] < 0 or elem[1] < 0 or elem[0] >= 4 or elem[1] >= 4:
            lista_sucs2.append(estado)
        else:
            lista_sucs2.append(elem[0]*4 + elem[1])
    return lista_sucs2

## Evalúa una política
def policy_evaluation(politica, theta, gamma):
    V = [0 for i in range(16)]
    delta = theta+1 
    while delta > theta:
        delta = 0
        for s in range(15):
            v = V[s]
            sucs = sucesores(s, politica[s])
            prom_val = 0
            for sprima in sucs:
                prom_val += (1/3)*V[sprima]
            V[s] = recompensa(s, politica[s]) + gamma*prom_val
            delta = max(delta, math.fabs(v - V[s]))
    return V

## Mejora de política
# @return False si y sólo si la política cambió
def policy_improvement(politica, V, gamma):
    policy_stable = True
    for s in range(15): # itera sobre los estados
        old = politica[s]
        prom_val = 0
        sucs = sucesores(s, old)
        for sprima in sucs:
            prom_val += (1/3)*V[sprima]
        maximo = recompensa(s, old) + gamma*prom_val
        for a in range(4): # itera sobre las acciones
            sucs = sucesores(s, a)
            prom_val = 0
            sucs = sucesores(s, a)
            for sprima in sucs:
                prom_val += (1/3)*V[sprima]
            newval = recompensa(s, a) + gamma*prom_val
            if newval > maximo:
                maximo = newval
                politica[s] = a
        if politica[s] != old:
            policy_stable = False
    return policy_stable

## Algoritmo de iteración de política
# @return una tupla: (valores, política)
def policy_iteration(theta, gamma):
    # primero se generará una política aleatoria
    politica_actual = []
    for i in range(16):
        politica_actual.append(random.randint(0,3))
    politica_actual[15] = -1 # el estado final no tiene política
    estable = False # para verificar si se cambió la política
    while not estable:
        V = policy_evaluation(politica_actual, theta, gamma)
        estable = policy_improvement(politica_actual, V, gamma)
    return (V, politica_actual)

## Algoritmo de iteración de valor
# @return tupla: (valores, política)
def value_iteration(theta, gamma):
    # Primera parte: calcular V
    V = [0 for i in range(16)]
    delta = theta+1 
    while delta > theta:
        delta = 0
        for s in range(15):
            maximo = -10e10
            v = V[s]
            for a in range(4):
                sucs = sucesores(s, a)
                prom_val = 0
                for sprima in sucs:
                    prom_val += (1/3)*V[sprima]
                newval = recompensa(s, a) + gamma*prom_val
                if newval > maximo:
                    maximo = newval
            V[s] = maximo
            delta = max(delta, math.fabs(v - V[s]))
    
    # Segunda parte: encontrar la política
    politica = [0 for i in range(16)]
    politica[15] = -1
    for s in range(15):
        maximo = -10e10
        for a in range(4):
            sucs = sucesores(s, a)
            prom_val = 0
            for sprima in sucs:
                prom_val += (1/3)*V[sprima]
            newval = recompensa(s, a) + gamma*prom_val
            if newval > maximo:
                maximo = newval
                politica[s] = a
    return (V, politica)

## función principal
def main():
    print("Elija un algoritmo:\n1. Iteración de política\n2. Iteración de valor")
    eleccion = input()
    if eleccion == "1":
        valores, politica = policy_iteration(0.001, 1)
        archivoValores = open("valoresIP.csv", "w")
        for i in range(len(valores)):
            archivoValores.write(str(i)+","+str(valores[i])+"\n")
        archivoValores.close()
        
        archivoPolitica = open("politicaIP.csv", "w")
        for i in range(len(politica)):
            archivoPolitica.write(str(i)+","+str(politica[i])+"\n")
        archivoPolitica.close()
        print("Revisar archivos: valoresIP.csv y politicaIP.csv")
    else:
        valores, politica = value_iteration(0.001, 1)
        archivoValores = open("valoresIV.csv", "w")
        for i in range(len(valores)):
            archivoValores.write(str(i)+","+str(valores[i])+"\n")
        archivoValores.close()
        
        archivoPolitica = open("politicaIV.csv", "w")
        for i in range(len(politica)):
            archivoPolitica.write(str(i)+","+str(politica[i])+"\n")
        archivoPolitica.close()
        print("Revisar archivos: valoresIV.csv y politicaIV.csv")

main()

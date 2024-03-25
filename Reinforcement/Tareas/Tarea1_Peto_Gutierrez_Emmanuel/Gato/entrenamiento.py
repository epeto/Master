
import gato2
import math

#calcula la esperanza dado que se encuentra en un estado y se toma una acción
def esperanza(estado, accion, gamma, V):
    sucs = gato2.sucesores(estado, accion)
    proba = 1/len(sucs) # son equiprobables
    suma = 0
    for sp in sucs:
        suma += proba*(gato2.recompensa(sp) + gamma*V[sp])
    return suma

# Evaluación de política. Supone que el diccionario de valores ya existe.
def policy_evaluation(estados, politica, theta, gamma, V):
    delta = theta+1
    while delta > theta:
        delta = 0
        for s in estados:
            if not gato2.es_terminal2(s):
                v = V[s]
                V[s] = esperanza(s, politica[s], gamma, V)
                delta = max(delta, math.fabs(v - V[s]))

# Mejora de política
def policy_improvement(estados, politica, gamma, V):
    policy_stable = True
    for s in estados:
        if not gato2.es_terminal2(s):
            old = politica[s]
            maximo = -10e10
            acciones = gato2.acciones(s)
            for a in acciones:
                newval = esperanza(s, a, gamma, V)
                if newval > maximo:
                    maximo = newval
                    politica[s] = a
            if politica[s] != old:
                policy_stable = False
    return policy_stable

# Dado el conjunto de estados, genera una política aleatoria
def politica_aleatoria(estados):
    politica = {}
    for s in estados:
        if gato2.es_terminal2(s):
            politica[s] = -1
        else:
            politica[s] = gato2.accionRand(s)
    return politica

# inicializa todos los valores de los estados en 0
def inicia_valores(estados):
    valores = {}
    for s in estados:
        valores[s] = 0
    return valores

# Algoritmo de iteración de política
def policy_iteration(estados, theta, gamma):
    V = inicia_valores(estados)
    politica_actual = politica_aleatoria(estados)
    estable = False
    while not estable:
        policy_evaluation(estados, politica_actual, theta, gamma, V)
        estable = policy_improvement(estados, politica_actual, gamma, V)
    return (V, politica_actual)

## Algoritmo de iteración de valor
# @return tupla: (valores, política)
def value_iteration(estados, theta, gamma):
    V = inicia_valores(estados)
    # Primera parte: calcular V
    delta = theta+1
    while delta > theta:
        delta = 0
        for s in estados:
            if not gato2.es_terminal2(s):
                maximo = -10e10
                v = V[s]
                acciones = gato2.acciones(s)
                for a in acciones:
                    newval = esperanza(s, a, gamma, V)
                    if newval > maximo:
                        maximo = newval
                V[s] = maximo
                delta = max(delta, math.fabs(v-V[s]))
    # Segunda parte: encontrar la política
    politica = politica_aleatoria(estados)
    for s in estados:
        if not gato2.es_terminal2(s):
            maximo = -10e10
            acciones = gato2.acciones(s)
            for a in acciones:
                newval = esperanza(s, a, gamma, V)
                if newval > maximo:
                    maximo = newval
                    politica[s] = a
    return (V, politica)

## función principal
def main():
    # Primera parte: leer los estados
    archivo_estados = open("estados_ttt", "r")
    estados_str = archivo_estados.read().split(" ")
    estados = list(map(lambda x : int(x), estados_str))
    # Segunda parte: entrenamiento
    print("Elija un algoritmo:\n1. Iteración de política\n2. Iteración de valor")
    eleccion = input()
    if eleccion == "1":
        valores, politica = policy_iteration(estados, 0.001, 1)
        archivoValores = open("valoresIP.csv", "w")
        for i in estados:
            archivoValores.write(str(i)+","+str(valores[i])+"\n")
        archivoValores.close()
        
        archivoPolitica = open("politicaIP.csv", "w")
        for i in estados:
            archivoPolitica.write(str(i)+","+str(politica[i])+"\n")
        archivoPolitica.close()
        print("Revisar archivos: valoresIP.csv y politicaIP.csv")
    else:
        valores, politica = value_iteration(estados, 0.001, 1)
        archivoValores = open("valoresIV.csv", "w")
        for i in estados:
            archivoValores.write(str(i)+","+str(valores[i])+"\n")
        archivoValores.close()
        
        archivoPolitica = open("politicaIV.csv", "w")
        for i in estados:
            archivoPolitica.write(str(i)+","+str(politica[i])+"\n")
        archivoPolitica.close()
        print("Revisar archivos: valoresIV.csv y politicaIV.csv")

main()
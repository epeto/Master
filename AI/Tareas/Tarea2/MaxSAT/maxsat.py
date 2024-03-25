
import random

## Recibe las líneas del archivo y las separa en cláusulas.
## Una cláusula es una lista de números (negativos o positivos)
# @param lineas las líneas leídas en el archivo de entrada
# @return fórmulas en forma normal conjuntiva
def creaFNC(lineas):
    fnc = []
    linea0 = lineas[0].split()
    numVars = int(linea0[2])
    for i in range(1,len(lineas)):
        linea = lineas[i]
        clausula = []
        varsString = linea.split()
        for elem in varsString:
            if elem[0] != '0':
                clausula.append(int(elem))
        fnc.append(clausula)
    return (numVars, fnc)

## Genera individuo aleatorio. Un individuo será un arreglo de True y False que
## representa una asignación de estados a las variables.
# @param n tamaño del individuo
# @return individuo nuevo
def generaIndividuo(n):
    individuo = []
    for i in range(n):
        prob = random.random()
        individuo.append(prob < 0.5)
    return individuo

## Evalúa una cláusula dado un estado de las variables.
# @param clausula lista de números que representan una cláusula
# @param estado asignación de valores las variables
# @return verdadero si y sólo si la clausula es verdadera en ese estado
def evaluaClausula(clausula, estado):
    for literal in clausula:
        if literal > 0 :
            if estado[literal-1]:
                return True
        else:
            if not estado[-literal-1]:
                return True
    return False

## Calcula cuántas cláusulas se hacen verdaderas dado un conjunto de fórmulas 
## en fnc y dado un estado de las variables.
# @param formulas conjunto de fórmulas en fnc
# @param estado de las variables
def idoneidad(formulas, individuo):
    contador = 0
    for clausula in formulas:
        if evaluaClausula(clausula, individuo):
            contador += 1
    return contador

## Genera una mutación en un individuo
# @param individuo
def muta(individuo):
    indice = random.randint(0, len(individuo)-1)
    individuo[indice] = not individuo[indice]

## Selecciona a un individuo de forma aleatoria pero con cierta probabilidad.
# @param idoPrefija suma prefija de las idoneidades de cada individuo.
# @param poblacion conjunto de individuos
# @return individuo seleccionado
def selecciona(idoPrefija, poblacion):
    rn = random.randint(0, idoPrefija[len(idoPrefija)-1])
    for i in range(len(idoPrefija)):
        if rn < idoPrefija[i]:
            return poblacion[i]
    return poblacion[len(poblacion)-1]

## Toma dos padres y los cruza para generar un hijo
# @param padre1 primer padre
# @param padre2 segundo padre
# @return hijo resultante de la cruza de padre1 y padre2
def reproduce(padre1, padre2):
    rn = random.randint(0, len(padre1)-1)
    hijo = []
    for i in range(len(padre1)):
        if i < rn:
            hijo.append(padre1[i])
        else:
            hijo.append(padre2[i])
    return hijo

## Algoritmo evolutivo.
# @param maxIt número máximo de iteraciones
# @param formulas fórmulas en fnc
# @param numVars número total de variables en las fórmulas
# @return individuo con la mejor idoneidad después de maxIt generaciones
def evolutivo(maxIt, formulas, numVars):
    # primer paso: crear 10 individuos aleatorios
    poblacion = []
    for i in range(10):
        poblacion.append(generaIndividuo(numVars))
    # siguiente paso: reproducir los individuos ad infinitum.
    for i in range(maxIt):
        nuevaPoblacion = []
        for j in range(len(poblacion)):
            # calcular la idoneidad de cada individuo
            listaIdo = []
            for individuo in poblacion:
                listaIdo.append(idoneidad(formulas, individuo))
            # se calcula la suma prefija de las idoneidades
            for k in range(1, len(listaIdo)):
                listaIdo[k] += listaIdo[k-1]
            padre1 = selecciona(listaIdo, poblacion)
            padre2 = selecciona(listaIdo, poblacion)
            hijo = reproduce(padre1, padre2)
            # se muta con una probabilidad del 5%
            if random.random() < 0.05 :
                muta(hijo)
            nuevaPoblacion.append(hijo)
        poblacion.extend(nuevaPoblacion) # se agregan los nuevos individuos a la población total
        # se ordenan respecto a la idoneidad
        poblacion.sort(key=lambda x : idoneidad(formulas, x))
        mitad = len(poblacion) // 2
        #se tiran a la basura la mitad de los individuos con menor idoneidad
        for j in range(mitad):
            poblacion.pop(0)
    resultados = []
    for individuo in poblacion:
        resultados.append(idoneidad(formulas, individuo))
    maxClaus = -1
    imc = -1
    for i in range(len(resultados)):
        if resultados[i] > maxClaus:
            maxClaus = resultados[i]
            imc = i
    return (poblacion[imc], maxClaus)


# Método principal
print("Ingrese el nombre del archivo que contiene las cláusulas")
nombreArchivo = input()
print("Ingrese el número de iteraciones a realizar")
numIt = int(input())
archivo = open(nombreArchivo, "r")
lineas = archivo.readlines()
archivo.close()
nVars, formulas = creaFNC(lineas)
mejorIndividuo, ncv = evolutivo(numIt, formulas, nVars)
print("\nNúmero de cláusulas verdaderas bajo ese estado:", ncv)
print("Estado:")
for i in range(len(mejorIndividuo)):
    varprop = i+1
    if mejorIndividuo[i]:
        print(varprop, end=" ")
    else:
        print(-varprop, end=" ")
print("")


import math
import random

## Función logit con un vector x y otro vector theta.
def logit(x, theta):
    exponente = 0
    for i in range(len(x)):
        exponente += theta[i]*x[i]
    e2 = math.e ** exponente
    pix = e2/(1 + e2)
    return pix

## El resultado de la derivada parcial de J(theta) respecto a theta[indice].
# se evalúa con los valores de theta actuales.
# @param theta : vector theta
def derivadaParcial(theta, x, y, indice):
    suma = 0
    for i in range(len(x)):
        suma += x[i][indice] * (y[i] - logit(x[i], theta))
    return suma

## A cada vector x[i] le inserta un 1 al inicio.
def inserta1(x):
    for elem in x:
        elem.insert(0, 1)

## Aplicando el algoritmo de gradiente descendente se obtiene theta
def gradDesc(x, y, alfa, iteraciones):
    theta = []
    d = len(x[0]) # dimensión del espacio
    for i in range(d):
        promedio = 0
        for j in range(len(x)):
            promedio += x[j][i]
        promedio /= len(x)
        theta.append(10/promedio)
    for i in range(iteraciones):
        print(theta)
        thetaAnterior = theta.copy()
        for j in range(len(thetaAnterior)):
            theta[j] = theta[j] + alfa*derivadaParcial(thetaAnterior, x, y, j)
    return theta

## Lee un archivo y construye los vectores x y y.
def lee(nombreArchivo):
    archivo = open(nombreArchivo, "r")
    lineas = archivo.readlines()
    archivo.close()
    filas = []
    for linea in lineas:
        filas.append(linea.split(","))
    x = []
    y = []
    for fila in filas:
        vx = []
        for i in range(len(fila)-1):
            vx.append(int(fila[i]))
        x.append(vx)
        y.append(int(fila[len(fila)-1]))
    return (x, y)

## Construye theta
def main():
    x, y = lee("social70.csv")
    inserta1(x)
    theta = gradDesc(x, y, 0.001, 100)
    print(theta)

main()

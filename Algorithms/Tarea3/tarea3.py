
import math
import random

# Convolución por fuerza bruta
def convolucion(A, B):
    C = []
    tam = len(A) + len(B)
    for k in range(tam-1):
        C.append(0)
    for i in range(len(A)):
        for j in range(len(B)):
            k = i+j
            C[k] += A[i]*B[j]
    return C


# El problema de los físicos
def fuerza_particulas(Q, c):
    F = []
    n = len(Q)
    for i in range(n):
        F.append(0)
    for i in range(n):
        for j in range(n):
            if j<i:
                F[i] += ((c*Q[i]*Q[j]) / ((i-j)*(i-j)))
            elif j>i:
                F[i] -= ((c*Q[i]*Q[j]) / ((i-j)*(i-j)))
    return F


# El problema de los físicos, versión 2
def fuerza_particulas2(Q, c):
    F = []
    n = len(Q)
    for i in range(n):
        F.append(0)
    B = []
    for i in range(-n+1, n):
        if(i == 0):
            B.append(0)
        elif i<0:
            B.append(-c / (i*i))
        else:
            B.append(c / (i*i))
    rconv = convolucion(Q, B)
    for i in range(n):
        F[i] = Q[i]*rconv[i+n-1]
    return F

# Genera un conjunto de n puntos aleatorios con coordenadas entre -500 y 500.
def genera_puntos(n):
    lista = []
    for i in range(n):
        x = random.randint(-500, 500)
        y = random.randint(-500, 500)
        lista.append((x,y))
    return lista

# Problema de dominios de puntos por fuerza bruta.
def bf_dominio(P):
    conj = []
    for i in range(len(P)):
        p1 = P[i]
        dominado = False
        for j in range(len(P)):
            if i != j:
                p2 = P[j]
                if p2[0] > p1[0] and p2[1] > p1[1]:
                    dominado = True
        if not dominado:
            conj.append(p1)
    return conj

# Problema del dominio de puntos por estrategia "divide y vencerás"
def dominio_aux(P):
    if len(P) <= 1:
        return P
    I = [] #izquierdo
    D = [] #derecho
    mitad = len(P) // 2
    for i in range(len(P)):
        if i<mitad:
            I.append(P[i])
        else:
            D.append(P[i])
    ndI = dominio_aux(I) # los no dominados del lado izquierdo
    ndD = dominio_aux(D) # los no dominados del lado derecho
    rv = [] # return value
    pdmax = ndD[0] #punto máximo (en la entrada y) del lado derecho
    for elemDer in ndD:
        if pdmax[1] < elemDer[1]:
            pdmax = elemDer
    # De los puntos de la izquierda, agregar solo los que tengan una entrada 'y' más grande que pdmax
    for elemIzq in ndI:
        if elemIzq[1] > pdmax[1]:
            rv.append(elemIzq)
    # Agregar todos los puntos de la derecha al resultado
    rv.extend(ndD)
    return rv

def dv_dominio(P):
    P.sort(key=lambda p : p[0]) # ordenar respecto a x
    return dominio_aux(P)

lista_aleatoria = genera_puntos(100)
print("lista completa:")
print(lista_aleatoria)

print("\npuntos no dominados (fuerza bruta):")
fbdp = bf_dominio(lista_aleatoria)
fbdp.sort(key=lambda p : p[0])
print(fbdp)

print("\npuntos no dominados (divide y vencerás):")
dvdp = dv_dominio(lista_aleatoria)
dvdp.sort(key=lambda p : p[0])
print(dvdp)

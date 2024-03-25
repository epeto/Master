
# Calcula la recurrencia
# s(n) = 5s(n-1) + 4s(n-2) - 2s(n-3)
# en tiempo lineal
def secuencia1(n):
    lista = [0, 1, 2]
    i = 3
    while i <= n:
        s_n = 5*lista[i-1] + 4*lista[i-2] - 2*lista[i-3]
        lista.append(s_n)
        i += 1
    return lista[n]


#multiplicacion de matrices
def matMul(m1, m2):
    if len(m1[0]) != len(m2):
        return []
    filas1 = len(m1)
    columnas2 = len(m2[0])
    rangoK = len(m1[0])
    matRes = []
    for i in range(filas1):
        vector = []
        for j in range(columnas2):
            vector.append(0)
        matRes.append(vector)
    for i in range(filas1):
        for j in range(columnas2):
            for k in range(rangoK):
                producto = m1[i][k]*m2[k][j]
                matRes[i][j] += producto
    return matRes


# construye una matriz identidad, cuadrada, de lado x lado
def matriz_identidad(lado):
    matriz = []
    for i in range(lado):
        vector = []
        for j in range(lado):
            if j == i:
                vector.append(1)
            else:
                vector.append(0)
        matriz.append(vector)
    return matriz


# matriz elevada a la n-esima potencia en tiempo O(log(n))
def potMat(matriz, potencia):
    n = potencia
    if n == 0:
        return matriz_identidad(len(matriz))
    elif n%2 == 1:
        return matMul(matriz, potMat(matriz, n-1))
    else:
        matAux = potMat(matriz, n//2)
        return matMul(matAux, matAux)


# Calcula la recurrencia
# s(n) = 5s(n-1) + 4s(n-2) - 2s(n-3)
# en tiempo O(log(n))
def secuencia2(n):
    m = [[5,4,-2],
         [1,0,0],
         [0,1,0]]
    vc = [[2],
          [1],
          [0]]
    mat_n = potMat(m, n)
    vr = matMul(mat_n, vc)
    return vr[2][0]


#verificar si coinciden las dos funciones de secuencia
for i in range(11):
    rs1 = secuencia1(i)
    rs2 = secuencia2(i)
    emoji = ""
    if(rs1 == rs2):
        emoji = "✓"
    else:
        emoji = "✖"
    print("s1:", rs1, "==", rs2, ":s2", emoji)

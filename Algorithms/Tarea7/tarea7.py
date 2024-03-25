
def buildMat(n):
    if n <= 0:
        return []
    mat = []
    for i in range(n):
        vec = [-1 for j in range(n)]
        mat.append(vec)
    return mat

def buildMat2(n):
    if n <= 0:
        return []
    mat = []
    cadenaVacia = ""
    for i in range(n):
        vec = [cadenaVacia for j in range(n)]
        mat.append(vec)
    return mat

def longMaxPal(cadena, i, j, matriz):
    if matriz[i][j] == -1:
        if i>j:
            matriz[i][j] = 0
        elif i==j:
            matriz[i][j] = 1
        else:
            if cadena[i] == cadena[j]:
                matriz[i][j] = 2 + longMaxPal(cadena, i+1, j-1, matriz)
            else:
                v1 = longMaxPal(cadena, i+1, j, matriz)
                v2 = longMaxPal(cadena, i, j-1, matriz)
                matriz[i][j] = max(v1, v2)
    return matriz[i][j]

def longMaxPal2(cadena):
    n = len(cadena)
    matriz = buildMat(n)
    return longMaxPal(cadena, 0, n-1, matriz)

def longMPIt(cadena):
    n = len(cadena)
    matriz = buildMat(n)
    for i in range(n-1, -1, -1):
        for j in range(n):
            if i>j:
                matriz[i][j] = 0
            elif i==j:
                matriz[i][j] = 1
            else:
                if cadena[i] == cadena[j]:
                    matriz[i][j] = 2 + matriz[i+1][j-1]
                else:
                    v1 = matriz[i+1][j]
                    v2 = matriz[i][j-1]
                    matriz[i][j] = max(v1, v2)
    return matriz

def construyePML(cadena):
    matLongs = longMPIt(cadena)
    n = len(cadena)
    matCads = buildMat2(n)
    for i in range(n-1, -1, -1):
        for j in range(n):
            if i==j:
                matCads[i][j] = cadena[i]
            elif i<j:
                if cadena[i] == cadena[j]:
                    letra = cadena[i]
                    matCads[i][j] = letra + matCads[i+1][j-1] + letra
                else:
                    if matLongs[i+1][j] > matLongs[i][j-1]:
                        matCads[i][j] = matCads[i+1][j]
                    else:
                        matCads[i][j] = matCads[i][j-1]
    return matCads[0][n-1]

c1 = "underqualified" # se espera un 7
c2 = "turboventilator" # se espera un 7
c3 = "character" # se espera un 5

print(c1, construyePML(c1))
print(c2, construyePML(c2))
print(c3, construyePML(c3))


def maximaSub(S, L, i):
    if L[i] == 0:
        maxLon = 0
        for j in range(i):
            temp = maximaSub(S, L, j)
            if (temp > maxLon) and (S[j] < S[i]):
                maxLon = temp
        L[i] = maxLon + 1
    return L[i]

def scml(S):
    L = [0 for elem in S]
    L[0] = 1
    maximaSub(S, L, len(S)-1)
    print(L)
    return max(L)
    
def maximaSubIt(S, L):
    L[0] = 1
    for i in range(1, len(S)):
        maxLon = 0
        for j in range(i):
            temp = L[j]
            if (temp > maxLon) and (S[j] < S[i]):
                maxLon = temp
        L[i] = maxLon + 1

def scmlIt(S):
    L = [0 for elem in S]
    L[0] = 1
    maximaSubIt(S, L)
    return L

def construyeSCML(S):
    L = scmlIt(S)
    salida = []
    salida.append(S[0])
    longAct = 2
    for i in range(1, len(L)):
        if (L[i] == longAct-1) and (S[i] < salida[len(salida)-1]):
            salida[len(salida)-1] = S[i]
        elif (L[i] == longAct) and (S[i] > salida[len(salida)-1]):
            salida.append(S[i])
            longAct += 1
    return salida

sec1 = [4, 2, -1, 3, 2, 3]
sec2 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(construyeSCML(sec1))
print(construyeSCML(sec2))


# problema 3
def bailarin(F, B):
    pares = []
    for i in range(len(F)):
        pares.append((F[i], i))
    pares.sort(key=lambda p : p[0])
    B.sort()
    
    retVal = []
    for i in range(len(B)):
        retVal.append(0)
        
    for i in range(len(B)):
        retVal[pares[i][1]] = B[i]
    return retVal

# problema 2
def skeduling(intervalos):
    pares = []
    for elem in intervalos:
        pares.append((elem[0], 'i'))
        pares.append((elem[1], 'f'))
    pares.sort(key=lambda p : p[0])
    empalme = 0
    maxval = 0
    for par in pares:
        if par[1] == 'i':
            empalme += 1
        else:
            empalme -=1
        if empalme > maxval:
            maxval = empalme
    print(pares)
    return maxval

f1 = [1.3, 1, 4, 2.5]
b1 = [9, 5, 3, 8]
     
    #[54, 72, 90, 0, 3, 21, 81, 12, 30, 5]
f2 = [ 9, 10, 43, 1, 2,  6, 11,  5,  7, 2]
b2 = [90, 72, 54, 3, 21, 30, 81, 0, 12, 5]

horarios = [(1, 3), (2, 5), (6, 8), (9, 11), (10, 12)]
print(skeduling(horarios))

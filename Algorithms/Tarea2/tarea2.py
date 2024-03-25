
def gcd(a, b):
    a = abs(a)
    b = abs(b)
    x = max(a, b)
    y = min(a, b)
    while y != 0:
        temp = x
        x = y
        y = temp % y
    return x


def esPalindromo(A):
    i = 0
    f = len(A) - 1
    mitad = len(A) // 2
    while i < mitad:
        if A[i] != A[f]:
            return False
        i += 1
        f -= 1
    return True


def fibo(n):
    lista = []
    for i in range(n):
        lista.append(0)
    if n<2:
        return n
    lista[0] = 0
    lista[1] = 1
    for i in range(2, n):
        lista[i] = lista[i-1] + lista[i-2]
    return lista


def bbRec(A, x, izq, der):
    if izq > der:
        return -1
    mitad = (izq+der) // 2
    if A[mitad] == x:
        return mitad
    elif x < A[mitad]:
        return bbRec(A, x, izq, mitad-1)
    else:
        return bbRec(A, x, mitad+1, der)

def busquedaBinaria(A, x):
    return bbRec(A, x, 0, len(A)-1)


def busquedaBinariaIterativa(A, x):
    izq = 0
    der = len(A) - 1
    encontrado = False
    mitad = 0
    while (izq <= der) and (not encontrado):
        mitad = (izq+der) // 2
        if A[mitad] == x:
            encontrado = True
        elif x < A[mitad]:
            der = mitad-1
        else:
            izq = mitad+1
    if A[mitad] == x:
        return mitad
    else:
        return -1

sucesion = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

for elem in sucesion:
    print(busquedaBinaria(sucesion, elem))



map_acc = {'A':0, 'B':1}

# s: estado
# a: acción
def sucesores(s, a):
    if s == 0:
        return []
    elif s == 1:
        if a == 'A':
            return [(0, 0.95), (2, 0.05)]
        else:
            return []
    elif s == 2:
        if a == 'A':
            return [(1, 0.95), (3, 0.05)]
        else:
            return [(0, 0.9), (3, 0.1)]
    elif s == 3:
        if a == 'A':
            return [(2, 0.95), (4, 0.05)]
        else:
            return [(1, 0.9), (4, 0.1)]
    else:
        return []

def recompensa(s):
    if s == 0:
        return -100
    elif s == 4:
        return 100
    else:
        return 0

def esperanza(s, a, V):
    sucs = sucesores(s, a)
    esp = 0
    for par in sucs:
        s_prima = par[0]
        proba = par[1]
        esp += proba*(recompensa(s_prima) + V[s_prima])
    return esp
    
def max_a(s, V):
    expected = [0, 0]
    if s == 1:
        return esperanza(s, 'A', V)
    else:
        expected[0] = esperanza(s, 'A', V)
        expected[1] = esperanza(s, 'B', V)
    return max(expected)

def iteracion_valor(it):
    V = [0, 0, 0, 0, 0]
    print(V)
    for i in range(it):
        for s in range(1,4):
            V[s] = max_a(s, V)
        print(V)
    return V

def calcula_politica():
    V = iteracion_valor(10)
    a = [esperanza(s, 'A', V) for s in range(1,4)]
    b = [esperanza(s, 'B', V) for s in range(1,4)]
    print('A', a)
    print('B', b)
    
calcula_politica()

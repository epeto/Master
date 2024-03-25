
import numpy as np
import random

def epsilon_greedy(s, epsilon, Q):
    maximal = max(Q[s])
    args_max = []
    args_totales = [0, 1, 2]
    for a in range(3):
        if maximal == Q[s][a]:
            args_max.append(a)
    rn = random.random()
    if rn < epsilon: # en este caso se devuelve una política aleatoria
        for elem in args_max:
            args_totales.remove(elem)
        if len(args_totales) > 0:
            return random.choice(args_totales)
        else:
            return min(args_max)
    else:
        return min(args_max)


def algoritmo(alfa, epsilon, gamma):
    Q = np.full((3,3), 0, dtype = float)
    print(Q)
    for i in range(100):
        s = random.randint(0,2)
        for j in range(100):
            a = epsilon_greedy(s, epsilon, Q)
            r = float(a+1)
            s_prima = a
            Q[s][a] = Q[s][a] + alfa*(r + gamma*max(Q[s_prima]) - Q[s][a])
            s = s_prima
    return Q

def algoritmo2(alfa, epsilon, gamma):
    Q = np.full((3,3), 6, dtype = float)
    print(Q)
    episodio = [0, 0, 1]
    recompensa = [1.0, 2.0]
    for i in range(2):
        s = episodio[i]
        a = s
        r = recompensa[i]
        s_prima = episodio[i+1]
        Q[s][a] = Q[s][a] + alfa*(r + gamma*max(Q[s_prima]) - Q[s][a])
        print(Q)
    return Q

q = algoritmo2(0.5, 0.2, 0.5)


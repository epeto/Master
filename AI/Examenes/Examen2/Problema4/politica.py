
import math

def distancia(x1, y1, x2, y2):
    dx = math.fabs(x1 - x2)
    dy = math.fabs(y1 - y2)
    return dx + dy
    
def main():
    c1 = (0, 0)
    c2 = (0, 2)
    r1 = 3
    r2 = 10
    gamma = 0.99
    
    matriz = []
    for i in range(3):
        vector = []
        for j in range(3):
            d1 = distancia(c1[0], c1[1], i, j)
            d2 = distancia(c2[0], c2[1], i, j)
            if d1 == 0 or d2 == 0:
                vector.append((0, 0))
            else:
                fst = (-1)*d1 + (gamma**d1)*r1
                snd = (-1)*d2 + (gamma**d2)*r2
                vector.append((fst, snd))
        matriz.append(vector)
    
    for fila in matriz:
        print(fila)

main()

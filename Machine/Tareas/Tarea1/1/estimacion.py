
import math

def avg(lista):
    suma = 0
    for elem in lista:
        suma += elem
    return suma/len(lista)

def varianza(lista, mu):
    suma = 0
    for x in lista:
        suma += (x - mu)**2
    return suma/len(lista)

def normal(x, mu, sigma):
    izq = 1/math.sqrt(2*math.pi*(sigma**2))
    exponente = -(((x-mu)**2)/(2*(sigma**2)))
    der = math.e**exponente
    print(exponente,izq,der)
    return izq*der
    
def log_normal(x, mu, sigma):
    izq = -(1/2)*math.log(2*math.pi*(sigma**2))
    der = -(((x-mu)**2)/(2*(sigma**2)))
    return izq + der

def main1():
    masculino = [[5071, 4854, 7238, 7238, 2220, 9017, 9017],
                [1.72, 1.82, 1.80, 1.70, 1.73, 1.80, 1.80],
                [75.3, 81.6, 86.1, 77.1, 78.2, 74.8, 74.3]]
                
    femenino = [[5071, 7238, 2220, 9213, 4854, 4854],
                [1.50, 1.52, 1.62, 1.67, 1.65, 1.75],
                [50.5, 45.3, 61.2, 68.0, 58.9, 68.0]]

    mu_masc = {"nombre":6379.28, "estatura":1.7671, "peso":78.2}
    mu_fem = {"nombre":5575.0, "estatura": 1.618, "peso":58.65}

    sigma_masc = {"nombre":2290.59, "estatura":0.044948, "peso":3.9706}
    sigma_fem = {"nombre":2181.37, "estatura":0.08629, "peso":8.4266}

    xs = [(9213, 1.68, 65), (4854, 1.75, 80), (5071, 1.80, 79), (7238, 1.90, 85), (2220, 1.65, 70)]
    for x in xs:
        print(x)
        print("Masculino")
        lnnom_m = log_normal(x[0], mu_masc["nombre"], sigma_masc["nombre"])
        print("nombre", lnnom_m)
        lnest_m = log_normal(x[1], mu_masc["estatura"], sigma_masc["estatura"])
        print("estatura", lnest_m)
        lnpeso_m = log_normal(x[2], mu_masc["peso"], sigma_masc["peso"])
        print("peso", lnpeso_m)
        py_m = math.log(7/13)
        print("p(y=M)", py_m)
        suma_m = lnnom_m + lnest_m + lnpeso_m + py_m
        print("suma:", suma_m)

        print("Femenino")
        lnnom_f = log_normal(x[0], mu_fem["nombre"], sigma_fem["nombre"])
        print("nombre", lnnom_f)
        lnest_f = log_normal(x[1], mu_fem["estatura"], sigma_fem["estatura"])
        print("estatura", lnest_f)
        lnpeso_f = log_normal(x[2], mu_fem["peso"], sigma_fem["peso"])
        print("peso", lnpeso_f)
        py_f = math.log(6/13)
        print("p(y=F)", py_f)
        suma_f = lnnom_f + lnest_f + lnpeso_f + py_f
        print("suma:", suma_f)

def categorica_map(c, alfa, n):
    q = []
    K = len(c)
    suma_alfa = sum(alfa)
    for i in range(K):
        numerador = c[i] + alfa[i] - 1
        denominador = n + suma_alfa - K
        q.append(numerador/denominador)
    return q

# Estimación de la Mu de máximo a posteriori
def mu_map(x, mu_0, sigma_0, sigma):
    suma_x = sum(x)
    numerador = (sigma_0**2)*suma_x + (sigma**2)*mu_0
    denominador = (sigma_0**2)*len(x) + sigma**2
    return numerador/denominador

def main2():
    xs = [("rene", 1.68, 65), ("guadalupe", 1.75, 80), ("denis", 1.80, 79), ("alex", 1.90, 85), ("cris", 1.65, 70)]
    categorias = {"alex":1, "cris":3, "denis":3, "guadalupe":4, "juan": 5, "rene":6}
    q_m = [0.1578, 0.1052, 0.1052, 0.1052, 0.1578, 0.0526]
    q_f = [0.1052, 0.1052, 0.1052, 0.1578, 0.0526, 0.1052]
    
    mu_masc = {"estatura":1.767, "peso":78.995}
    mu_fem = {"estatura":1.616, "peso":60.073}

    sigma_masc = {"estatura":0.044721, "peso":3.9698}
    sigma_fem = {"estatura":0.086, "peso":8.426}
    
    for x in xs:
        print(x)
        print("Masculino")
        lnnom_m = math.log(q_m[categorias[x[0]]-1])
        print("nombre", lnnom_m)
        lnest_m = log_normal(x[1], mu_masc["estatura"], sigma_masc["estatura"])
        print("estatura", lnest_m)
        lnpeso_m = log_normal(x[2], mu_masc["peso"], sigma_masc["peso"])
        print("peso", lnpeso_m)
        py_m = math.log(7/13)
        print("p(y=M)", py_m)
        suma_m = lnnom_m + lnest_m + lnpeso_m + py_m
        print("suma:", suma_m)

        print("Femenino")
        lnnom_f = math.log(q_f[categorias[x[0]]-1])
        print("nombre", lnnom_f)
        lnest_f = log_normal(x[1], mu_fem["estatura"], sigma_fem["estatura"])
        print("estatura", lnest_f)
        lnpeso_f = log_normal(x[2], mu_fem["peso"], sigma_fem["peso"])
        print("peso", lnpeso_f)
        py_f = math.log(6/13)
        print("p(y=F)", py_f)
        suma_f = lnnom_f + lnest_f + lnpeso_f + py_f
        print("suma:", suma_f)

main2()


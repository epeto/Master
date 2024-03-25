

import random
import sympy as sym
from pybigparser import evaluator

## construye el vector gradiente.
# @param f: función simbólica (construida con sympy).
# @param simbolos: tupla de símbolos (variables de la función).
def construyeGradiente(f, simbolos):
    gradSym = []
    for i in range(len(simbolos)):
        gradSym.append(sym.diff(f, simbolos[i]))
    print("Vector gradiente:", gradSym)
    gradFun = []
    for expr in gradSym:
        gradFun.append(str(expr))
    return gradFun

## Algoritmo de gradiente descendente
# gradiente: Vector gradiente como una lista de strings
# variables: Variables de la función como una lista de strings
# alfa: valor de la constante alfa
# iteraciones: número de iteraciones a realizar en el algoritmo
def gradienteDescendente(gradiente, variables, alfa, iteraciones):
    vector = []
    grad2 = []
    for elem in gradiente:
        parser = evaluator.MathParser()
        parser.set_function(elem)
        grad2.append(parser)
    for i in range(len(variables)):
        vector.append(random.randint(-500, 500))
    # se imprime el vector para ver el punto inicial
    print("Punto inicial:", vector)
    for i in range(iteraciones):
        vectorNuevo = []
        for subFuncion in grad2:
            for j in range(len(variables)):
                subFuncion.add_sub(variables[j], vector[j])
            subFuncion.evaluate()
            vectorNuevo.append(subFuncion.value)
        for j in range(len(vectorNuevo)):
            vector[j] = vector[j] - alfa*vectorNuevo[j]
    return vector


variables = 'x y'
tupla = sym.symbols(variables)
funcion = tupla[0]**2+tupla[1]**2 # esta es la función f(x,y)=x²+y²
funcionLambda = sym.lambdify(tupla, funcion)
print("Función: f(x,y) =", funcion)
gradiente = construyeGradiente(funcion, tupla)
mejorVector = gradienteDescendente(gradiente, variables.split(" "), 0.001, 10000)
print("Mejor vector encontrado: (x, y):", mejorVector)
print("f(x, y) =", funcionLambda(mejorVector[0], mejorVector[1]))


# Problema de la mochila

Las instrucciones para compilar y ejecutar son las siguientes:
- Compilar: make compile
- Ejecutar: make run

Al ejecutar se pedirá que ingrese el nombre del archivo que contiene los datos de los elementos. En este caso deberá escribir:
ks_19_0
o
ks_10000_0

Después se le pedirá que ingrese el tiempo máximo de ejecución. ¿Por qué poner un límite en el tiempo de ejecución? Porque si lo dejaba ejecutando por mucho tiempo me marcaba un OutOfMemoryError. 

La búsqueda utiliza la estrategia de A* con la siguiente función:
f(x) = peso - valor
El peso y el valor son los totales en la mochila. Se eligió esta función porque se explora primero al nodo cuya f(x) es menor y se está buscando minimizar el peso y maximizar el valor.

Se notará que el método toString de un elemento muestra lo siguiente:
(i: número de id, v: valor, p: peso)
El id de un elemento es el renglón en el que está en el archivo menos 2 (id = renglon-2).

La mochila siempre guarda una lista de los elementos que contiene actualmente. Si se encuentra un conjunto de elementos con un mejor valor que no supere la capacidad de la mochila, entonces se actualizan los datos de la mochila.

Al final se imprime el valor total de los elementos en la mochila, el peso total y la lista de elementos.


# Problema de las n reinas

El programa está hecho en C++ y se necesita el compilador g++.

- La instrucción para compilar es: make compile
- Para ejecutar: make run

Cuando se ejecuta se debe ingresar un número n que representa el número de reinas que se intentarán poner en un tablero de nxn. Después se debe ingresar un número que representa el tiempo máximo (en segundos) que se ejecutará el programa.

Se utiliza la estrategia de backtracking para tratar de encontrar una solución y se procede en orden. Cuando se encuentra una solución o se termina el tiempo de ejecución se imprime el vector resultante y se interpreta de la siguiente manera:
- Se supone que la reina en la casilla i está en la columna i. Es decir, la reina 0 está en la columna 0, la reina 1 en la columna 1 y así sucesivamente.
- El número en la casilla i representa la fila en la que se encuentra la reina. Ejemplo, si v es el vector y v(i) = j entonces la reina está en la columna i y la fila j.
- Si una casilla tiene -1 significa que no hay una reina en esa columna.

Después de imprimir el vector se muestra un tablero con emojis.


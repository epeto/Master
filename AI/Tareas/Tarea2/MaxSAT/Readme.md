
# Max SAT

- Para ejecutar: python3 maxsat.py

Se utiliza un algoritmo evolutivo para tratar de encontrar el estado que satisfaga la mayor cantidad de cláusulas en la fórmula que se da en forma normal conjuntiva.

El algoritmo tiene las siguientes características:
- La población empieza con 10 individuos.
- Se generan 10 hijos a partir de esos 10 padres.
- La población total ahora es de 20 pero se tiran a la basura la mitad de los individuos menos aptos.

Un individuo representa una asignación de valores a las variables. La función de idoneidad devuelve el número de cláusulas que se satisfacen con ese individuo. Los que satisfagan más cláusulas son los que sobreviven para la siguiente generación. Al final se selecciona al individuo más apto de la población.

El resultado se da como una lista de números, algunos positivos, otros negativos. Si un número i es positivo significa que la variable i tiene asignado el valor True. Si i es negativo entonces |i| tiene asignado el valor False. Así se determina el estado de todas las variables.


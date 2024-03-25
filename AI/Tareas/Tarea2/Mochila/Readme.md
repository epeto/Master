
# Problema de la mochila

- Compilar: make compile
- Ejecutar: make run

Para resolver este problema se usa la estrategia de ascensión de colinas. Inicialmente se tiene la mochila vacía. Los sucesores de una mochila actual son el resultado de agregar exactamente un elemento sin que se supere la capacidad. Como es un problema de optimización se elige al estado sucesor e que tenga el mínimo valor de la siguiente función:

f(e) = peso(e) - valor(e)

Si un estado tiene menos peso y mayor valor entonces f(e) será menor. Cuando se encuentra al estado mínimo, se actualiza el nodo actual (el agente se mueve hacia el estado mínimo) y se realiza la búsqueda otra vez.

El algoritmo termina cuando ya no se puede agregar ningún elemento a la mochila sin que se supere la capacidad.


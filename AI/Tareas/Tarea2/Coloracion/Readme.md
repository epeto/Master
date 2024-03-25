
# Coloración de gráficas

- Compilar: make compile
- Ejecutar: make run

Se utiliza la estrategia de recocido simulado para tratar de encontrar una coloración óptima para la gráfica. Se cumple que para cualquier estado (cualquier punto del algoritmo) se tiene una coloración consistente; es decir, una donde no hay dos vértices del mismo color que sean adyacentes.

Un sucesor resulta de cambiar el color de exactamente un vértice en la gráfica. Así, en el primer sucesor se cambia el color del primer vértice, en el segundo sucesor se cambia el color del segundo vértice y así sucesivamente. En cada iteración se tendrá una lista de n sucesores, donde n es el orden de la gráfica.

¿Cómo se elige el siguiente color de un vértice? La respuesta es: de forma aleatoria. Esto es por dos razones:
- 1) Si se prueban todos los colores para todos los vértices entonces se tendrán n^n sucesores en el peor caso y eso no es costeable en memoria ni en tiempo.
- 2) Si existe aleatoriedad al momento de elegir un estado siguiente entonces no debería haber problema con elegir un color de forma aleatoria (supongo).

La gráfica siempre empieza con n colores y a partir de ahí se trata de disminuir.

Sugerencia: En la gráfica de tamaño 1000 se generan 1000 sucesores en cada iteración, así que se recomienda no elegir números demasiado grandes para este ejemplar.

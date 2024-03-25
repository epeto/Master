
# Encontrar mínimo

- Compilar: make compile
- Ejecutar: make run

Se intenta encontrar el mínimo en las siguientes funciones:

- 1) 𝑓(𝑥_1,𝑥_2 )=𝑥_1^2+𝑥_2^2, −5≤𝑥_1,𝑥_2≤5
- 2) 𝑔(𝑥_1,𝑥_2) =(2)(418.9829) − 𝑥_1∗sin⁡(√|𝑥_1 |)  − 𝑥_2∗sin⁡(√|𝑥_2 |)),−500≤𝑥_1,𝑥_2≤500

Para ello se utiliza la estrategia de ascensión de colinas estocástica. Lo que quiere decir que se inicia con un punto aleatorio (x,y) y a partir de ahí se intenta mejorar (minimizar f(x,y)). La estrategia se repite varias veces hasta que se haya agotado el tiempo de ejecución y se devuelve el mínimo global.


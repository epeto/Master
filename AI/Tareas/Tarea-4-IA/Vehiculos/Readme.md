
# Predicción del valor de los vehículos

- Primero se transformaron los datos a números. Ejemplo, el nombre de la empresa se cambió por un número, dos autos de la misma empresa tienen el mismo número y no hay dos empresas con el mismo número.

- Luego se separaron los datos en datos70.csv y datos30.csv. El primero tiene un 70 % de los datos y el segundo un 30 %, y se seleccionaron aleatoriamente.

- Con el script regresion.py se hizo regresión polinomial con un polinomio de grado 3, usando datos70.csv como datos de entrenamiento.

- Después se hizo una comparación de los precios usando la predicción realizada por la regresión polinomial y el valor real, con los datos del archivo datos30.csv. El reporte de las diferencias de precios se encuentra en el archivo reporte.csv

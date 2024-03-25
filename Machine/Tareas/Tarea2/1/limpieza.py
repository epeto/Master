
## El primer paso es 'preprocesar' los datos de entrada:
# cambiar los signos de interrogación por datos reales.
# cambiar los datos de texto por números.

import csv
import random

# Recibe un archivo csv y devuelve las columnas que tengan al
# menos un signo de interrogación.
def col_interrogacion(csvfile):
    columnas_meta = []
    for row in csvfile:
        for i in range(len(row)):
            if row[i] == '?':
                if not (i in columnas_meta):
                    columnas_meta.append(i)
    return columnas_meta


# Devuelve el valor de una fila aleatoria, dada una columna.
def random_datum(csvfile, columna):
    encontrado = False
    nuevo_dato = ''
    while not encontrado:
        fila_ran = random.randint(0, len(csvfile)-1)
        nuevo_dato = csvfile[fila_ran][columna]
        if nuevo_dato != '?':
            encontrado = True
    return nuevo_dato

# Devuelve una lista con los elementos en esa columna, sin repeticiones.
def sinrep(dataset, columna):
    salida = []
    for fila in dataset:
        if not (fila[columna] in salida):
            salida.append(fila[columna])
    return salida

# Método principal
def main():
    archivo = open('imports-85.data')
    csvreader = csv.reader(archivo)
    salida = []
    for row in csvreader:
        salida.append(row.copy())
    ci = col_interrogacion(salida)
    archivo.close()
    # Se quitan los signos de interrogación
    for fila in range(len(salida)):
        for columna in ci:
            if salida[fila][columna] == '?':
                salida[fila][columna] = random_datum(salida, columna)
    col_str = [2, 3, 4, 6, 7, 8, 14, 17] # columnas con cadenas de caracteres
    # Se cambian los strings por números
    for columna in col_str:
        csr = sinrep(salida[1:], columna)
        for fila in range(1,len(salida)):
            indice = csr.index(salida[fila][columna])+1 # le sumo un 1 para evitar tener 0's en la matriz
            salida[fila][columna] = str(indice)
    # Ahora se tratan los casos particulares para el número de puertas
    # y número de cilindros
    numstr = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 
              'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'ten':'10',
              'eleven':'11', 'twelve':'12'}
    cilindros = [5, 15]
    for columna in cilindros:
        for fila in range(1,len(salida)):
            salida[fila][columna] = numstr[salida[fila][columna]]
    # Se escribe el archivo resultante
    archivo_salida = open('imports-85_v2.csv', 'w')
    csvwriter = csv.writer(archivo_salida)
    for fila in salida:
        csvwriter.writerow(fila)
    archivo_salida.close()

main()

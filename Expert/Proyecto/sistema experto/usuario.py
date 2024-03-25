

import pg
import random
import pandas as pd

# cierra la conexión con la base de datos
def cierra_conexion(conexion):
    conexion.close()


# crea una consulta de SQL para incluir los ingredientes de la lista
def consulta_incluye(lista_ings):
    salida = ''
    if len(lista_ings) == 1:
        salida = 'SELECT DISTINCT id_recipe FROM public.ingredients WHERE public.ingredients.ingredient LIKE \'%'+lista_ings[0]+'%\''
    elif len(lista_ings) > 1:
        for i in range(len(lista_ings)-1):
            salida += '(SELECT DISTINCT id_recipe FROM public.ingredients WHERE public.ingredients.ingredient LIKE \'%'+lista_ings[i]+'%\')\n'
            salida += 'INTERSECT\n'
        salida += '(SELECT DISTINCT id_recipe FROM public.ingredients WHERE public.ingredients.ingredient LIKE \'%'+lista_ings[len(lista_ings)-1]+'%\')'
    return salida


# crea una consulta que excluye los ingredientes de la lista
def consulta_excluye(lista_ings):
    salida = ''
    if len(lista_ings) == 1:
        salida = 'SELECT DISTINCT id_recipe FROM public.ingredients WHERE public.ingredients.ingredient NOT LIKE \'%'+lista_ings[0]+'%\''
    elif len(lista_ings) > 1:
        for i in range(len(lista_ings)-1):
            salida += '(SELECT DISTINCT id_recipe FROM public.ingredients WHERE public.ingredients.ingredient NOT LIKE \'%'+lista_ings[i]+'%\')\n'
            salida += 'INTERSECT\n'
        salida += '(SELECT DISTINCT id_recipe FROM public.ingredients WHERE public.ingredients.ingredient NOT LIKE \'%'+lista_ings[len(lista_ings)-1]+'%\')'
    return salida


## Crea una consulta con requerimientos nutricionales por cantidad.
def requerimientos_nutri(columna, elige_cantidad, cantidad = 0):
    salida = ''
    if elige_cantidad:
        salida = 'SELECT DISTINCT id_recipe FROM public.nutrition WHERE '+columna+' < '+str(cantidad)
    else: # si no se elige cantidad, simplemente se seleccionan los elementos menores a la media
        salida = 'SELECT DISTINCT id_recipe FROM public.nutrition WHERE '+columna+' < (SELECT AVG('+columna+') FROM public.nutrition)'
    return salida


## crea una consulta multi-requerimientos nutricionales
def nutri_multi(columnas, elige_cantidades, cantidades):
    lista_consultas = []
    for col, ec, cant in zip(columnas, elige_cantidades, cantidades):
        lista_consultas.append(requerimientos_nutri(col, ec, cant))
    salida = ''
    for i in range(len(lista_consultas) - 1):
        salida += '('+lista_consultas[i]+')\n'
        salida += 'INTERSECT\n'
    salida += '('+lista_consultas[len(lista_consultas) - 1]+')'
    return salida


## Crea una consulta donde la receta pertenezca a cierta categoría.
def requerimientos_categoria(categoria):
    return 'SELECT DISTINCT id_recipe FROM public.tags WHERE tag LIKE \'%'+categoria+'%\''


## cuando se eligen múltiples categorías
def categoria_multi(categorias):
    lista_consultas = []
    for cat in categorias:
        lista_consultas.append(requerimientos_categoria(cat))
    salida = ''
    for i in range(len(lista_consultas) - 1):
        salida += '('+lista_consultas[i]+')\n'
        salida += 'INTERSECT\n'
    
    salida += '('+lista_consultas[len(lista_consultas)-1]+')'
    return salida

## Dada una lista de consultas, las concatena en una sola.
def concatena_consulta(lista_query):
    salida = ""
    for i in range(len(lista_query)-1):
        salida += '(' + lista_query[i] + ')\nINTERSECT\n'
    salida += '(' + lista_query[len(lista_query)-1] + ')'
    return salida

#--------------------------------------------------------------------------------
# A partir de aquí se definen las consultas cuando ya se tienen guardados los ids de receta


## Dado el id de una receta, devuelve una consulta de los pasos, ordenados por id.
def pasos_idReceta(id_receta):
    salida = 'SELECT step\n'
    salida += 'FROM public.steps\n'
    salida += 'WHERE id_recipe = ' + str(id_receta) + '\n'
    salida += 'ORDER BY id'
    return salida


# Dado el id de una receta, devuelve sus ingredientes
def ingredients_idReceta(id_receta):
    salida = 'SELECT ingredient\n'
    salida += 'FROM public.ingredients\n'
    salida += 'WHERE id_recipe =' + str(id_receta)
    return salida


## Dada una lista de id's de receta, devuelve
def ingredients_listaRecetas(lista_idrec):
    salida = 'SELECT DISTINCT ingredient\n'
    salida += 'FROM public.ingredients\n'
    salida += 'WHERE '

    for i in range(len(lista_idrec) - 1):
        salida += 'id_recipe = ' + str(lista_idrec[i]) + ' OR '
    salida += 'id_recipe = ' + str(lista_idrec[len(lista_idrec) - 1])
    return salida


## Dada una lista de id's de receta, devuelve la tupla del id con el nombre
def nombres_recetas(lista_idrec):
    salida = 'SELECT id, name\n'
    salida += 'FROM public.recipes\n'
    salida += 'WHERE '
    for i in range(len(lista_idrec) - 1):
        salida += 'id = ' + str(lista_idrec[i]) + ' OR '
    salida += 'id = ' + str(lista_idrec[len(lista_idrec) - 1])
    return salida


## Se ejecuta la primera parte del sistema experto:
# hacer la consulta de recetas y guardar los id's en un archivo
def guarda_ids_recipes():
    lista_querys = [] # va a contener todas las consultas que se hagan
    
    print('¿Desea incluir ingredientes?\n1.-Sí\n2.-No')
    opcion = input()
    if opcion == '1':
        print('Ingrese la lista de ingredientes a incluir, separados solo por comas.')
        entrada = input()
        lii = entrada.split(',')
        lista_querys.append(consulta_incluye(lii))
    
    print('¿Desea excluir ingredientes?\n1.-Sí\n2.-No')
    opcion = input()
    if opcion == '1':
        print('Ingrese la lista de ingredientes a excluir, separados solo por comas.')
        entrada = input()
        lie = entrada.split(',')
        lista_querys.append(consulta_excluye(lie))
    
    print('¿Las recetas pertenecen a alguna categoría?\n1.-Sí\n2.-No')
    opcion = input()
    if opcion == '1':
        print('Ingrese las categorías, separadas solo por comas.')
        entrada = input()
        lcat = entrada.split(',')
        lista_querys.append(categoria_multi(lcat))

    print('¿Desea agregar requerimientos nutricionales?\n1.-Sí\n2.-No')
    opcion = input()
    if opcion == '1':
        print('Se pueden elegir recetas bajas en alguno de las siguientes componentes:')
        print('calories, total_fat, sugar, sodium, protein, saturated_fat, carbohydrates')
        print('Ingrese los componentes, separados por comas.')
        entrada = input()
        lcomp = entrada.split(',')
        condiciones = [False for _ in range(len(lcomp))]
        cantidades = [0 for _ in range(len(lcomp))]
        lista_querys.append(nutri_multi(lcomp, condiciones, cantidades))

    # Se ejecuta la consulta
    conexion = pg.DB(host="localhost", user="postgres", passwd="ZAPDOSRED7536589", dbname="SE_cocina")
    consulta = conexion.query(concatena_consulta(lista_querys)).getresult()
    lista_idings = [tupla[0] for tupla in consulta]
    f = open('query_id_recipes.csv', 'w')
    for i in range(len(lista_idings)-1):  
        f.write(str(lista_idings[i])+',')
    f.write(str(lista_idings[len(lista_idings) -1]))
    f.close()
    print('Recetas guardadas en archivo: query_id_recipes.csv')
    cierra_conexion(conexion)


## Función que hará un subarchivo de recetas dependiendo si elige:
# 1.- una receta
# 2.- recetas para el día
# 3.- plan semanal
def plan_recetas():
    file = open('query_id_recipes.csv', 'r')
    ids_str = file.read().split(',')
    ids = [int(identificador) for identificador in ids_str]
    query = nombres_recetas(ids)
    conexion = pg.DB(host="localhost", user="postgres", passwd="ZAPDOSRED7536589", dbname="SE_cocina")
    consulta = conexion.query(query).getresult()
    lista_recetas = [str(tupla[0]) + '|' + tupla[1] for tupla in consulta]
    print('Elija qué tipo de plan requiere:\n1.-Una receta\n2.-Recetas para el día\n3.-Plan semanal')
    opcion = input()
    if opcion == '1':
        muestra = random.sample(lista_recetas, 10) # se toman 10 recetas
        df = pd.DataFrame({'receta' : muestra})
        df.to_csv('query_una.csv', index=False)
        print('Lista de 10 recetas guardada en: query_una')
    elif opcion == '2':
        muestra = random.sample(lista_recetas, 9) # se toman 9 recetas
        diccionario = {'desayuno' : muestra[0:3], 'comida' : muestra[3:6], 'cena' : muestra[6:9]}
        df = pd.DataFrame(diccionario)
        df.to_csv('query_dia.csv', index=False)
        print('9 recetas guardadas en: query_dia.csv')
    else:
        muestra = random.sample(lista_recetas, 15) # se toman 15 recetas
        diccionario = {'lunes' : muestra[0:3], 'martes' : muestra[3:6], 'miercoles' : muestra[6:9], 'jueves' : muestra[9:12], 'viernes':muestra[12:15]}
        df = pd.DataFrame(diccionario)
        df.to_csv('query_semana.csv', index=False)
        print('15 recetas guardadas en: query_semana.csv')
    file.close()
    cierra_conexion(conexion)


## Dado que se tiene un plan, se observa con pandas y se elige una receta
#  para mostrar sus pasos e ingredientes
def ingres_pasos():
    print('Ingrese el plan que quiere consultar:\n1.-Una receta\n2.-Un día\n3.-Semanal')
    opcion = input()
    if opcion == '1':
        df = pd.read_csv('query_una.csv')
    elif opcion == '2':
        df = pd.read_csv('query_dia.csv')
    else:
        df = pd.read_csv('query_semana.csv')
    lista_ids = []
    for columna in df:
        for fila in df[columna]:
            id_rec = int(fila.split('|')[0])
            lista_ids.append(id_rec)
    print('El número a la izquierda es el id de la receta')
    print(df)
    print('Elija una acción:\n1.-Obtener lista completa de ingredientes\n2.-Mostrar ingredientes y pasos de una receta')
    opcion = input()
    if opcion == '1':
        conexion = pg.DB(host="localhost", user="postgres", passwd="ZAPDOSRED7536589", dbname="SE_cocina")
        consulta = conexion.query(ingredients_listaRecetas(lista_ids)).getresult()
        print('Lista de ingredientes:')
        for tupla in consulta:
            print(tupla[0])
        cierra_conexion(conexion)
    else:
        print('Ingrese el id de la receta que quiere obtener')
        idrec = int(input())
        conexion = pg.DB(host="localhost", user="postgres", passwd="ZAPDOSRED7536589", dbname="SE_cocina")
        consulta = conexion.query(ingredients_idReceta(idrec)).getresult()
        print('Lista de ingredientes:')
        for tupla in consulta:
            print(tupla[0])
        
        consulta = conexion.query(pasos_idReceta(idrec)).getresult()
        print('\nPasos a seguir:')
        for tupla in consulta:
            print(tupla[0])
        cierra_conexion(conexion)

# función principal
def main():
    print('Elija una acción:\n1.-Crear consulta\n2.-Crear plan\n3.-Consultar ingredientes y pasos de un plan')
    opcion = input()
    if opcion == '1':
        guarda_ids_recipes()
    elif opcion == '2':
        plan_recetas()
    else:
        ingres_pasos()


main()


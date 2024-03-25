
import pandas as pd


# Para reducir el archivo a tamaño 1000
def cortar_archivo():
    dataframe = pd.read_csv("RAW_recipes.csv")
    reduccion = dataframe[:1000]
    reduccion.to_csv('recipes_reducido.csv')
    

# quita caracteres especiales de una palabra
def trim_word(palabra):
    ind_ini = 0
    ind_fin = len(palabra) - 1
    while not palabra[ind_ini].isalnum():
        ind_ini += 1
    while not palabra[ind_fin].isalnum():
        ind_fin -= 1
    return palabra[ind_ini : ind_fin+1]
    

# construye la tabla (en csv) de los ingredientes
def construye_ingredientes():
    dataframe = pd.read_csv('recipes_reducido.csv')
    ids = dataframe['id']
    ingredientes = dataframe['ingredients']
    lista_idrec = [] # lista del id de la receta
    lista_ing = [] # lista de ingredientes
    for par in zip(ids, ingredientes):
        separacion = par[1].split(',')
        for inge in separacion:
            lista_idrec.append(par[0])
            lista_ing.append(trim_word(inge))
    df2 = pd.DataFrame({'ingredient': lista_ing, 'id_recipe': lista_idrec})
    df2.to_csv('ingredients.csv')


# construye la tabla de pasos (en csv)
def construye_pasos():
    dataframe = pd.read_csv('recipes_reducido.csv')
    ids = dataframe['id']
    pasos = dataframe['steps']
    lista_idrec = [] # lista del id de la receta
    lista_step = [] # lista de pasos
    for par in zip(ids, pasos):
        separacion = par[1].split(',')
        for paso in separacion:
            if len(paso) > 1:
                lista_idrec.append(par[0])
                lista_step.append(trim_word(paso))
    df2 = pd.DataFrame({'step': lista_step, 'id_recipe': lista_idrec})
    df2.to_csv('steps.csv')

# construye la tabla de etiquetas (en csv)
def construye_tags():
    dataframe = pd.read_csv('recipes_reducido.csv')
    ids = dataframe['id']
    tags = dataframe['tags']
    lista_idrec = [] # lista del id de la receta
    lista_tag = [] # lista de pasos
    for par in zip(ids, tags):
        separacion = par[1].split(',')
        for paso in separacion:
            if len(paso) > 1:
                lista_idrec.append(par[0])
                lista_tag.append(trim_word(paso))
    df2 = pd.DataFrame({'tag': lista_tag, 'id_recipe': lista_idrec})
    df2.to_csv('tags.csv')

def construye_nutrition():
    dataframe = pd.read_csv('recipes_reducido.csv')
    ids = dataframe['id']
    nuts = dataframe['nutrition']
    lista_idrec = []
    calories = []
    total_fat = []
    sugar = []
    sodium = []
    protein = []
    saturated_fat = []
    carbs = []
    for par in zip(ids, nuts):
        separacion = par[1].split(',')
        lista_idrec.append(par[0])
        calories.append(trim_word(separacion[0]))
        total_fat.append(trim_word(separacion[1]))
        sugar.append(trim_word(separacion[2]))
        sodium.append(trim_word(separacion[3]))
        protein.append(trim_word(separacion[4]))
        saturated_fat.append(trim_word(separacion[5]))
        carbs.append(trim_word(separacion[6]))
    df2 = pd.DataFrame({'calories':calories, 'total_fat':total_fat, 'sugar':sugar, 'sodium':sodium, 'protein':protein, 'saturated_fat':saturated_fat, 'carbohydrates':carbs, 'id_recipe': lista_idrec})
    df2.to_csv('nutrition.csv')

# reduce el número de columnas en recetas
def proyeccion():
    df = pd.read_csv('recipes_reducido.csv')
    df2 = pd.DataFrame({'id': df['id'], 'name':df['name'], 'minutes':df['minutes'], 'n_steps':df['n_steps'], 'description':df['description'], 'n_ingredients':df['n_ingredients']})
    df2.to_csv('recipes.csv')

# quita comillas simples y comillas dobles
def limpia_cadena(cadena):
    salida = ''
    for i in range(len(cadena)):
        if cadena[i] != '\'' and cadena[i] != '\"':
            salida += cadena[i]
    return salida

# crea archivo de insercion
def insercion_recipes():
    strsal = "INSERT INTO public.recipes(\n"
    strsal += "id, name, minutes, n_steps, description, n_ingredients)\n"
    strsal += 'VALUES\n'
    df = pd.read_csv('recipes.csv')
    for i in range(len(df)-1):
        fila = '('+str(df['id'][i])+', \''+limpia_cadena(df['name'][i])+'\', '+str(df['minutes'][i])+', '+str(df['n_steps'][i])+', \''+limpia_cadena(df['description'][i])+'\', '+str(df['n_ingredients'][i])+'),\n'
        strsal += fila
    ultimafila = '('+str(df['id'][len(df)-1])+', \''+limpia_cadena(df['name'][len(df)-1])+'\', '+str(df['minutes'][len(df)-1])+', '+str(df['n_steps'][len(df)-1])+', \''+limpia_cadena(df['description'][len(df)-1])+'\', '+str(df['n_ingredients'][len(df)-1])+');'
    strsal += ultimafila
    f = open("inserta_recipe.sql", "w")
    f.write(strsal)
    f.close()

# crea un archivo de nutrición
def insercion_nutrition():
    strsal = "INSERT INTO public.nutrition(\n"
    strsal += "id, calories, total_fat, sugar, sodium, protein, saturated_fat, carbohydrates, id_recipe)\n"
    strsal += "VALUES\n"
    df = pd.read_csv('nutrition.csv')
    for i in range(len(df)-1):
        fila = '('+str(df['id'][i])+', '+str(df['calories'][i])+', '+str(df['total_fat'][i])+', '+str(df['sugar'][i])+', '+str(df['sodium'][i])+', '+str(df['protein'][i])+', '+str(df['saturated_fat'][i])+', '+str(df['carbohydrates'][i])+', '+str(df['id_recipe'][i])+'),\n'
        strsal += fila
    ultimafila = '('+str(df['id'][len(df)-1])+', '+str(df['calories'][len(df)-1])+', '+str(df['total_fat'][len(df)-1])+', '+str(df['sugar'][len(df)-1])+', '+str(df['sodium'][len(df)-1])+', '+str(df['protein'][len(df)-1])+', '+str(df['saturated_fat'][len(df)-1])+', '+str(df['carbohydrates'][len(df)-1])+', '+str(df['id_recipe'][len(df)-1])+');'
    strsal += ultimafila
    f = open("inserta_nutrition.sql", "w")
    f.write(strsal)
    f.close()

# crea un archivo de inserción de ingredientes
def insercion_ingredients():
    strsal = 'INSERT INTO public.ingredients(\n'
    strsal += 'id, ingredient, id_recipe)\n'
    strsal += 'VALUES\n'
    df = pd.read_csv('ingredients.csv')
    for i in range(len(df)-1):
        fila = '('+str(df['id'][i])+', \''+limpia_cadena(df['ingredient'][i])+'\', '+str(df['id_recipe'][i])+'),\n'
        strsal += fila
    ultimafila = '('+str(df['id'][len(df)-1])+', \''+limpia_cadena(df['ingredient'][len(df)-1])+'\', '+str(df['id_recipe'][len(df)-1])+');'
    strsal += ultimafila
    f = open('inserta_ingredients.sql', 'w')
    f.write(strsal)
    f.close()

# crea un archivo de inserción para steps (pasos)
def insercion_steps():
    strsal = 'INSERT INTO public.steps(\n'
    strsal += 'id, step, id_recipe)\n'
    strsal += 'VALUES\n'
    df = pd.read_csv('steps.csv')
    for i in range(len(df)-1):
        fila = '('+str(df['id'][i])+', \''+limpia_cadena(df['step'][i])+'\', '+str(df['id_recipe'][i])+'),\n'
        strsal += fila
    ultimafila = '('+str(df['id'][len(df)-1])+', \''+limpia_cadena(df['step'][len(df)-1])+'\', '+str(df['id_recipe'][len(df)-1])+');'
    strsal += ultimafila
    f = open('inserta_steps.sql', 'w')
    f.write(strsal)
    f.close()

# crea un archivo de inserción para tags
def insercion_tags():
    strsal = 'INSERT INTO public.tags(\n'
    strsal += 'id, tag, id_recipe)\n'
    strsal += 'VALUES\n'
    df = pd.read_csv('tags.csv')
    for i in range(len(df)-1):
        fila = '('+str(df['id'][i])+', \''+limpia_cadena(df['tag'][i])+'\', '+str(df['id_recipe'][i])+'),\n'
        strsal += fila
    ultimafila = '('+str(df['id'][len(df)-1])+', \''+limpia_cadena(df['tag'][len(df)-1])+'\', '+str(df['id_recipe'][len(df)-1])+');'
    strsal += ultimafila
    f = open('inserta_tags.sql', 'w')
    f.write(strsal)
    f.close()

insercion_tags()


import pandas

class MarketItem:
    def __init__(self, nombre, tipo_contenedor, tamanio, congelado):
        self.name = nombre
        self.container_type = tipo_contenedor
        self.size = tamanio
        self.frozen = congelado

    def __str__(self):
        return self.name
    # Fin de la clase

class Bolsa:
    def __init__(self, tipo):
        self.secuencia = []
        self.tipo = tipo
    
    # Agregar un elemento a la bolsa
    def add(self, item):
        self.secuencia.append(item)

    # Devuelve true si la bola ya está llena (6 items).
    def esta_llena(self):
        return len(self.secuencia) >= 6
    
    # Devuelve true si la bolsa está vacía.
    def is_empty(self):
        return len(self.secuencia) == 0
    
    # devuelve true si solo tiene elementos medianos
    # (también se cumple por vacuidad)
    def only_medium(self):
        om = True
        for elem in self.secuencia:
            if elem.size != 'medium':
                om = False
                break
        return om
    
    # devuelve true si y solo si contiene algun bote
    def contains_bottle(self):
        for elem in self.secuencia:
            if elem.container_type == 'bottle':
                return True
        return False
    
    def __getitem__(self, index):
        return self.secuencia[index]

    def __len__(self):
        return len(self.secuencia)
    
    def __str__(self):
        retval = '['
        for i in range(len(self.secuencia)-1):
            retval += str(self.secuencia[i]) + ', '
        retval += str(self.secuencia[len(self.secuencia)-1]) + ']'
        return retval

# Obtiene la primera bolsa no llena del tipo especificado.
def get_fb(tipo, bolsas):
    retval = None
    for bag in bolsas:
        if bag.tipo == tipo and not bag.esta_llena():
            retval = bag
            break
    return retval

# Construye objetos (items) a partir del nombre
def str_to_obj(nombre, dic):
    dicitem = dic[nombre]
    return MarketItem(nombre, dicitem['container'], dicitem['size'], dicitem['frozen'])

def strtoobj_list(lista_orden, dic):
    lista_items = []
    for elem in lista_orden:
        lista_items.append(str_to_obj(elem, dic))
    return lista_items


# 1 Cuando a penas va a empacar
def check_order(carrito, dicc):
    # B1
    bag_of_chips = False
    soft_drink = False
    for elem in carrito:
        if elem.name == 'chips':
            bag_of_chips = True
        if elem.name == 'pepsi':
            soft_drink = True
    if bag_of_chips and not soft_drink:
        carrito.append(str_to_obj('pepsi', dicc))

# Definición de reglas

# Regla: hay un bote grande
def regla_isbottlelarge(carrito):
    retval = None
    for i,item in enumerate(carrito):
        if item.size == 'large' and item.container_type == 'bottle':
            retval = item
            del carrito[i]
            break
    return retval

# Regla: hay cualquier item grande
def regla_islarge(carrito):
    retval = None
    for i,item in enumerate(carrito):
        if item.size == 'large':
            retval = item
            del carrito[i]
            break
    return retval

# 2 package large items
def pli(carrito, bolsas):
    # B3: empacar todos los items que sean botes grandes
    aempacar = regla_isbottlelarge(carrito)
    while aempacar != None:
        first_bag = get_fb('normal', bolsas)
        if first_bag == None:
            bolsas.append(Bolsa('normal'))
            first_bag = bolsas[len(bolsas)-1]
        first_bag.add(aempacar)
        aempacar = regla_isbottlelarge(carrito)
    # B4: empacar todos los items grandes
    aempacar = regla_islarge(carrito)
    while aempacar != None:
        first_bag = get_fb('normal', bolsas)
        # si ya tiene 6 items, conseguir otra bolsa
        if first_bag == None:
            bolsas.append(Bolsa('normal'))
            first_bag = bolsas[len(bolsas)-1]
        first_bag.add(aempacar)
        aempacar = regla_islarge(carrito)

# Regla: hay un item mediano y congelado
def regla_ismediumfrozen(carrito):
    retval = None
    for i,item in enumerate(carrito):
        if item.size == 'medium' and item.frozen:
            retval = item
            del carrito[i]
            break
    return retval

# Regla: hay un item mediano
def regla_ismedium(carrito):
    retval = None
    for i,item in enumerate(carrito):
        if item.size == 'medium':
            retval = item
            del carrito[i]
            break
    return retval

# devuelve la primera bolsa no llena que contenga solo elementos medianos.
def get_fb_medium(tipo, bolsas):
    retval = None
    for bolsa in bolsas:
        if bolsa.only_medium() and bolsa.tipo == tipo and not bolsa.esta_llena():
            retval = bolsa
            break
    return retval

# Obtiene la primera bolsa no llena.
def get_fb(tipo, bolsas):
    retval = None
    for bag in bolsas:
        if bag.tipo == tipo and not bag.esta_llena():
            retval = bag
            break
    return retval

# 3 package medium items
def pmi(carrito, bolsas):
    # B7: empacar items medianos congelados
    aempacar = regla_ismediumfrozen(carrito)
    while aempacar != None:
        first_bag = get_fb_medium('freezer', bolsas)
        if first_bag == None:
            bolsas.append(Bolsa('freezer'))
            first_bag = bolsas[len(bolsas)-1]
        first_bag.add(aempacar)
        aempacar = regla_ismediumfrozen(carrito)
    # B8: empacar items no congelados
    aempacar = regla_ismedium(carrito)
    while aempacar != None:
        first_bag = get_fb_medium('normal', bolsas)
        if first_bag == None:
            bolsas.append(Bolsa('normal'))
            first_bag = bolsas[len(bolsas)-1]
        first_bag.add(aempacar)
        aempacar = regla_ismedium(carrito)

# Obtiene la primera bolsa no llena que no contenga botes.
def get_fb_nb(tipo, bolsas):
    retval = None
    for bag in bolsas:
        if bag.tipo == tipo and not bag.esta_llena() and not bag.contains_bottle():
            retval = bag
            break
    return retval

# Regla: hay un item pequeño
def regla_issmall(carrito):
    retval = None
    for i,item in enumerate(carrito):
        if item.size == 'small':
            retval = item
            del carrito[i]
            break
    return retval

# 3 package small items
def psi(carrito, bolsas):
    aempacar = regla_issmall(carrito)
    while aempacar != None:
        # B11: empacar item pequeño en bolsa sin botes
        first_bag = get_fb_nb('normal', bolsas)
        # B12: empacar item pequeño
        if first_bag == None:
            first_bag = get_fb('normal', bolsas)
        if first_bag == None:
            bolsas.append(Bolsa('normal'))
            first_bag = bolsas[len(bolsas)-1]
        first_bag.add(aempacar)
        aempacar = regla_issmall(carrito)

# Construye una orden a partir de un archivo csv.
def construye_csv(archivo, dicc):
    datos = pandas.read_csv(archivo)
    lista_items = []
    items = datos['item']
    cants = datos['cantidad']
    for i,item in enumerate(items):
        for _ in range(cants[i]):
            lista_items.append(item)
    return strtoobj_list(lista_items, dicc)

# Recibe una bolsa de bolsas e imprime el empacado
def imprime_embolsado(bolsas):
    for i,bolsa in enumerate(bolsas):
        print(f'bolsa {i} ('+bolsa.tipo+'): '+str(bolsa))


def main():
    diccionario = {'bread':     {'container': 'plastic bag',      'size':'medium', 'frozen':False},
                   'glop':      {'container': 'Jar',              'size':'small',  'frozen':False},
                   'granola':   {'container': 'cardboard box',    'size':'large',  'frozen':False},
                   'ice cream': {'container': 'cardboard carton', 'size':'medium', 'frozen':True},
                   'pepsi':     {'container': 'bottle',           'size':'large',  'frozen':False},
                   'chips':     {'container': 'plastic bag',      'size':'medium', 'frozen':False}}
    
    print('Ingrese el nombre del archivo que contiene la orden')
    archivo = input()
    carrito = construye_csv(archivo, diccionario)
    print("Carrito:")
    for elem in carrito:
        print(str(elem)+", ", end='')
    # 1: revisar la orden
    check_order(carrito, diccionario)
    bolsas = [Bolsa('normal')] # se crea un conjunto de bolsas vacías
    # 2: empacar items grandes
    pli(carrito, bolsas)
    # 3: empacar items medianos
    pmi(carrito, bolsas)
    # 4: empacar items pequeños
    psi(carrito, bolsas)
    print('\nEmbolsado:')
    imprime_embolsado(bolsas)

if __name__ == '__main__':
    main()

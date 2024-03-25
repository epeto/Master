
alfabeto = "abcdefghijklmnopqrstuvwxyz"

def hashFun(cadena):
    suma = 0
    for i in range(len(cadena)):
        indiceChar = alfabeto.index(cadena[i])
        suma += indiceChar*(26**i)
    return (suma%10000)
    
def main():
    nombres = ["denis", "guadalupe", "alex", "cris", "juan", "rene"]
    #for name in nombres:
    #    print(name, hashFun(name))
    nombres.sort()
    print(nombres)
        

main()


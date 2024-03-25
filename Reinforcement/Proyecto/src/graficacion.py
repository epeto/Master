
import AgenteQ_v1
import matplotlib.pyplot as plt

def main():
    agente = AgenteQ_v1.Agente()
    print('Entrenando al agente...')
    agente.qlearning()
    print('Generando política')
    agente.encuentra_politica()
    print('Realizando control')
    x, y = agente.control(0) # se le pasa la altura inicial
    plt.plot(x, y)
    plt.xlabel('Tiempo')
    plt.ylabel('Altura')
    plt.show()

def main2():
    print('hola mundo')

main()

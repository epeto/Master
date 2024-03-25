## Se implementa un Q-learning sencillo, discretizando los estados

import TanqueDisc
import numpy as np
import random

class Agente:
    def __init__(self):
        self.tam = 100
        self.Q = np.zeros((self.tam, self.tam), dtype = float)
        self.politica = np.zeros((self.tam), dtype = np.int32)
        self.tanque = TanqueDisc.Tanque(1)
    
    ## Transforma un flotante que representa la altura del tanque a una acción.
    def altura_to_estado(self, h):
        hmax = self.tanque.hmax
        if h == hmax:
            return self.tam-1
        return int((h*self.tam)/hmax)
    
    # Transforma una acción discreta a una señal
    def accion_to_senial(self, a):
        umax = self.tanque.umax
        return umax*(a/(self.tam-1))
    
    # Toma una acción basado en épsilon-greedy
    def epsilon_greedy(self, s, epsilon):
        num_al = random.random()
        am = np.argmax(self.Q[s])
        if num_al > epsilon: # devuelve el argumento máximo
            return am
        else: # devuelve cualquier acción que no sea la máxima
            lista_acciones = [i for i in range(self.tam)]
            lista_acciones.remove(am)
            return random.choice(lista_acciones)
    
    # Algoritmo de entrenamiento q-learning
    def qlearning(self):
        episodios = 100000
        pasos = 10000 # pasos máximos por episodio
        eps1 = np.ones((episodios//2), dtype = float)
        eps2 = np.linspace(1,0.01, num = episodios - (episodios//2)) # la épsilon va decrementando con el tiempo
        epsilon = np.concatenate([eps1, eps2])
        gamma = 0.95
        alfa = 0.01
        recompensa_media = []
        for i in range(episodios):
            j = 0
            s_cont = random.random()*2
            s_disc = self.altura_to_estado(s_cont)
            self.tanque.h = s_cont
            terminado = 0
            while j<pasos and terminado == 0:
                accion = self.epsilon_greedy(s_disc, epsilon[i])
                senial = self.accion_to_senial(accion)
                observacion, recompensa, terminado = self.tanque.step(senial)
                s_sig_disc = self.altura_to_estado(observacion)
                self.Q[s_disc][accion] = self.Q[s_disc][accion] + alfa*(recompensa + gamma*max(self.Q[s_sig_disc]) - self.Q[s_disc][accion])
                s_cont = observacion
                s_disc = s_sig_disc
                j+=1
    
    # Una vez que está entrenado el modelo, se calcula la política óptima
    def encuentra_politica(self):
        for i in range(self.politica.shape[0]):
            self.politica[i] = self.accion_to_senial(np.argmax(self.Q[i]))

    # Cuando ya se encontró la política, se puede hacer control sobre el tanque
    def control(self, h_ini):
        ht = [] # altura respecto al tiempo
        tiempo = []
        ht.append(self.tanque.h)
        tiempo.append(0)
        self.tanque.h = h_ini
        for i in range(300):
            s = self.altura_to_estado(self.tanque.h)
            u = self.politica[s]
            self.tanque.step(u)
            ht.append(self.tanque.h)
            tiempo.append(i*self.tanque.ts)
        return (tiempo, ht)


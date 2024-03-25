
# Simulación del sistema de un tanque, discretizado, con periodo de muestreo 0.2 s
# Este será el ambiente.

import math
import numpy as np
import random

class Tanque:
    # recibe la altura objetivo
    def __init__(self, objetivo):
        self.numerador = 2.5409e-4
        self.denominador = [1, -0.9956]
        self.ts = 0.2
        self.h = 0.0 # altura inicial
        self.goal = objetivo
        self.hmax = 2.0 # altura máxima del agua
        self.umax = 50.0 # señal de entrada máxima
        self.max_err = self.hmax
        self.num_actions = 50
        self.tol = 0.01 # tolerancia de error
        self.acciones = np.linspace(0, self.umax, num = self.num_actions, endpoint=False)

    # reinicio del estado del tanque
    def reset(self):
        self.h = 0.0
        return self.h

    # Recibe el estado s y la acción a.
    # Devuelve un par (estado_siguiente, recompensa)
    def actua(self, s, a):
        s_sig = -self.denominador[1]*s + self.numerador*a
        if s_sig < 0:
            s_sig = 0
        if s_sig > self.hmax:
            s_sig = self.hmax
        observacion = s_sig
        terminado = math.fabs(self.goal-s_sig) < self.tol
        if terminado:
          recompensa = 200
        else:
          recompensa = -1
        return (observacion, recompensa, terminado)
    
    # actualiza la altura de este tanque, dada una acción discreta a
    def step(self, a):
        u = self.acciones[a]
        observacion, recompensa, terminado = self.actua(self.h, u)
        self.h = observacion
        return (observacion, recompensa, terminado)

    # Devuelve una acción aleatoria (en discreto)
    def action_sample(self):
        return random.randint(0, self.num_actions-1)
    
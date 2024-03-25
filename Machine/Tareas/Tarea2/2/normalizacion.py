
import pandas as pd
import numpy as np
import math

datacsv = pd.read_csv('partidas_entrenamiento.csv')
datanp = datacsv.to_numpy()

def reescalado(X):
    X2 = np.ones(X.shape)
    for c in range(1, X.shape[1]):
        columna = X[:,c]
        xmax = columna.max()
        xmin = columna.min()
        for f in range(X.shape[0]):
            X2[f][c] = (X[f][c] - xmin)/(xmax - xmin)
    return X2
    
'''
def estandarizacion(X):
    X2 = X.copy()
    denoms = np.zeros(X.shape[0])
    for 
    for c in range(X.shape[1]):
        columna = X[:,c]
        prom = sum(columna)/columna.shape[0]
        for f in range(X.shape[0]):
            num = X[f][c] - prom
            den = math.sqrt()
'''

Xres = reescalado(datanp)
print(Xres)


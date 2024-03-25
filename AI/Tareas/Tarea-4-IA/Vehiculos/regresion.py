
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import math

def construyeXY(nombreArchivo):
    archivo = open(nombreArchivo, "r")
    lineas = archivo.readlines()
    archivo.close()
    filas = []
    for linea in lineas:
        filas.append(linea.split(","))
    x = []
    y = []
    for fila in filas:
        vx = []
        for i in range(len(fila)-1):
            vx.append(float(fila[i]))
        x.append(vx)
        y.append(float(fila[len(fila)-1]))
    return (x, y)
    
def main():
    #Primero las x, y de entrenamiento
    x, y = construyeXY("datos70.csv")
    poly = PolynomialFeatures(degree=3)
    x2 = poly.fit_transform(x)
    reg = linear_model.LinearRegression()
    reg.fit(x2, y)
    
    #Luego las x, y de prueba
    xp, yp = construyeXY("datos30.csv")
    xp2 = poly.fit_transform(xp)
    predY = reg.predict(xp2) #valores de predicción
    
    escritor = open("reporte.csv", "w")
    primeraFila = "Prediccion,Valor real,Diferencia absoluta\n"
    escritor.write(primeraFila)
    errorCuad = 0
    for i in range(len(yp)):
        nuevaLinea = ""
        nuevaLinea += str(predY[i]) + ","
        nuevaLinea += str(yp[i]) + ","
        difAbs = math.fabs(predY[i] - yp[i])
        errorCuad += difAbs**2
        nuevaLinea += str(difAbs)
        escritor.write(nuevaLinea)
        escritor.write("\n")
    errorCuad /= len(yp)
    ultimaFila = "Error,cuadratico," + str(errorCuad)
    escritor.write(ultimaFila)
    escritor.close()
    
main()


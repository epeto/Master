

public class Equilatero extends Triangulo {
    
    /**
     * Constructor de la clase que recibe un lado del triángulo.
     * @param lado del triángulo
     */
    public Equilatero(double lado){
        lados[0] = lado;
        lados[1] = lado;
        lados[2] = lado;
    }

    /**
     * Calcula el área del triángulo.
     */
    @Override
    public double calcularArea(){
        double altura = (Math.sqrt(3)/2) * lados[0];
        return (lados[0]*altura)/2;
    }
}

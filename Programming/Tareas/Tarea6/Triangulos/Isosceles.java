
public class Isosceles extends Triangulo {
    /**
     * Constructor de un triángulo isóceles (dos lados iguales)
     * @param lado1 base del triángulo
     * @param lado2 representa los dos lados que no son la base
     */
    public Isosceles(double lado1, double lado2){
        lados[0] = lado1;
        lados[1] = lado2;
        lados[2] = lado2;
    }

    @Override
    public double calcularArea(){
        double term1 = lados[1]*lados[1];
        double term2 = (lados[0]*lados[0])/4;
        double altura = Math.sqrt(term1-term2);
        return (lados[0]*altura)/2;
    }
}
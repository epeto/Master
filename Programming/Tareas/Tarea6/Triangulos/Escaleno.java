
public class Escaleno extends Triangulo {
    /**
     * Constructor del triángulo escaleno que recibe la longitud de cada lado.
     * @param lado1
     * @param lado2
     * @param lado3
     */
    public Escaleno(double lado1, double lado2, double lado3){
        lados[0] = lado1;
        lados[1] = lado2;
        lados[2] = lado3;
    }

    @Override
    public double calcularArea(){
        double sp = calcularPerimetro()/2;
        double producto = sp * (sp-lados[0]) * (sp-lados[1]) * (sp-lados[2]);
        return Math.sqrt(producto);
    }
}

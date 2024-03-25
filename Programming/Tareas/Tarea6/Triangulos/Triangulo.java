
import java.util.Arrays;

public class Triangulo{
    protected double[] lados;

    //Constructor de la clase triángulo
    public Triangulo(){
        lados = new double[3];
    }

    //Método que calcula el perímetro de un triángulo.
    public double calcularPerimetro(){
        double suma = lados[0]+lados[1]+lados[2];
        return suma;
    }

    //Método que calcula el área de un triángulo.
    public double calcularArea(){
        return 0.0;
    }

    //Método que imprime los lados del triángulo.
    public void imprimirLados(){
        System.out.println("Lados "+Arrays.toString(lados));
    }
}

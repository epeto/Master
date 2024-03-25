
public class TestTriangulo {
    public static void main(String[] args){
        Equilatero equi = new Equilatero(2);
        double area = equi.calcularArea();
        double peri = equi.calcularPerimetro();
        System.out.println("--- EQUILATERO ---");
        System.out.println("area = "+area);
        System.out.println("perimetro = "+peri);
        equi.imprimirLados();

        Isosceles iso = new Isosceles(2, 5);
        area = iso.calcularArea();
        peri = iso.calcularPerimetro();
        System.out.println("--- ISOSCELES ---");
        System.out.println("area = "+area);
        System.out.println("perimetro = "+peri);
        iso.imprimirLados();

        Escaleno esca = new Escaleno(3, 4, 5);
        area = esca.calcularArea();
        peri = esca.calcularPerimetro();
        System.out.println("--- ESCALENO ---");
        System.out.println("area = "+area);
        System.out.println("perimetro = "+peri);
        esca.imprimirLados();
    }
}

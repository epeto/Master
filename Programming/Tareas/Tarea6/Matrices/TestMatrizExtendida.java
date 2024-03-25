
import java.util.Scanner;

public class TestMatrizExtendida {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese el lado de la matriz.");
        int n = sc.nextInt();
        MatrizExtendida m1 = new MatrizExtendida(n);
        System.out.println("Ingrese la fila a modificar.");
        int f = sc.nextInt();
        System.out.println("Ingrese la columna a modificar.");
        int c = sc.nextInt();
        System.out.println("Ingrese el valor nuevo en esa posición.");
        int val = sc.nextInt();
        m1.sustituirElemento(f, c, val);
        System.out.println("Matriz construída:");
        sc.close();
        m1.imprimirMatriz();
    }
}

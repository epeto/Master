
import java.util.Scanner;

public class TestMatriz {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese el lado de la matriz.");
        int n = sc.nextInt();
        sc.close();
        Matriz m1 = new Matriz(n);
        System.out.println("Matriz construída:");
        m1.imprimirMatriz();
    }
}

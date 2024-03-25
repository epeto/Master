
import java.util.Scanner;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.HashSet;

public class Principal {
    public static void main(String[] args){
        System.out.println("Escriba el nombre del archivo con los datos de los elementos.");
        Scanner sc = new Scanner(System.in);
        String archivo = sc.nextLine();
        sc.close();
        Lector lector = new Lector();
        lector.lee(archivo);
        long[] caja = new long[1];
        ArrayList<Elemento> elementos = lector.creaElementos(caja);
        long capacidad = caja[0];
        Mochila mochila = new Mochila(capacidad);
        Estado actual = new Estado(0, 0, new HashSet<>(), 0);
        LinkedList<Estado> sucesores = actual.expande(elementos, capacidad);
        //El algoritmo termina cuando la lista de sucesores es vacía.
        while(!sucesores.isEmpty()){
            //Primero se elige el estado con la llave más pequeña.
            Estado minimo = sucesores.getFirst();
            for(Estado sig : sucesores){
                if(sig.getKey() < minimo.getKey()){
                    minimo = sig;
                }
            }
            //El nuevo estado actual va a ser el que tenga la llave más pequeña.
            actual = minimo;
            sucesores = actual.expande(elementos, capacidad);
        }
        mochila.copiaEstado(actual, elementos);
        System.out.println("\nMejor mochila encontrada:");
        System.out.println(mochila);
    }
}

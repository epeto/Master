
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.HashSet;
import java.util.Calendar;

public class Principal {

    public static void main(String[] args){
        System.out.println("Escriba el nombre del archivo con los datos de los elementos.");
        Scanner sc = new Scanner(System.in);
        String archivo = sc.nextLine();
        System.out.println("Escriba el tiempo máximo (en segundos) que se ejecutará la búsqueda.");
        int timeLimit = Integer.parseInt(sc.nextLine());
        sc.close();
        Lector lector = new Lector();
        lector.lee(archivo);
        long[] caja = new long[1];
        ArrayList<Elemento> elementos = lector.creaElementos(caja);
        long capacidad = caja[0];
        Mochila mochila = new Mochila(capacidad);

        //Se realiza una búsqueda utilizando la estrategia de A*
        Tiempo t1 = new Tiempo();
        boolean tiempoAlcanzado = false;
        Calendar limite = t1.tiempoLimite(t1.ahora(), timeLimit);
        PriorityQueue<Estado> cola = new PriorityQueue<>();
        Estado inicial = new Estado(0, 0, new HashSet<>(), 0);
        cola.offer(inicial);
        try{
            //Para verificar que no se repitan estados (en la medida de lo posible).
            HashSet<Integer> estadosRep = new HashSet<>();
            estadosRep.add(inicial.hashCode());
            while(!cola.isEmpty() && !tiempoAlcanzado){
                Estado actual = cola.poll();
                LinkedList<Estado> sucesores = actual.expande(elementos, capacidad);
                for(Estado suc : sucesores){
                    if(!estadosRep.contains(suc.hashCode())){
                        estadosRep.add(suc.hashCode());
                        if(suc.valorTotal > mochila.valorTotal){
                            mochila.copiaEstado(suc, elementos);
                        }
                        cola.offer(suc);
                    }
                }
                if(t1.pasoLimite(limite)){
                    System.out.println("Pasó el límite de "+timeLimit+" s");
                    tiempoAlcanzado = true;
                }
            }
        }catch(OutOfMemoryError error){
            System.err.println("Se agotó la memoria.");
        }finally{
            System.out.println("\nMejor mochila encontrada:");
            System.out.println(mochila);
        }
    }
}

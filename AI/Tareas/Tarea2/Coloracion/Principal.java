
import java.util.Scanner;
import java.util.Random;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.TreeSet;
import java.util.HashMap;

public class Principal{

    /**
     * Algoritmo de recocido simulado
     * @param grafica gráfica a la cual se le va a buscar una coloración.
     * @param temperatura número total de iteraciones a realizar.
     * @return mejor estado encontrado durante la ejecución.
     */
    public static Estado recocido(Grafica grafica, long temperatura){
        //Primero se colorea la gráfica con n colores.
        for(Vertice v : grafica.vertices){
            v.color = v.id; //Al vértice i se le asigna el color i.
        }
        grafica.numColores = grafica.getOrden();
        Estado mejor = new Estado(grafica); //Mejor estado.
        double doubTemp = (double) temperatura; //Temperatura en tipo double
        doubTemp /= 100;
        double decremento = 0.01;
        ArrayList<Estado> sucesores = grafica.expande(); //Primera expansión
        Random rn = new Random(Calendar.getInstance().getTimeInMillis());
        while(doubTemp > 0){
            int indexRand = rn.nextInt(sucesores.size());
            Estado siguiente = sucesores.get(indexRand); //estado elegido de forma aleatoria.
            double deltaE = (double) (grafica.numColores - siguiente.numColores);
            if(deltaE > 0){ //Una mejora se da cuando el número de colores disminuye
                grafica.copiaEstado(siguiente);
                sucesores = grafica.expande();
            }else{
                double probabilidad = Math.pow(Math.E, deltaE/doubTemp);
                if(rn.nextDouble() < probabilidad){
                    grafica.copiaEstado(siguiente);
                    sucesores = grafica.expande();
                }
            }

            if(grafica.numColores < mejor.numColores){
                mejor.copiaGrafica(grafica);
            }
            doubTemp -= decremento;
        }
        return mejor;
    }

    /**
     * Trata de usar los números más pequeños posibles para colorear una gráfica.
     * Recibe un estado y elige una coloración equivalente pero con números más pequeños.
     * @param estado
     */
    public static void minimizaColores(Estado estado){
        TreeSet<Integer> arbol = new TreeSet<>();
        for(int color : estado.colVert){
            if(!arbol.contains(color)){
                arbol.add(color);
            }
        }
        int indice = 0;
        HashMap<Integer, Integer> tabla = new HashMap<>();
        for(Integer elem : arbol){
            tabla.put(elem, indice);
            indice++;
        }

        for(int i=0; i<estado.colVert.length; i++){
            estado.colVert[i] = tabla.get(estado.colVert[i]);
        }
    }

    public static void main(String[] args) {
        Lector l = new Lector();
        Scanner sc = new Scanner(System.in);
        System.out.println("Escriba el nombre del archivo que contiene a la gráfica.");
        String nombreArchivo = sc.nextLine();
        l.lee(nombreArchivo); //Se lee el archivo.
        Grafica g1;
        g1 = l.creaGrafica(); //Se crea una gráfica con el archivo leído.
        System.out.println("Ingrese la temperatura (número total de iteraciones)");
        long temp = sc.nextLong();
        sc.close();
        Estado mejor = recocido(g1, temp);
        minimizaColores(mejor);
        System.out.println("\n"+mejor.numColores);
        for(int i=0; i<mejor.colVert.length; i++){
            System.out.println(mejor.colVert[i] + " " + i);
        }
    }
}





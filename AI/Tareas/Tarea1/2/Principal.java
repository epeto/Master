

import org.graphstream.graph.*;
import org.graphstream.graph.implementations.SingleGraph;
import java.util.Scanner;
import javax.naming.NameNotFoundException;
import java.util.HashMap;

public class Principal{
    /**
    * Método que recibe un objeto tipo Grafica y la dibuja.
    * @param g: gráfica que recibe.
    * @param inicial: id del vértice inicial
    * @param fin: id del vértice final
    */
    public void dibujaGrafica(Grafica g, String inicial, String fin){
        String styleSheet = "edge {size: 5px; text-size: 20;}"
                            +"edge.tree {fill-color: red;}"
                            +"node {size: 10px; text-size: 20;}"
                            +"node.meta {fill-color: green;}"
                            +"node.origen {fill-color: blue;}"; //Estilo de la gráfica.

        Graph graph = new SingleGraph("Ventana"); //Se crea una gráfica de graphstream
        
        //En esta parte se agregan todos los vértices a "graph".
        for(Vertice v : g.vertices.values()){
            graph.addNode(v.toString());
            //Se agrega una etiqueta con el nombre del vértice.
            graph.getNode(v.toString()).setAttribute("ui.label", v.toString());
        }

        //En esta parte se agregan las aristas.
        for(Vertice v : g.vertices.values()){
            for(Pair<Vertice, Integer> par : v.ady){
                Vertice u = par.getKey();
                String nombreArista = v.toString()+","+u.toString();
                String nombreArista2 = u.toString()+","+v.toString();
                if(graph.getEdge(nombreArista2) == null){ //Si no se ha agregado la arista (u,v).
                    graph.addEdge(nombreArista, v.toString(), u.toString()); //Agregar la (v,u).
                    graph.getEdge(nombreArista).setAttribute("ui.label", par.getValue()); //Se etiqueta la arista con su peso.
                }
            }
        }
        
        //En esta parte se cambia la clase (de estilo) de las aristas que pertenecen al camino.
        graph.getNode(inicial).setAttribute("ui.class","origen");
        graph.getNode(fin).setAttribute("ui.class","meta");
        Vertice actual = g.getVertice(fin);
        while(!actual.id.equals(inicial) && actual.p != null){
            String nombreAri1 = actual.p.toString()+","+actual.toString();
            String nombreAri2 = actual.toString()+","+actual.p.toString();
            Edge ari1 = graph.getEdge(nombreAri1);
            Edge ari2 = graph.getEdge(nombreAri2);
            if(ari1 != null){ //Si la arista existe.
                ari1.setAttribute("ui.class","tree");
            }
            if(ari2 != null){ //Si la arista existe.
                ari2.setAttribute("ui.class","tree");
            }
            actual = actual.p;
        }
        
        graph.setAttribute("ui.stylesheet", styleSheet); //Se agrega la hoja de estilo a la gráfica.
        System.setProperty("org.graphstream.ui", "swing");
        graph.display(); //Se pone la gráfica en pantalla.
    }

    public static void main(String[] args) throws NameNotFoundException{
        Lector l = new Lector();
        Scanner sc = new Scanner(System.in);
        System.out.println("Escriba el nombre del archivo que contiene a la gráfica.");
        String nombreArchivo = sc.nextLine();
        l.lee(nombreArchivo); //Se lee el archivo.
        Grafica g1;
        g1 = l.creaGrafica(); //Se crea una gráfica con el archivo leído.
        System.out.println("Escriba el nombre del vértice de origen.");
        String vOrigen = sc.nextLine();
        if(g1.getVertice(vOrigen) == null){
            sc.close();
            throw new NameNotFoundException("Ese vértice no existe.");
        }
        System.out.println("Escriba el nombre del vértice meta.");
        String vMeta = sc.nextLine();
        if(g1.getVertice(vMeta) == null){
            sc.close();
            throw new NameNotFoundException("Ese vértice no existe.");
        }
        System.out.println("Elija un número del 1 al 6 para seleccionar el algoritmo.");
        System.out.println("1.- Búsqueda en anchura");
        System.out.println("2.- Búsqueda en profundidad");
        System.out.println("3.- Búsqueda iterativa");
        System.out.println("4.- Búsqueda de costo uniforme");
        System.out.println("5.- Búsqueda voraz");
        System.out.println("6.- Búsqueda A*");
        String caso = sc.nextLine();
        switch(caso.charAt(0)){
            case '1': Algoritmos.anchura(g1, vOrigen, vMeta);
            break;
            case '2': Algoritmos.profundidad(g1, vOrigen, vMeta, Integer.MAX_VALUE);
            break;
            case '3': Algoritmos.iterativa(g1, vOrigen, vMeta);
            break;
            case '4': Algoritmos.costoUniforme(g1, vOrigen, vMeta);
            break;
            case '5':
            case '6': l.lineas.clear();
                      System.out.println("Escriba el nombre del archivo que contiene las distancias.");
                      String archivoDistancias = sc.nextLine();
                      l.lee(archivoDistancias);
                      HashMap<String, Integer> tabla = l.creaTabla();
                      vMeta = "Bucharest";
                      if(caso.charAt(0) == '5'){
                          Algoritmos.voraz(g1, vOrigen, vMeta, tabla);
                      }else{
                          Algoritmos.aestrella(g1, vOrigen, vMeta, tabla);
                      }
            break;
            default: System.out.println("Algoritmo no implementado.");
        }
        sc.close();
        Vertice meta = g1.getVertice(vMeta);
        Principal pr = new Principal();
        pr.dibujaGrafica(g1, vOrigen, vMeta); //Se dibuja la gráfica en pantalla
        System.out.println("Costo del camino: "+meta.costoCamino);
    }
}






// Clase que representa una gráfica (o grafo) con listas de adyacencias

import java.util.HashMap;

public class Grafica {

    HashMap<String, Vertice> vertices; //Conjunto de vértices

    /**
     * Constructor de la clase gráfica.
     **/
    public Grafica(){
        vertices = new HashMap<String, Vertice>();
    }

    /**
    * Función que recibe un id y devuelve el vértice que tiene dicho id.
    * Si no existe devuelve null.
    * @param ident: identificador del vértice.
    * @return vertice con ese id.
    */
    public Vertice getVertice(String ident){
        return vertices.get(ident);
    }
 
    /**
    * Función que agrega una arista cuando recibe los objetos tipo Vertice.
    * @param vi: vértice de origen de la arista.
    * @param vj: id del vértice de destino de la arista.
    * @param peso: peso de la arista a agregar.
    */
    public void agregaArista(Vertice vi, Vertice vj, int peso){
        vi.agregaVecino(vj, peso);
        vj.agregaVecino(vi, peso);
    }

    /**
    * Función que agrega una arista, recibiendo los id's de los vértices.
    * @param i: id del vértice de origen de la arista.
    * @param j: id del vértice de destino de la arista.
    * @param peso: peso de la arista a agregar.
    */
    public void agregaArista(String i, String j, int peso){
        Vertice vert_i = getVertice(i);
        Vertice vert_j = getVertice(j);
        agregaArista(vert_i, vert_j, peso);
    }
  
    /**
    * Agrega un vértice a la gráfica
    * @param ident: identificador del vértice nuevo.
    */
    public void agregaVertice(String ident){
        Vertice nuevo = new Vertice(ident);
        vertices.put(ident, nuevo);
    }

    /**
    * Obtiene el orden(número de vértices) de la gráfica.
    * @return orden de la gráfica.
    */
    public int getOrden(){
        return vertices.size();
    }
}




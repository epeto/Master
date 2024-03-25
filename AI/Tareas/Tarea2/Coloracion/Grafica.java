
// Clase que representa una gráfica (o grafo) con listas de adyacencias

import java.util.ArrayList;

public class Grafica {

    Vertice[] vertices; //Conjunto de vértices
    int numColores;

    /**
     * Constructor de la clase gráfica.
     **/
    public Grafica(int n){
        vertices = new Vertice[n];
        numColores = 0;
        for(int i=0; i<n; i++){
            agregaVertice(i);
        }
    }

    /**
    * Función que recibe un id y devuelve el vértice que tiene dicho id.
    * @param ident: identificador del vértice.
    * @return vertice con ese id.
    */
    public Vertice getVertice(int ident){
        return vertices[ident];
    }
 
    /**
    * Función que agrega una arista cuando recibe los objetos tipo Vertice.
    * @param vi: vértice de origen de la arista.
    * @param vj: id del vértice de destino de la arista.
    */
    public void agregaArista(Vertice vi, Vertice vj){
        vi.agregaVecino(vj);
        vj.agregaVecino(vi);
    }

    /**
    * Función que agrega una arista, recibiendo los id's de los vértices.
    * @param i: id del vértice de origen de la arista.
    * @param j: id del vértice de destino de la arista.
    */
    public void agregaArista(int i, int j){
        Vertice vert_i = getVertice(i);
        Vertice vert_j = getVertice(j);
        agregaArista(vert_i, vert_j);
    }
  
    /**
    * Agrega un vértice a la gráfica
    * @param ident: identificador del vértice nuevo.
    */
    public void agregaVertice(int ident){
        Vertice nuevo = new Vertice(ident);
        vertices[ident] = nuevo;
    }

    /**
    * Obtiene el orden(número de vértices) de la gráfica.
    * @return orden de la gráfica.
    */
    public int getOrden(){
        return vertices.length;
    }

    /**
     * Genera una lista de los sucesores de la coloración actual.
     * Un sucesor se obtiene al cambiar el color aleatoriamente de exactamente un vértice.
     * @return lista de sucesores.
     */
    public ArrayList<Estado> expande(){
        ArrayList<Estado> lista = new ArrayList<>();
        for(Vertice v : vertices){
            int colorAntiguo = v.color;
            v.cambiaColor(getOrden());
            lista.add(new Estado(this));
            v.color = colorAntiguo;
        }
        return lista;
    }

    /**
     * Copia un estado para actualizar la coloración de esta gráfica.
     * @param e estado que recibe.
     */
    public void copiaEstado(Estado e){
        for(int i=0; i<getOrden(); i++){
            vertices[i].color = e.colVert[i];
        }
        numColores = e.numColores;
    }
}


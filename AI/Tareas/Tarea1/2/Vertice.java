
//Clase vértice con pesos en los vecinos.

import java.util.LinkedList;

public class Vertice implements Comparable<Vertice> {
    LinkedList<Pair<Vertice, Integer>> ady; //Lista de adyacencias (vecinos)
    String id; //Identificador.
    int key; //Atributo para comparar.
    int costoCamino; //Servirá para guardar el costo desde el origen hasta este vértice.
    boolean visitado; //para no visitar un vértice dos veces.
    Vertice p; //Padre de este vértice.
  
    /**
     * Constructor de la clase vértice.
     * @param ident: identificador del vértice (su nombre).
     */
    public Vertice(String ident){
        id = ident;
        ady = new LinkedList<Pair<Vertice, Integer>>();
        visitado = false;
    }
  
    //Comprueba si 2 vértices son iguales.
    @Override
    public boolean equals(Object o){
        boolean ret = false;
        if(o instanceof Vertice){
            Vertice comp = (Vertice)o;
            if(comp.id.equals(this.id)){
                ret = true;
            }
        }
        return ret;
    }
  
    /**
     * Agrega un vecino a este vértice
     * @param vec: nuevo vecino.
     * @param peso: peso de la arista entre este vértice y el vecino.
     */
    public void agregaVecino(Vertice vec, int peso){
        Pair<Vertice, Integer> vecino = new Pair<>(vec, peso);
        if(!ady.contains(vecino)){
            ady.add(vecino);
        }
    }

    @Override
    public String toString(){
        return id;
    }

    @Override
    public int compareTo(Vertice v) {
        return (this.key - v.key);
    }
    
    @Override
    public int hashCode(){
        return id.hashCode();
    }
}





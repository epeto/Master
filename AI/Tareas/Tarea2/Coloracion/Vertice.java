
//Clase vértice con pesos en los vecinos.

import java.util.LinkedList;
import java.util.HashSet;
import java.util.Random;
import java.util.Calendar;

public class Vertice {
    LinkedList<Vertice> ady; //Lista de adyacencias (vecinos)
    int id; //Identificador.
    int color; //número que representa su color.
  
    /**
     * Constructor de la clase vértice.
     * @param ident: identificador del vértice (su nombre).
     */
    public Vertice(int ident){
        id = ident;
        ady = new LinkedList<Vertice>();
    }
  
    //Comprueba si 2 vértices son iguales.
    @Override
    public boolean equals(Object o){
        boolean ret = false;
        if(o instanceof Vertice){
            Vertice comp = (Vertice)o;
            if(comp.id == this.id){
                ret = true;
            }
        }
        return ret;
    }

    /**
     * Agrega un vecino a este vértice
     * @param vec: nuevo vecino.
     */
    public void agregaVecino(Vertice vec){
        if(!ady.contains(vec)){
            ady.add(vec);
        }
    }

    @Override
    public String toString(){
        return String.valueOf(id);
    }
    
    @Override
    public int hashCode(){
        return id;
    }

    /**
     * Cambia aleatoriamente el color de este vértice a uno que no sea el mismo 
     * (si se puede) y que cumpla que ningún vecino tiene ese color.
     * @param n : el orden de la gráfica
     */
    public void cambiaColor(int n){
        HashSet<Integer> conjunto = new HashSet<>();
        for(int i=0; i<n; i++){
            conjunto.add(i);
        }
        if(conjunto.contains(color)){
            conjunto.remove(color);
        }
        for(Vertice vec : ady){
            if(conjunto.contains(vec.color)){
                conjunto.remove(vec.color);
            }
        }
        LinkedList<Integer> candidatos = new LinkedList<>(conjunto);
        if(!candidatos.isEmpty()){
            Random rn = new Random(Calendar.getInstance().getTimeInMillis());
            int indexRand = rn.nextInt(candidatos.size());
            color = candidatos.get(indexRand);
        }
    }
}




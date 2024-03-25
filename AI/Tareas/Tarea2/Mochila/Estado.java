
/**
 * Representa un estado de la mochila.
 */

import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;

public class Estado implements Comparable<Estado>{
    long pesoTotal; //suma de los pesos de todos los elementos en este estado
    long valorTotal; //suma de los valores.
    HashSet<Integer> conjunto; //guarda los id's de los elementos en este estado.
    long key; //se usará para comparar.

    public Estado(long peso, long valor, HashSet<Integer> conj, long llave){
        pesoTotal = peso;
        valorTotal = valor;
        conjunto = new HashSet<>(conj);
        key = llave;
    }

    @Override
    public int compareTo(Estado e) {
        Long l = this.key - e.key;
        return l.intValue();
    }

    public long getKey(){
        return key;
    }

    /**
     * Expande este estado.
     * @param listaElems lista total de elementos.
     * @param capacidad de la mochila.
     * @return lista con los estados sucesores de este estado.
     */
    public LinkedList<Estado> expande(List<Elemento> listaElems, long capacidad){
        LinkedList<Estado> sucesores = new LinkedList<>();
        for(int i=0; i<listaElems.size(); i++){
            if(!conjunto.contains(i)){
                Elemento elem = listaElems.get(i);
                if(elem.peso + pesoTotal <= capacidad){
                    long pesoNuevo = elem.peso + pesoTotal;
                    long valorNuevo = elem.valor + valorTotal;
                    //f(x) = g(x) + h(x)
                    //g(x) = peso acumulado
                    //h(x) = negativo del valor acumulado
                    long keyNueva = pesoNuevo - valorNuevo;
                    Estado estadoNuevo = new Estado(pesoNuevo, valorNuevo, conjunto, keyNueva);
                    estadoNuevo.conjunto.add(i); //Inserta un nuevo elemento
                    sucesores.addLast(estadoNuevo);
                }
            }
        }
        return sucesores;
    }
}

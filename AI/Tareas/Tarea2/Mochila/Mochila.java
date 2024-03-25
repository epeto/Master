
/**
 * Representa a la mochila.
 * Solo guardará el mejor estado encontrado.
 */

import java.util.LinkedList;
import java.util.List;

public class Mochila {
    long capacidad;
    long pesoTotal; //suma de los pesos de todos los elementos en este estado.
    long valorTotal; //suma de los valores.
    LinkedList<Elemento> lista; //Lista de elementos en la mochila.

    public Mochila(long capacidad){
        this.capacidad = capacidad;
        lista = new LinkedList<>();
        pesoTotal = 0;
        valorTotal = 0;
    }

    @Override
    public String toString(){
        return "capacidad: "+capacidad
        +"\npeso: "+pesoTotal
        +"\nvalor: "+valorTotal
        +"\nelementos: "+lista.toString();
    }

    public void copiaEstado(Estado estado, List<Elemento> listaTotal){
        pesoTotal = estado.pesoTotal;
        valorTotal = estado.valorTotal;
        lista.clear();
        for(Integer id : estado.conjunto){
            lista.add(listaTotal.get(id));
        }
    }
}

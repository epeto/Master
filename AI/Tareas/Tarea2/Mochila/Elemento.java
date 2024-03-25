
/**
 * Representa un elemento que se puede meter en la mochila
 */

public class Elemento {
    int id;
    long valor;
    long peso;

    public Elemento(int id, long valor, long peso){
        this.id = id;
        this.valor = valor;
        this.peso = peso;
    }

    @Override
    public String toString(){
        return "(i: "+id+", v: "+valor+", p: "+peso+")";
    }
}

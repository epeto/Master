
/**
 * @author: Emmanuel Peto Gutiérrez
 */

public class Inventario {

    //Variable estática que lleva el conteo del siguiente id.
    private static int nextId = 99;

    //método que incrementa la variable de clase nextId y la devuelve.
    public static int getNextId(){
        nextId++;
        return nextId;
    }
}

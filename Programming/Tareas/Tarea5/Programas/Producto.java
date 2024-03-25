
/**
 * @author: Emmanuel Peto Gutiérrez
 */

public class Producto {

    private int id; //identificador del producto

    //Constructor del producto
    public Producto(){
        id = Inventario.getNextId();
    }

    //Devuelve el id del producto
    public int getId(){
        return id;
    }

}

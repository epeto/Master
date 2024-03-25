
/**
 * @author: Emmanuel Peto Gutiérrez
 */

public class Perro{
    private String nombre;
    private String raza;
    private float peso;

    /**
     * Constructor de Perro con un parámetro tipo String.
     * @param nombre del perro.
     */
    public Perro(String nombre){
        this.nombre = nombre;
    }

    /**
     * Constructor de Perro con dos parámetros tipo String.
     * @param nombre del perro
     * @param raza del perro
     */
    public Perro(String nombre, String raza){
        this.nombre = nombre;
        this.raza = raza;
    }

    /**
     * Constructor de Perro con dos parámetros String y uno float.
     * @param nombre
     * @param raza
     * @param peso
     */
    public Perro(String nombre, String raza, float peso){
        this.nombre = nombre;
        this.raza = raza;
        this.peso = peso;
    }

    /**
     * Método que muestra los atributos del perro.
     */
    public void describir(){
        System.out.println("Nombre: "+nombre+"\t"
                          +"Raza: "+raza+"\t"
                          +"Peso: "+peso);
    }

    /**
     * Devuelve el nombre del perro
     * @return nombre
     */
    public String getNombre(){
        return nombre;
    }

    /**
     * Método que simula que un perro ladra y muestra quién ladra.
     */
    public void ladrar(){
        System.out.println("woof woof ... ("+nombre+" esta ladrando)");
    }
}

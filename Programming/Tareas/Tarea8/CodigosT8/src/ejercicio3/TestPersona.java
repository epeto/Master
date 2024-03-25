/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ejercicio3;

/**
 *
 * @author emmanuel
 */
public class TestPersona {

    public static void main(String[] args){
        Persona p1 = new Persona("Pedro", "Paramo", 21);
        Persona p2 = new Persona("Meriadoc", "Brandigamo", 55);
        Persona p3 = new Persona("Aureliano", "Buendía", 35);
    
        System.out.println("Se tienen 3 personas:");
        System.out.println(p1.getNombre()+" "+p1.getApellido()+" de "+p1.getEdad()+" años.");
        System.out.println(p2.getNombre()+" "+p2.getApellido()+" de "+p2.getEdad()+" años.");
        System.out.println(p3.getNombre()+" "+p3.getApellido()+" de "+p3.getEdad()+" años.");
        
        Persona mayor = Comparador.mayorEntre3(p1, p2, p3);
        
        System.out.println("\nEl mayor entre ellos es:");
        System.out.println(mayor);
    }
}

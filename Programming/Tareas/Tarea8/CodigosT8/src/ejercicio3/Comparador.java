/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ejercicio3;

/**
 *
 * @author emmanuel
 */
public class Comparador {
    public static Persona mayorEntre3(Persona p1, Persona p2, Persona p3){
        Persona retVal;
        if(p1.getEdad() > p2.getEdad()){
            retVal = p1;
        }else{
            retVal = p2;
        }
        
        if(p3.getEdad() > retVal.getEdad()){
            retVal = p3;
        }
        return retVal;
    }
}

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ejercicio3;

/**
 *
 * @author emmanuel
 */
public class Persona {
    private String nombre;
    private String apellido;
    private int edad;
    
    public Persona(String nom, String ap, int ed){
        nombre = nom;
        apellido = ap;
        edad = ed;
    }
    
    public String getNombre(){
        return nombre;
    }
    
    public String getApellido(){
        return apellido;
    }
    
    public int getEdad(){
        return edad;
    }
    
    public void setNombre(String nom){
        nombre = nom;
    }
    
    public void setApellido(String ap){
        apellido = ap;
    }
    
    public void setEdad(int ed){
        edad = ed;
    }
    
    public String toString(){
        return "Nombre: "+nombre+" "+apellido+", Edad: "+edad+" años";
    }
}

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ejercicio2;

import java.util.LinkedList;

/**
 *
 * @author emmanuel
 */
public class TestPalindromos {
    
    public static void main(String[] args){
        LinkedList<String> palins = new LinkedList<>();
        LinkedList<String> noPalins = new LinkedList<>();
    
        palins.add("Oxxo");
        palins.add("Alli ves, Sevilla");
        palins.add("Asi, Maria, raparas a Sara para ir a misa");
        palins.add("Dabale arroz a la zorra el abad");
        palins.add("Anita lava la tina");
        
        noPalins.add("somos no somos");
        noPalins.add("s o m o s, no, som..os");
        noPalins.add("esta oracion no es palindroma");
        noPalins.add("el perro juega con la pelota");
        noPalins.add("america");
        
        //Se espera que todas sean palíndromas.
        for(String elem : palins){
            boolean esPali = Palindromos.esPalindroma(elem);
            if(esPali){
                System.out.println(elem+"\nes palíndroma\n");
            }else{
                System.out.println(elem+"\nno es palíndroma\n");
            }
        }
        
        //Se espera que ninguna sea palíndroma.
        for(String elem : noPalins){
            boolean esPali = Palindromos.esPalindroma(elem);
            if(esPali){
                System.out.println(elem+"\nes palíndroma\n");
            }else{
                System.out.println(elem+"\nno es palíndroma\n");
            }
        }
    }
}

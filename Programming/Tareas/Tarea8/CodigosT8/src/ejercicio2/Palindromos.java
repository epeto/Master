/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ejercicio2;

/**
 *
 * @author emmanuel
 */
public class Palindromos {
    /**
     * Decide si un caracter es alfabético.
     * @param c caracter a comprobar.
     * @return true si y sólo si c es un caracter alfabético.
     */
    private static boolean esAlfabetico(char c){
        int ic = (int) c;
        return (65 <= ic && ic <= 90) || (97 <= ic && ic <= 122);
    }
    
    /**
     * Recibe un caracter alfabético y lo convierte a minúscula.
     * @param c caracter a convertir.
     * @return c en minúscula.
     */
    private static char aMinuscula(char c){
        int ic = (int) c;
        if(65 <= ic && ic <= 90){
            ic += 32;
            char c2 = (char) ic;
            return c2;
        }else{
            return c;
        }
    }
    
    /**
     * Limpia una cadena de texto, dejando solo los caracteres alfabéticos.
     * @param cadena de entrada
     * @return la cadena pero sin los caracteres que no son alfabéticos.
     */
    private static String limpia(String cadena){
        String salida = "";
        for(int i=0; i<cadena.length(); i++){
            if(esAlfabetico(cadena.charAt(i))){
                salida += cadena.charAt(i);
            }
        }
        return salida;
    }
    
    /**
     * Recibe una cadena de caracteres alfabéticos y transforma cada letra a minúscula.
     * @param cadena a transformar a minúsculas.
     * @return la misma cadena pero con todas sus letras en minúscula.
     */
    private static String aMinusculas(String cadena){
        String salida = "";
        for(int i=0; i<cadena.length(); i++){
            salida += aMinuscula(cadena.charAt(i));
        }
        return salida;
    }
    
    /**
     * Comprueba si una cadena es palíndroma.
     * @param cadena a comprobar si es palíndroma.
     * @return true si y sólo si la cadena es palíndroma.
     */
    private static boolean esPalindromaAux(String cadena){
        int ini;
        int fin;
        int mitad = cadena.length()/2;
        for(ini = 0, fin = cadena.length()-1; ini<mitad; ini++, fin--){
            if(cadena.charAt(ini) != cadena.charAt(fin)){
                return false;
            }
        }
        return true;
    }
    
    public static boolean esPalindroma(String cadena){
        String cadenaLimpia = aMinusculas(limpia(cadena));
        return esPalindromaAux(cadenaLimpia);
    }
}

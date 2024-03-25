/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ejercicio1;

import java.util.LinkedList;
import java.util.Scanner;

/**
 *
 * @author emmanuel
 */
public class Average {
    /**
     * Recibe una lista de números y calcula el promedio.
     * @param listaNums lista de números.
     * @return promedio de los números de la lista que recibe.
     */
    public static double promedio(LinkedList<Double> listaNums) throws IllegalArgumentException {
        if(listaNums.isEmpty()){
            throw new IllegalArgumentException("La lista de números no debe ser vacía.");
        }
        double suma = 0.0;
        for(Double elem : listaNums){
            suma += elem;
        }
        double p = suma/listaNums.size();
        return p;
    }
    
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese la cantidad de números a promediar.");
        int n;
        try{
            n = Integer.parseInt(sc.nextLine());
        } catch (NumberFormatException nfe){
            System.err.println("El formato es inadecuado, debe ser un número entero.");
            System.out.println(nfe);
            n = 3; //si se equivoca, por defecto se ponen 3.
        }
        if(n>0){
            System.out.println("Ingrese "+ n +" números reales, separados por un salto de línea.");
        }
        LinkedList<Double> lista = new LinkedList<>();
        int cantidad = 0;
        while(cantidad < n){
            try{
                double d = Double.parseDouble(sc.nextLine());
                lista.add(d);
            }catch(NumberFormatException nfe){
                System.err.println("El formato es inadecuado, debe ser un número real.");
                System.out.println(nfe);
                lista.add(0.0);
            }finally{
                cantidad++;
            }
        }
        sc.close();
        
        double avg = 0.0;
        try{
            avg = promedio(lista);
        }catch(IllegalArgumentException iae){
            System.out.println(iae);
        }finally{
            System.out.println("Lista de números:\n"+lista);
            System.out.println("Promedio: "+avg);
        }
    }
}

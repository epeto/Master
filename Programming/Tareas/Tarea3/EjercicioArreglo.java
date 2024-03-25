
/**
 * @author: Emmanuel Peto Gutiérrez
 */

public class EjercicioArreglo{
    /**
     * Imprime el contenido de un arreglo de tipo int.
     * @param arr arreglo a imprimir
     */
    public static void imprimeArregloInt(int[] arr){
        System.out.print("[");
        for(int i=0; i<arr.length-1; i++){
            System.out.print(String.valueOf(arr[i]) + ", ");
        }
        System.out.println(String.valueOf(arr[arr.length-1]) + "]");
    }

    public static void main(String[] args){
        //Se crea un arreglo de tamaño 3.
        int[] arregloUno = new int[3];

        //Segundo arreglo igualado al primero.
        int[] arregloDos = arregloUno;
        
        //Se modifica el contenido del primero (se guarda (i+2)²)
        for(int i=0; i<arregloUno.length; i++){
            arregloUno[i] = (i+2)*(i+2);
        }
        
        //Se imprimen ambos arreglos.
        System.out.println("Arreglo uno:");
        imprimeArregloInt(arregloUno);
        System.out.println("Arreglo dos (identico al uno):");
        imprimeArregloInt(arregloDos);

        //Se crea una copia del arregloUno y se guarda en arregloTres
        int[] arregloTres = arregloUno.clone();
        //Se imprimen ambos
        System.out.println("\nArreglo uno:");
        imprimeArregloInt(arregloUno);
        System.out.println("Arreglo tres (clon del 1):");
        imprimeArregloInt(arregloTres);

        //Como evidencia de que el uno y el tres no son el mismo arreglo, se modifican y se imprimen.
        arregloUno[0] = 13;
        arregloTres[2] = 31;
        System.out.println("\nArreglos modificados.");
        System.out.println("Arreglo uno:");
        imprimeArregloInt(arregloUno);
        System.out.println("Arreglo tres:");
        imprimeArregloInt(arregloTres);
    }
}

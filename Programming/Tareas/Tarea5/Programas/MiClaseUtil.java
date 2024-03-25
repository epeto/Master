/**
 * En esta clase se define el método estático: maxInArray, que recibe un arreglo
 * de un tipo primitivo numérico y devuelve el elemento máximo de ese arreglo.
 * @author: Emmanuel Peto Gutiérrez
 */
public class MiClaseUtil{
    public static byte maxInArray(byte[] arr){
        byte maximo = arr[0];
        for(int i=1; i<arr.length; i++){
            if(arr[i] > maximo){
                maximo = arr[i];
            }
        }
        return maximo;
    }

    public static short maxInArray(short[] arr){
        short maximo = arr[0];
        for(int i=1; i<arr.length; i++){
            if(arr[i] > maximo){
                maximo = arr[i];
            }
        }
        return maximo;
    }

    public static int maxInArray(int[] arr){
        int maximo = arr[0];
        for(int i=1; i<arr.length; i++){
            if(arr[i] > maximo){
                maximo = arr[i];
            }
        }
        return maximo;
    }

    public static long maxInArray(long[] arr){
        long maximo = arr[0];
        for(int i=1; i<arr.length; i++){
            if(arr[i] > maximo){
                maximo = arr[i];
            }
        }
        return maximo;
    }

    public static float maxInArray(float[] arr){
        float maximo = arr[0];
        for(int i=1; i<arr.length; i++){
            if(arr[i] > maximo){
                maximo = arr[i];
            }
        }
        return maximo;
    }

    public static double maxInArray(double[] arr){
        double maximo = arr[0];
        for(int i=1; i<arr.length; i++){
            if(arr[i] > maximo){
                maximo = arr[i];
            }
        }
        return maximo;
    }
}
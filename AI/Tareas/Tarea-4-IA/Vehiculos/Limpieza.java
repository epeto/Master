
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Arrays;

public class Limpieza{

    /**
     * Lee un archivo
     * @param archivo nombre del archivo
     * @return lista con las líneas del archivo, separadas en un arreglo de strings.
     */
    public static ArrayList<String[]> lee(String archivo){
        ArrayList<String[]> lineas = new ArrayList<>();
        try{
            FileReader fr1 = new FileReader(archivo);
            BufferedReader br1 = new BufferedReader(fr1);
    
            String linea = br1.readLine(); //Lee la primera línea.
            while(linea!=null){ //Mientras no llegue al final, lee líneas.
                lineas.add(linea.split(","));
                linea = br1.readLine();
            }
            br1.close();
        }catch(Exception e){System.err.println("Archivo no encontrado");}
        return lineas;
    }

    /**
     * Recibe un número de columna y transforma sus elementos a números.
     * @param col número de columna
     * @param lista tabla
     */
    public static void transformaColumna(int col, ArrayList<String[]> lista){
        HashMap<String, Integer> tabla = new HashMap<>();
        int indice = 0;
        for(String[] fila : lista){
            String elem = fila[col];
            if(!tabla.containsKey(elem)){
                tabla.put(elem, indice);
                indice++;
            }
        }
        for(String[] fila : lista){
            fila[col] = tabla.get(fila[col]).toString();
        }
    }

    public static void escribe(ArrayList<String[]> lista){
        try{
            FileWriter fw1 = new FileWriter("datos_limpios.csv");
            BufferedWriter bw1 = new BufferedWriter(fw1);
            for(String[] linea : lista){
                String salida = "";
                for(int i=1; i<linea.length-1; i++){
                    salida += linea[i]+",";
                }
                salida += linea[linea.length-1];
                bw1.write(salida);
                bw1.newLine();
            }
            bw1.close();
        }catch(Exception e){
            System.out.println(e);
        }
    }

    public static void main(String[] args){
        String nombreArchivo = "CarPrice_Assignment.csv";
        ArrayList<String[]> lista = lee(nombreArchivo);
        int[] categoricas = {2, 3, 4, 5, 6, 7, 8, 14, 15, 17};
        for(int i : categoricas){
            transformaColumna(i, lista);
        }
        escribe(lista);
    }
}

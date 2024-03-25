
import java.util.LinkedList;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Random;
import java.io.BufferedWriter;
import java.io.FileWriter;

public class Separacion {
    public static LinkedList<String> lee(String archivo){
        LinkedList<String> lineas = new LinkedList<>();
        try{
            FileReader fr1 = new FileReader(archivo);
            BufferedReader br1 = new BufferedReader(fr1);
    
            String linea = br1.readLine(); //Lee la primera línea.
            while(linea!=null){ //Mientras no llegue al final, lee líneas.
                lineas.add(linea);
                linea = br1.readLine();
            }
            br1.close();
        }catch(Exception e){
            System.out.println(e);
            System.err.println("Archivo no encontrado");
        }
        return lineas;
    }

    public static void separa(LinkedList<String> total, LinkedList<String> parcial){
        Random rn = new Random();
        int tamPar = (int) (0.3*total.size());
        while(parcial.size() < tamPar){
            int indice = rn.nextInt(total.size());
            parcial.add(total.remove(indice));
        }
    }

    public static void escribe(LinkedList<String> total, LinkedList<String> parcial){
        try{
            FileWriter fw1 = new FileWriter("social70.csv");
            BufferedWriter bw1 = new BufferedWriter(fw1);
            for(String linea : total){
                bw1.write(linea);
                bw1.newLine();
            }
            bw1.close();
        }catch(Exception e){
            System.out.println(e);
        }

        try{
            FileWriter fw2 = new FileWriter("social30.csv");
            BufferedWriter bw2 = new BufferedWriter(fw2);
            for(String linea : parcial){
                bw2.write(linea);
                bw2.newLine();
            }
            bw2.close();
        }catch(Exception e){
            System.out.println(e);
        }
    }

    public static void main(String[] args){
        LinkedList<String> lista = lee("Social_Network_Ads.csv");
        LinkedList<String> otra = new LinkedList<>();
        separa(lista, otra);
        escribe(lista, otra);
    }
}

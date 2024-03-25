
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class Lector{

    ArrayList<String> lineas;

    //Constructor del lector.
    public Lector(){
        lineas = new ArrayList<String>();
    }

    /**
    * Método que lee línea a línea el archivo que recibe.
    * @param archivo: nombre del archivo a leer.
    */
    public void lee(String archivo){
        try{
            FileReader fr1 = new FileReader(archivo);
            BufferedReader br1 = new BufferedReader(fr1);
    
            String linea = br1.readLine(); //Lee la primera línea.
            while(linea!=null){ //Mientras no llegue al final, lee líneas.
                lineas.add(linea);
                linea = br1.readLine();
            }
            br1.close();
        }catch(Exception e){System.err.println("Archivo no encontrado");}
    }

    /**
     * Crea la lista de elementos a partir del archivo.
     * @param caja guardará la capacidad de la mochila.
     * @return lista de elementos
     */
    public ArrayList<Elemento> creaElementos(long[] caja){
        String[] fstLine = lineas.get(0).split(" ");
        caja[0] = Long.parseLong(fstLine[1]);
        ArrayList<Elemento> elementos = new ArrayList<>();
        for(int i=1; i<lineas.size(); i++){
            String[] par = lineas.get(i).split(" ");
            long valor = Long.parseLong(par[0]);
            long peso = Long.parseLong(par[1]);
            Elemento elem = new Elemento(i-1, valor, peso);
            elementos.add(elem);
        }
        return elementos;
    }

}





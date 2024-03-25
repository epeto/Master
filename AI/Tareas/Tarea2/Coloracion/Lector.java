
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
    * Método que crea una gráfica con el archivo de entrada.
    * @return objeto tipo gráfica.
    */
    public Grafica creaGrafica(){
        String[] verts = lineas.get(0).split(" ");
        //Se crea una gráfica.
        Grafica grafica = new Grafica(Integer.parseInt(verts[0]));
        //A partir de aquí se agregan las aristas.
        for(int i=1;i<lineas.size();i++){
            String[] ari = lineas.get(i).split(" ");
            int id0 = Integer.parseInt(ari[0]); //id del primer vértice.
            int id1 = Integer.parseInt(ari[1]); //id del segundo vértice.
            grafica.agregaArista(id0, id1); //Se agrega la arista a la gráfica.
        }
        return grafica;
    }
}






import java.io.BufferedReader;
import java.io.FileReader;
import java.util.LinkedList;
import java.util.HashMap;

public class Lector{

    LinkedList<String> lineas;

    //Constructor del lector.
    public Lector(){
        lineas = new LinkedList<String>();
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
        Grafica grafica = new Grafica();
        String[] verts = lineas.get(0).split(","); //Se separan los vértices por comas
        
        //Se agregan los vértices a la gráfica.
        for(int i=0;i<verts.length;i++){
            grafica.agregaVertice(verts[i]);
        }

        //A partir de aquí se agregan las aristas.
        for(int i=1;i<lineas.size();i++){
            String[] ari = lineas.get(i).split(",");
            String id0 = ari[0]; //id del primer vértice.
            String id1 = ari[1]; //id del segundo vértice.
            int peso = Integer.parseInt(ari[2]); //Peso de la arista.
            grafica.agregaArista(id0, id1, peso); //Se agrega la arista a la gráfica.
        }
        return grafica;
    }

    /**
     * Crea una tabla de distancias.
     * @return
     */
    public HashMap<String, Integer> creaTabla(){
        HashMap<String, Integer> tabla = new HashMap<>();
        for(String linea : lineas){
            String[] renglon = linea.split(",");
            tabla.put(renglon[0], Integer.parseInt(renglon[1]));
        }
        return tabla;
    }
}





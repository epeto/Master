
import java.util.HashSet;

public class Estado {
    public int[] colVert; //guarda el color de cada vértice.
    public int numColores; //número total de colores en este estado.

    public Estado(Grafica g){
        int n = g.getOrden();
        colVert = new int[n];
        for(int i=0; i<n; i++){
            colVert[i] = g.vertices[i].color;
        }
        HashSet<Integer> conjunto = new HashSet<>(); //para contar cuántos números diferentes hay.
        for(int idc : colVert){
            if(!conjunto.contains(idc)){
                conjunto.add(idc);
            }
        }
        numColores = conjunto.size();
    }

    public void copiaGrafica(Grafica g){
        int n = g.getOrden();
        colVert = new int[n];
        for(int i=0; i<n; i++){
            colVert[i] = g.vertices[i].color;
        }
        numColores = g.numColores;
    }
}


// Servirá para generar todos los estados de un tablero de gato.

import java.util.HashSet;
import java.util.Queue;
import java.util.LinkedList;
import java.util.List;
import java.util.Arrays;
import java.io.FileWriter;
import java.io.BufferedWriter;

public class Generador {

    public static int codigoHash(Integer[] tablero){
        int suma = 0;
        for(int i=0; i<tablero.length; i++){
            suma += tablero[i]*Math.pow(3, i);
        }
        return suma;
    }

    public static List<Integer> casillasDisponibles(Integer[] tablero){
        LinkedList<Integer> lista = new LinkedList<>();
        for(int i=0; i<tablero.length; i++){
            if(tablero[i] == 0){
                lista.add(i);
            }
        }
        return lista;
    }

    //Los estados válidos serán solo aquellos donde el número de
    //círculos sea igual al número de cruces
    public static boolean estadoValido(Integer[] tablero){
        int unos = 0;
        int dos = 0;
        for(Integer elem : tablero){
            if(elem == 1){
                unos++;
            }else if(elem == 2){
                dos++;
            }
        }
        return unos == dos;
    }

    //Determina si un estado es terminal
    public static boolean terminal(Integer[] tablero){
        int ceros = 0;
        for(int elem : tablero){
            if(elem == 0){
                ceros++;
            }
        }
        if(ceros == 0){ //Tablero lleno
            return true;
        }
        int ganador = 0;
        int i;
        for(i=0; i<3; i++){
            if(tablero[i*3] == tablero[i*3+1] && tablero[i*3+1] == tablero[i*3+2]){
                ganador = tablero[i*3];
                if(ganador != 0){
                    return true;
                }
            }
        }
        for(i=0; i<3; i++){
            if(tablero[i] == tablero[3+i] && tablero[3+i] == tablero[6+i]){
                ganador = tablero[i];
                if(ganador != 0){
                    return true;
                }
            }
        }
        if(tablero[0] == tablero[4] && tablero[4] == tablero[8]){
            ganador = tablero[0];
            if(ganador != 0){
                return true;
            }
        }
        if(tablero[2] == tablero[4] && tablero[4] == tablero[6]){
            ganador = tablero[2];
            if(ganador != 0){
                return true;
            }
        }
        return false;
    }

    public static List<Integer[]> sucesores(int turno, Integer[] tablero){
        List<Integer> disp = casillasDisponibles(tablero);
        LinkedList<Integer[]> sucs = new LinkedList<>();
        for(Integer casilla : disp){
            Integer[] sig = Arrays.copyOf(tablero, tablero.length);
            sig[casilla] = turno;
            sucs.add(sig);
        }
        return sucs;
    }

    public static void main(String[] args){
        HashSet<Integer> conjunto = new HashSet<>();
        Queue<Integer[]> cola = new LinkedList<>();
        Integer[] inicial = new Integer[9];
        for(int i=0; i<inicial.length; i++){
            inicial[i] = 0;
        }
        conjunto.add(codigoHash(inicial));
        cola.offer(inicial);
        while(!cola.isEmpty()){
            Integer[] actual = cola.poll();
            if(!terminal(actual)){
                int turno = (estadoValido(actual))? 1 : 2;
                List<Integer[]> sucAct = sucesores(turno, actual); //sucesores del actual
                for(Integer[] suc : sucAct){
                    int hc = codigoHash(suc);
                    if((estadoValido(suc) || terminal(suc)) && !conjunto.contains(hc)){
                        conjunto.add(hc);
                    }
                    cola.offer(suc);
                }
            }
        }
        System.out.println("Estados: "+String.valueOf(conjunto.size()));
        String salida = "";
        for(Integer estado : conjunto){
            salida += String.valueOf(estado)+" ";
        }
        try{
            FileWriter fw = new FileWriter("estados_ttt");
            BufferedWriter bw = new BufferedWriter(fw);
            bw.write(salida);
            bw.close();
            fw.close();
        }catch(Exception e){
            System.err.println("Error");
        }
    }
}

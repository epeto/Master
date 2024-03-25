
import java.util.PriorityQueue;
import java.util.HashMap;

public class Algoritmos {
    /**
     * Algoritmo de búsqueda en anchura.
     * @param g gráfica
     * @param origen id del vértice de origen
     * @param meta id del vértice meta
     */
    public static void anchura(Grafica g, String origen, String meta){
        for(Vertice v : g.vertices.values()){
            v.p = null;
            v.key = 0;
            v.costoCamino = 0;
            v.visitado = false;
        }

        Vertice vOrigen = g.getVertice(origen);
        PriorityQueue<Vertice> cola = new PriorityQueue<>();
        cola.offer(vOrigen);
        boolean metaEncontrada = false;
        if(origen.equals(meta)){
            metaEncontrada = true;
        }

        while(!cola.isEmpty() && !metaEncontrada){
            Vertice v = cola.poll();
            for(Pair<Vertice, Integer> par : v.ady){
                Vertice u = par.getKey();
                if(!u.visitado){
                    int peso = par.getValue();
                    u.visitado = true;
                    u.p = v;
                    u.key = v.key+1; //la llave guarda la profundidad
                    u.costoCamino = v.costoCamino + peso;
                    cola.offer(u);
                    if(u.id.equals(meta)){
                        metaEncontrada = true;
                    }
                }
            }
        }
    }

    /**
     * Algoritmo de búsqueda en profundidad
     * @param g gráfica
     * @param origen id de vértice de origen
     * @param meta id del vértice meta
     * @param maxDepth solo expande a los vértices que estén a una profundidad menor a este número
     */
    public static void profundidad(Grafica g, String origen, String meta, int maxDepth){
        for(Vertice v : g.vertices.values()){
            v.p = null;
            v.key = 0;
            v.costoCamino = 0;
            v.visitado = false;
        }

        Vertice vOrigen = g.getVertice(origen);
        //La cola de prioridad saca primero al que tenga la prioridad más pequeña
        //así que se guardará el negativo de la profundidad.
        PriorityQueue<Vertice> cola = new PriorityQueue<>();
        vOrigen.key = 0;
        vOrigen.costoCamino = 0;
        cola.offer(vOrigen);
        boolean metaEncontrada = false;
        if(origen.equals(meta)){
            metaEncontrada = true;
        }

        while(!cola.isEmpty() && !metaEncontrada){
            Vertice v = cola.poll();
            for(Pair<Vertice, Integer> par : v.ady){
                Vertice u = par.getKey();
                if(!u.visitado){
                    int peso = par.getValue();
                    u.visitado = true;
                    u.p = v;
                    u.key = v.key-1; //la llave guarda el negativo de la profundidad
                    u.costoCamino = v.costoCamino + peso;
                    if(Math.abs(u.key) < maxDepth){
                        cola.offer(u);
                    }
                    if(u.id.equals(meta)){
                        metaEncontrada = true;
                    }
                }
            }
        }
    }

    /**
     * Algoritmo de búsqueda iterativa.
     * @param g gráfica
     * @param origen id del vértice de origen
     * @param meta id del vértice meta
     */
    public static void iterativa(Grafica g, String origen, String meta){
        int maxDepth = 1; //profundidad máxima
        Vertice verticeMeta = g.getVertice(meta);

        while(!verticeMeta.visitado){
            profundidad(g, origen, meta, maxDepth);
            maxDepth++;
        }
    }

    /**
     * Algoritmo de búsqueda de costo uniforme.
     * @param g gráfica
     * @param origen id del vértice de origen
     * @param meta id del vértice meta
     */
    public static void costoUniforme(Grafica g, String origen, String meta){
        for(Vertice v : g.vertices.values()){
            v.p = null;
            v.key = 0;
            v.costoCamino = 0;
            v.visitado = false;
        }

        Vertice vOrigen = g.getVertice(origen);
        PriorityQueue<Vertice> cola = new PriorityQueue<>();
        cola.offer(vOrigen);
        boolean metaEncontrada = false;
        if(origen.equals(meta)){
            metaEncontrada = true;
        }

        while(!cola.isEmpty() && !metaEncontrada){
            Vertice v = cola.poll();
            for(Pair<Vertice, Integer> par : v.ady){
                Vertice u = par.getKey();
                if(!u.visitado){
                    int peso = par.getValue();
                    u.visitado = true;
                    u.p = v;
                    u.costoCamino = v.costoCamino + peso;
                    u.key = u.costoCamino; //la llave guarda el costo del camino
                    cola.offer(u);
                    if(u.id.equals(meta)){
                        metaEncontrada = true;
                    }
                }
            }
        }
    }

    /**
     * Algoritmo de búsqueda voraz
     * @param g gráfica
     * @param origen id del nodo origen
     * @param distancias tabla de distancias
     */
    public static void voraz(Grafica g, String origen, String meta, HashMap<String, Integer> distancias){
        for(Vertice v : g.vertices.values()){
            v.p = null;
            v.key = 0;
            v.costoCamino = 0;
            v.visitado = false;
        }
        Vertice vOrigen = g.getVertice(origen);
        PriorityQueue<Vertice> cola = new PriorityQueue<>();
        cola.offer(vOrigen);
        boolean metaEncontrada = false;
        if(origen.equals(meta)){
            metaEncontrada = true;
        }

        while(!cola.isEmpty() && !metaEncontrada){
            Vertice v = cola.poll();
            for(Pair<Vertice, Integer> par : v.ady){
                Vertice u = par.getKey();
                if(!u.visitado){
                    int peso = par.getValue();
                    u.visitado = true;
                    u.p = v;
                    //la llave guarda la distancia recta desde u hacia la meta
                    u.key = distancias.get(u.id);
                    u.costoCamino = v.costoCamino + peso;
                    cola.offer(u);
                    if(u.id.equals(meta)){
                        metaEncontrada = true;
                    }
                }
            }
        }
    }

    /**
     * Algoritmo de búsqueda A-estrella
     * @param g gráfica
     * @param origen id del nodo origen
     * @param distancias tabla de distancias
     */
    public static void aestrella(Grafica g, String origen, String meta, HashMap<String, Integer> distancias){
        for(Vertice v : g.vertices.values()){
            v.p = null;
            v.key = 0;
            v.costoCamino = 0;
            v.visitado = false;
        }
        Vertice vOrigen = g.getVertice(origen);
        PriorityQueue<Vertice> cola = new PriorityQueue<>();
        cola.offer(vOrigen);
        boolean metaEncontrada = false;
        if(origen.equals(meta)){
            metaEncontrada = true;
        }

        while(!cola.isEmpty() && !metaEncontrada){
            Vertice v = cola.poll();
            for(Pair<Vertice, Integer> par : v.ady){
                Vertice u = par.getKey();
                if(!u.visitado){
                    int peso = par.getValue();
                    u.visitado = true;
                    u.p = v;
                    u.costoCamino = v.costoCamino + peso;
                    //la llave guarda la distancia recta desde u hacia la meta
                    //más el costo del camino.
                    u.key = distancias.get(u.id) + u.costoCamino;
                    cola.offer(u);
                    if(u.id.equals(meta)){
                        metaEncontrada = true;
                    }
                }
            }
        }
    }
}

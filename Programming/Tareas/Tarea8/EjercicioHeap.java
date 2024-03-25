
import java.util.Arrays;

public class EjercicioHeap {
    private int id;
    
    public EjercicioHeap(int id) {
        this.id = id;
    }
    
    @Override
    public String toString(){
        return String.valueOf(id);
    }

    public static void main(String[] args) {
        EjercicioHeap[] eh = new EjercicioHeap[5];
        int x = 0;
        while (x < 5) {
            eh[x] = new EjercicioHeap(x);
            x++;
        }
        eh[0] = eh[3];
        eh[4] = eh[1];
        eh[3].id = 7;
        eh[1] = eh[2];
        eh[2] = eh[4];
        // continua
        System.out.println(Arrays.toString(eh));
    }
}

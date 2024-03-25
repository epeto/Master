
import java.util.Arrays;

public class EjercicioHeap{
    private int id = 0;

    @Override
    public String toString(){
        return "id="+String.valueOf(id);
    }

    public static void main(String[] args){
        EjercicioHeap[] eh = new EjercicioHeap[5];
        int x = 0;
        while(x < 5){
            eh[x] = new EjercicioHeap();
            eh[x].id = x;
            x++;
        }
        eh[0] = eh[3];
        eh[3] = eh[1];
        eh[3].id = 6;
        eh[2] = eh[4];
        eh[4] = null;
        eh[3] = eh[2];
        eh[4] = eh[0];

        System.out.println(Arrays.toString(eh));
    }
}
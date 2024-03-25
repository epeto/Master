
public class Matriz{
    protected int[][] mat;

    /**
     * Constructor de la clase Matriz.
     * @param n lado de la matriz.
     */
    public Matriz(int n){
        mat = new int[n][n];
        int k = 0;
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                mat[i][j] = k;
                k++;
            }
        }
    }

    //Calcula el número de dígitos de n
    private int numDigs(int n){
        if(n == 0){
            return 1;
        }
        int d = 0;
        while(n > 0){
            n /= 10;
            d++;
        }
        return d;
    }

    //Imprime la matriz
    public void imprimirMatriz(){
        int maxDig = 0;
        int n = mat.length;
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                int nd = numDigs(mat[i][j]);
                if(nd > maxDig){
                    maxDig = nd;
                }
            }
        }

        for(int i=0; i<n; i++){
            System.out.print("|");
            for(int j=0; j<n; j++){
                String espacios = " ";
                int nEsp = maxDig - numDigs(mat[i][j]);
                for(int k=0; k<nEsp; k++){
                    espacios += " ";
                }
                System.out.print(espacios+mat[i][j]);
            }
            System.out.println(" |");
        }
    }
}

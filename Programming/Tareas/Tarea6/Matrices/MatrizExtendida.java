public class MatrizExtendida extends Matriz {

    /**
     * Constructor de la clase MatrizExtendida.
     * @param n lado de la matriz.
     */
    public MatrizExtendida(int n){
        super(n);
    }

    /**
     * Toma la fila y la columna de la matriz y actualiza su valor.
     * @param i fila
     * @param j columna
     * @param valor nuevo
     */
    public void sustituirElemento(int i, int j, int valor){
        mat[i][j] = valor;
    }
}

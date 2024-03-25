
abstract class P1abs{
    int x = 0;
    public abstract void metodoAbstracto();

    abstract int add(int a, int b);

    public int cuadrado(int n){
        return n*n;
    }

    public P1abs(int var){
        x = var;
    }
}
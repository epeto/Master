
public class P1conc extends P1abs{

    @Override
    public void metodoAbstracto() {
        System.out.println("Implementación concreta del método abstracto");
    }

    @Override
    int add(int a, int b){
        return a+b;
    }

    public P1conc(){
        super(3);
    }

    public static void main(String[] args){
        P1conc ejemplar = new P1conc();
        ejemplar.metodoAbstracto();
        System.out.println(ejemplar.cuadrado(9));
    }
}
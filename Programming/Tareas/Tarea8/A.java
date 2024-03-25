
public class A {
    private A() {
        System.out.println("A");
    }
    
    private A(int i){
        this();
        System.out.println(i);
    }

    protected A(char c){
        this(5);
        System.out.println(c);
    }
}

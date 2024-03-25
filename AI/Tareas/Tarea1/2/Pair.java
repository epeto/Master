
/**
 * Es como la clase Pair de javafx, pero mejor la programo para no
 * tener que compilar con las bibliotecas de javafx.
 */

public class Pair<K, V> {
    private K key; // llave
    private V value; // valor

    public Pair(K llave, V valor){
        key = llave;
        value = valor;
    }

    public K getKey(){
        return key;
    }

    public V getValue(){
        return value;
    }

    @Override
    public int hashCode(){
        int n1 = (key == null)? 0 : key.hashCode();
        int n2 = (value == null)? 0 : value.hashCode();
        return n1 + n2;
    }

    @Override
    public String toString(){
        String s1 = (key == null)? "null" : key.toString();
        String s2 = (value == null)? "null" : value.toString();
        return "〈" + s1 + ", " + s2 + "〉";
    }

    @Override
    public boolean equals(Object o){
        if(o instanceof Pair<?, ?>){
            Pair<?, ?> par2 = (Pair<?, ?>) o;
            int both = 0;
            if(key == null){
                if(par2.getKey() == null){
                    both++;
                }
            }else{
                if(key.equals(par2.getKey())){
                    both++;
                }
            }

            if(value == null){
                if(par2.getValue() == null){
                    both++;
                }
            }else{
                if(value.equals(par2.getValue())){
                    both++;
                }
            }
            return both == 2;
        }else{
            return false;
        }
    }
}

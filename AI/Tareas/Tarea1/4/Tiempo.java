
import java.util.Calendar;

public class Tiempo {
    // Devuelve el tiempo actual
    public Calendar ahora(){ 
        return Calendar.getInstance();
    }

    // Establece un límite dependiendo de los segundos y lo devuelve
    public Calendar tiempoLimite(Calendar tiempo, int segundos){        
        tiempo.add(Calendar.SECOND, segundos);
        return tiempo;
    }

    // Usado para comparar si pasó el limite
    public boolean pasoLimite(Calendar tiempoLimite){ 
        boolean pasoLimite = false;
        Calendar ahora = ahora();
        
        if(ahora.compareTo(tiempoLimite) >= 1 ){
            pasoLimite = true;
        }
        
        return pasoLimite;
    }

    public static void main(String[] args){
        Tiempo tiempo = new Tiempo();
        boolean finalizar = false;
 
        Calendar limite = tiempo.tiempoLimite(tiempo.ahora(), 10);
        do{
           if(tiempo.pasoLimite(limite)){
              System.out.println("Pasó el límite de 10 segundos");
              finalizar = true;
           } else {
              System.out.println("Estoy en el ciclo");
           }     
        }while (!finalizar); // Mientras finalizar no sea igual a true
    }
}

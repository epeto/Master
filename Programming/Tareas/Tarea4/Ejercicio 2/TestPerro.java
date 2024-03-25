public class TestPerro {
    public static void main(String[] args){
        Perro[] pets = new Perro[3];
        pets[0] = new Perro("Tomas");
        pets[1] = new Perro("Chester", "Labrador");
        pets[2] = new Perro("Rayo", "Pitbull", 25.3f);

        System.out.println("LO QUE SÉ DE MIS MASCOTAS");
        for(int i=0; i<pets.length; i++){
            pets[i].describir();
        }

        System.out.println("\nESTOS SON LOS NOMBRES DE MIS PERROS:");
        for(int i = 0; i<pets.length; i++){
            System.out.println(pets[i].getNombre());
        }

        System.out.println("\nY CUANDO PASAN LOS TAMALES TODOS LADRAN");
        for (int i=0; i<pets.length; i++){
            pets[i].ladrar();
        }
    }
}

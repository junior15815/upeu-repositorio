//para lanzar hilos se hace desde objetos que heredan

public class unamas extends Thread{
    private int id;
    public unamas(int id){
        this.id = id;
    }
    public void run(){
        System.out.println("Soy el hilo: "+id);

    }
    public static void main(String[] args){
        unamas h1= new unamas(1);
        unamas h2= new unamas(2);
        unamas h3= new unamas(3);

        h1.start();
        h2.start();
        h3.start();

        System.out.println("Soy el hilo principal");
    }
}

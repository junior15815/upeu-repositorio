public class unade extends Thread {

    private int id;
    public unade(int id){
        this.id =id;

    }
    public void run(){
        System.out.println("Soy el hilo: "+id);
    }

    public static void main(String[] args){
        unade[] vec = new unade[5];
        
        for(int i = 0; i < vec.length; i++){
        vec[i] = new unade (i+1);
        
        }
        vec[0].start();
        
        System.out.println("Soy el hilo principal");
    }
}
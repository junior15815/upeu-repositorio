import java.util.Random;

public class tarea extends Thread{
    private static double[] vec = new double[80000000] ; //10.000.000
    private int inicio, fin;

    public tarea(int inicio, int fin){
        this.inicio = inicio;
        this.fin = fin;
    }
    public static void main(String[] args){
    iniciavec();
    //opsion NO sonsurrente:
    vec_NOconcurrente();
    //opsion concucrente:
    vec_concurrente();
    }
    //Metede que indicia el vector estatice con valores. aleatorios
    private static void iniciavec(){
        Random rand = new Random(System.nanoTime());

        for(int i = 0; i < vec.length; i++){
            vec[i] = rand.nextInt();
        }
    }
 

    //Metode que NO utiliza el paralelisme y por tante se eiecuta de forma secuensial
    private static void vec_NOconcurrente(){
        double tiempo = System.nanoTime();
        for(int i = 0; i < vec.length; i++){
            vec[i] /= 10;
            vec[i] *= 10;
            vec[i] /= 10;
        }

        System.out.println("Version NO concurrente:"+ ((System.nanoTime() - tiempo) / 1000000) + "milisegundos" );
    }
    //Metodo que siscuta les hiles que que se Janzan
    public void run(){
        for(int i= inicio; i < fin; i++){
            vec[i] /= 10;
            vec[i] *= 10;
            vec[i] /= 10;
        }
    }

    //Mmetedo que siscuta npres hiles en paralele y que Maman al metado run para realizar Ja multiplicacion del
    //vector de forma paralela
    private static void vec_concurrente(){
        int nproc = Runtime.getRuntime().availableProcessors(); //Deyuelve cuantos nucleos tiene la CPU
        int inicio = 0, fin = 0;
        tarea[] prin = new tarea[nproc];
        double tiempo = System.nanoTime(); //Comienzo para capturar. el tiempo que tarda en ejecutarse
        
        for(int i = 0; i < nproc; i++){//multiplicacion del vector por los nares hilos.
            inicio = fin;
            fin += vec. length/nproc;
            prin[i] = new tarea(inicio, fin);
            prin[i].start();
        }
        for(int i = 0; i < nproc; i++){
            try{
                prin[i].join();
            }catch(Exception e){}
        }
        System.out.println("Version Concurrente: "+((System.nanoTime() - tiempo) / 1000000) + "milisegundos");
    }
 
}


import java.util.Random;

//Mulsiplicar por. 10 todos les elementos de una matriz de forma concucnente y medin el tiempo.
public class principal extends Thread{
    private static int tam = 4;
    private static int[][] matriz = new int[tam] [tam]; 
    private int inicio, fin;

    public principal(int inicio, int fin){
        this.inicio = inicio;
        this.fin = fin;
    }

    public void run(){
        for (int i = inicio; i < fin; i++){
            for(int j = 0; j < matriz[0].length; j++){
                matriz[i] [j] *=10;
            }
        }
    }

    public static void main(String[] args){
        Random rand = new Random(System.nanoTime());
        for(int i = 0; i < matriz.length; i++){
            for(int j = 0; j < matriz[0].length; j++){
                matriz[i][j] = rand.nextInt(10);
            }
        }
        principal h1 = new principal(0, 2);
        principal h2 = new principal(2, 4);

        h1.start();
        h2.start();
        try{
            h1.join();
            h2.join();
        }catch(Exception e){}
        for(int i = 0; i < matriz.length; i++){
            for(int j = 0; j < matriz[0].length; j++){
            System.out.print(matriz[i][j]+" ");
            
            }
            System.out.println();
        }
    }
}
public class first{
    public static void main(String[]args){
        getSmallest(3,0,2);
    }

    public static void getSmallest(int x, int y, int z){
        System.out.println(Math.min(Math.min(x, y), z));
    }
}
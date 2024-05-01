import java.util.Arrays;

public class RunningSumArray {
    public static void main (String [] args){
        int[] num = {3,1,2,10,1};
        System.out.print(Arrays.toString(RunningSum(num)));
    }

    static int[] RunningSum(int[] num){
        //My Code
        /*int sum = 0;
        int[] result = new int[num.length];
        for(int i=0;i<num.length;i++){
            sum = num[i] + sum;
            result[i] = sum;
        }
        return result;*/

        int[] result = new int[num.length];
        result[0] = num[0];

        for(int i = 1; i<num.length; i++){
            result[i] = result[i - 1] + num[i]; 
        }
        return result;

        //Overwritting input
        /*for(int i = 1; i<num.length;i++){
            num[i] = num[i-1] + num[i];
        }
        return num;*/
    }
}

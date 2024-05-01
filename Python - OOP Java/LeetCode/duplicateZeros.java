
/*
 * Input: arr = [1,0,2,3,0,4,5,0]
 * Output: [1,0,0,2,3,0,0,4]
 */
import java.util.Arrays;

public class duplicateZeros {
    public static void main(String[] args) {
        int[] arr = { 1, 0, 2, 3, 0, 4, 5, 0 };
        duplicateZeros(arr);
        System.out.print(Arrays.toString(arr));
    }

    static void duplicateZeros(int[] arr) {
        // iterate every element without hitting the bounds
        for (int i = 0; i < arr.length - 1; i++) {

            // Check if the current index is 0
            if (arr[i] == 0) {

                // duplicate the values from left to right of the value of j
                for (int j = arr.length - 2; j > i; j--) {
                    arr[j + 1] = arr[j];
                }

                // Set 0 next to the current 0
                arr[i + 1] = 0;

                // To ignore the second 0;
                i++;
            }
        }

        // Method 2
        /*
         * //iterate every element from the second to the last element
         * for(int i = arr.length - 2; i>=0; i--){
         * 
         * //Check if i is 0
         * if (arr[i] == 0){
         * 
         * //Move the values from left to right start from left to right
         * for(int j = arr.length - 2; j > i; j--){
         * arr[j + 1] = arr[j];
         * 
         * }
         * //Change values
         * arr[i + 1] = 0;
         * }
         * }
         */
    }
}

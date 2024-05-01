import java.util.Arrays;

public class MergeSortArray{

    public static void main(String []args){
        int[] nums1 = {1,2,3,0,0,0};
        int[] nums2 = {2,5,6};
        int n = 3;
        
        merge(nums1, nums2, n);
    }

    static void merge(int[] nums1, int[] nums2, int n){
        //iterate the array nums1
        for(int i = 0; n > 0; i++){
            
            //Check if it is 0 and replace it with the last 
            if(nums1[i] == 0){
                nums1[i] = nums2[n - 1];
                n--;
            }  
        }

        //Sort the array nums1
        Arrays.sort(nums1);

        System.out.print(Arrays.toString(nums1));
    }
}
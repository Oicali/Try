//Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

import java.util.Arrays;

public class AddTwoSum {

    public static void main(String[] args) {
        //Case 1
        int[] nums = {2,5,5,11};
        int target = 10;

        System.out.print(Arrays.toString(twoSum(nums, target)));
    }

    static int[] twoSum(int[] nums, int target) {
        int[] output = new int[2];
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length ; j++) {
                if (nums[i] + nums[j] == target) {
                    output[0] = i;
                    output[1] = j;
                    return output;

                    //return new int[] { i, j };
                }
            }
        }
        throw new IllegalArgumentException("No two numbers add up to target.");
    }
}

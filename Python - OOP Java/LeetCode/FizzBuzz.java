//Create a Function that takes a number as an argument and returns "Fizz", "Buzz", or "FizzBuzz"
//If number is a multiple of 3, print "Fizz"
//If number is a multiple of 5, print "Buzz"
//If number is a multiple of 3 and 5, print "FizzBuzz"
//If number is a not multiple of 3 and 5, print number

public class FizzBuzz {
    public static void main(String[] args) {

        System.out.println(Fizz_Buzz(3));
        System.out.println(Fizz_Buzz(5));
        System.out.println(Fizz_Buzz(15));
        System.out.println(Fizz_Buzz(4));

    }

    static String Fizz_Buzz(int num) {
        if (num % 3 == 0 && num % 5 == 0) {
            return "FizzBuzz";
        } else if (num % 3 == 0) {
            return "Fizz";
        } else if (num % 5 == 0) {
            return "Buzz";
        } else {
            return String.valueOf(num);
        }

        /*
         * # Method 1
         * if (num%3 == 0){
         * word = "Fizz";
         * }
         * elif (num%5 == 0){
         * word = "Buzz";
         * }
         * elif (num%5 == 0){
         * word = "FizzBuzz";
         * }
         * else {
         * word = String.valueOf(num);
         * }
         * 
         * 
         * # Method 2 
         * String word = "";
         * 
         * if (num % 3 == 0) {
         * word = word.concat("Fizz");
         * }
         * if (num % 5 == 0) {
         * word = word.concat("Buzz");
         * }
         * if (num % 3 != 0 && num % 5 != 0) {
         * word = String.valueOf(num);
         * }
         * return word;
         */
    }
}
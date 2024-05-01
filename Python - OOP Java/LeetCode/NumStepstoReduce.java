public class NumStepstoReduce {
    public static void main(String []args){
        System.out.println(numSteps(8));
        System.out.println(numSteps(14));
    }

    static int numSteps(int n){
        int steps = 0;

        while(n>0){
            boolean divisibleBy2 = n % 2 == 0;
            boolean notEqualsZero = n != 0;

            if (divisibleBy2){
                n /= 2;
            }
            else if(notEqualsZero){
                n -= 1;
            }

            steps++;
        }
        return steps;
    }
}

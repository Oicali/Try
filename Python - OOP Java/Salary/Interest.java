public class Interest {
    
    private static double computeInterest(double loanableAmount, int numMonth){
        double rate = 0;

        if(numMonth<=5){
            rate = 0.0062;
        }
        else if(numMonth<=10){
            rate = 0.0065;
        }
        else if(numMonth<=15){
            rate = 0.0068;
        }
        else if(numMonth<=20){
            rate = 0.0075;
        }
        else if(numMonth<=25){
            rate = 0.0080;
        }

        double interest = loanableAmount * numMonth * rate;
        return interest;
    }

    public static double getInterest(double loanableAmount, int numMonth){
        return computeInterest(loanableAmount, numMonth);
    }
}


public class LoanAmount {
    
    private static double computeLoan(double salary){
        double LoanableAmount = salary * 2.5;
        return LoanableAmount;
    }

    public static double getLoan(double salary){
        return computeLoan(salary);
    }
}

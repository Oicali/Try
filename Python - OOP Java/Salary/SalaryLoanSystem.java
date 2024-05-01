import java.util.Scanner;


public class SalaryLoanSystem {
    public static void main(String []args){
        Scanner input = new Scanner(System.in);

        System.out.print("Enter Salary: ");
        double salary = input.nextDouble();

        System.out.print("Enter months: ");
        int numMonth = input.nextInt();

        //Print the loan
        double loan = LoanAmount.getLoan(salary);
        System.out.println("Loanable Amount: " + loan);

        //print the interest
        double interest = Interest.getInterest(loan, numMonth);
        System.out.println("Amount of interest: " + interest);



        
    }
}

public class RichestCustomerWealth {
    public static void main(String[] args) {
        int[][] accounts = { { 7, 1, 3 }, { 2, 8, 7 }, { 1, 9, 5 } };
        System.out.print(wealthiestiest(accounts));
    }

    static int wealthiestiest(int[][] accounts) {
        int wealthiest = 0;

        // iterate for every row
        for (int i = 0; i < accounts.length; i++) {
            int currentTotal = 0;
            // iterate and add the numbers for every column

            for (int j = 0; j < accounts[i].length; j++) {
                currentTotal += accounts[i][j];
            }
            
            // Check the total
            if (currentTotal > wealthiest) {
                wealthiest = currentTotal;
            }

            //Short hand if - else
            //wealthiest = (currentTotal > wealthiest) ? currentTotal : wealthiest;

            // remove if statement:
            // wealthiest = Math.max(wealthiest, currentTotal);

        }
        return wealthiest;
    }
}

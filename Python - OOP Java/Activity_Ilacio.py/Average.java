public class Average{

    int num1, num2, num3;
    double Average;

    Average(int num1, int num2, int num3){
        this.num1 = num1;
        this.num2 = num2;
        this.num3 = num3;

        //Average = (double)(num1+num2+num3)/3;
        Average = (num1+num2+num3)/3.0;

        System.out.println("Your average: " + Average);
    }
}
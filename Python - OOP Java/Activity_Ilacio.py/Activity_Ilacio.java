import java.util.Scanner;

public class Activity_Ilacio {
    public static void main(String []args){
        Scanner input = new Scanner(System.in);

        //PART 1
        //Call a method
        Print();

        //PART 2
        //Create a new object
        Person p1 = new Person("Ariel Delos Santos", 19, "New Patient");

        //Print the attributes
        System.out.println("Full name: " + p1.getName());
        System.out.println("Age: " + p1.getAge());
        System.out.println("Status: " + p1.getStatus());


        //PART 2
        //Input the following 
        System.out.print("Enter your nickname: ");
        String nickname = input.nextLine();

        System.out.print("Enter your favorite vegetable: ");
        String vegetable = input.nextLine();

        System.out.print("Enter your favorite fruit: ");
        String fruit = input.nextLine();

        System.out.print("Enter your favorite subject: ");
        String subject = input.nextLine();

        System.out.print("Enter your favorite teacher: ");
        String teacher = input.nextLine();

        //Create a new object for person
        Person p2 = new Person(nickname, vegetable, fruit, subject, teacher);

        //Print
        System.out.println("\nHello, " + p2.getNickname() + "! Your body is healthy because you eat your favorite vegetable, " + p2.getVegetable() + ".");
        System.out.println("Let's go to the market and buy your favorite " + p2.getFruit() + ".");
        System.out.println("Wow! Your favorite teacher, " + p2.getTeacher() + ", is a great person.");
        System.out.println(p2.getSubject() + "? Now that's a terrific subject.");


        //PART 4 
        System.out.println("\nSample output:");
        //Input 3 numbers
        System.out.print("Enter Input number 1: ");
        int num1 = Integer.parseInt(input.nextLine());

        System.out.print("Enter Input number 2: ");
        int num2 = Integer.parseInt(input.nextLine());

        System.out.print("Enter Input number 3: ");
        int num3 = Integer.parseInt(input.nextLine());

        //Instantly average the numbers
        new Average(num1, num2, num3);
    }


    static void Print(){
        System.out.println("Hi and welcome to my first activity, my name is Jairus!");
    }
}

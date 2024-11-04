/**
 * cw1030
 * program will demo reptition structures
 */
   
import java.util.Scanner;
public class cw1030
{

    public static void main(String[] args)
    {
        Scanner k = new Scanner(System.in);
        /*String choice = "yes";
        while(choice.equalsIgnoreCase("yes"))
        {
            System.out.println("LaRicia");
            System.out.print("Would you like to run the program again? Enter yes or no:");
            choice = k.next();
        }
        System.out.println("Program has exited!");
        k.close();
        */


        System.out.print("Enter number of grades to average: ");
        int num = k.nextInt();
        int count;
        double total = 0;
        for(count = 0; count < num; count++ )
        {
            System.out.print("Enter a grade; ");
            int grade = k.nextInt();
            total + grade ;
        }
        System.out.println(total);
        k.close();
    }
}


/**
 * cw1030
 * program will demo reptition structures
 */

import java.util.Scanner;
    public class cw1030
    {

    public static void main(String[] args)
    {
        Scanner k = new Scanner(System.in);
    /*String choice = "yes";
    while(choice.equalsIgnoreCase("yes"))
        {
        System.out.println("LaRicia");
        System.out.print("Would you like to run the program again? Enter yes or no:");
        choice = k.next();
    }
    System.out.println("Program has exited!");
    */


        System.out.print("Enter number of grades to average: ");
        int num = k.nextInt();
        int count;
        double total = 0;
        for(count = 1; count < num; count++ )
        {
            System.out.print("Enter a grade #" + count+ ": ");
            int grade = k.nextInt();
            while (grade < 0 || grade > 100);
            {
                System.out.println("Bad grade Try again");
                System.out.println("Grades must be between 1 and 100 only!");
                System.out.print("Enter a grade #" + count+ ": ");
                grade = k.nextInt();3

            }
            total += grade;
        }
        System.out.println(total);
        k.close();
        
    }
}

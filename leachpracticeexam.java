/**
 * leachFinalExam
 */
import java.util.Scanner;
public class leachFinalExam
{

    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        displayInfo();
        float payRate = getRate(in);
        float hours = getHours(in);
        float grossPay = calculateGrossPay(payRate, hours);
        displayRHGrossPay(payRate, hours, grossPay);

    }
    public static void displayInfo()
    {
        System.out.println("LaRicia Leach");
        System.out.println("Dec 09, 2024");
        System.out.println("Find the gross pay for an individual");
    }
    public static float getRate(Scanner in)
    {
        System.out.print("Enter Pay Rate here: ");
        float payRate = in.nextFloat();
        return payRate;
    }
    public static float getHours(Scanner in)
    {
        System.out.print("Enter hours here: ");
        float hours = in.nextFloat();
        return hours;
    }
    public static float calculateGrossPay(float a, float b)
    {
        float grossPay = a*b;
        return grossPay;
    }
    public static void displayRHGrossPay(float payRate, float hours, float grossPay)
    {
        System.out.println();
        System.out.println("The pay rate is $" + payRate);
        System.out.println("The hours worked are " + hours);
        System.out.println("The gross pay is $" + grossPay);
    }
}

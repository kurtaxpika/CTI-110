/**
 * M7HW1_Leach
 */
import java.util.Scanner;
public class M7HW1_Leach
{

    public static void main(String[] args) 
    {
        runProgram();
    }
    public static void runProgram()
    {
        Scanner in = new Scanner(System.in);
        String keep_going = "yes";
        while(keep_going.equalsIgnoreCase("yes"))
            {
                displayInfo();
                int widgetsSold = getSales();
                int widgetsReturned = getReturns();
                int netWidgetsSold = calWidSold(widgetsSold, widgetsReturned);
                double widgetsSalesAmount = calWidSalesAmt(netWidgetsSold, 4.79);
                double commissionAmount = calComm(netWidgetsSold, widgetsSalesAmount);
                double monthlySalary = calSalary(2000, commissionAmount);
                // all calls to your function/methods should come from runProgram()  method only
                displayValues(widgetsSold, widgetsReturned, netWidgetsSold, widgetsSalesAmount, commissionAmount, monthlySalary);
                System.out.print("Do you want to run the program again? Enter yes or no: ");
                keep_going = in.next();
                System.out.println();
            }
        in.close();
        System.out.println("Program has terminated!");
    }
    public static void displayInfo()
    {
        System.out.println();
        System.out.println("LaRicia Leach");
        System.out.println();
        System.out.println("M7HW1 solution");
        System.out.println();
    }
    // create your functions/methods here
    public static int getSales()
    {
        int total = 0;
        int count, week;
        Scanner k = new Scanner(System.in);
            
        for (count = 1; count < 5; count++)
        { 
            System.out.print("Enter the amount of widgets sold in week " + count + ": ");
            week = k.nextInt();
            total += week;
        }
        return total;
    }
    public static int getReturns()
    {
        int total = 0;
        int count, week;
        Scanner k = new Scanner(System.in);
            
        for (count = 1; count < 5; count++)
        { 
            System.out.print("Enter the amount of widgets returned in week " + count + ": ");
            week = k.nextInt();
            total += week;
        }
        return total;
    }
    public static int calWidSold(int widgetsSold, int widgetsReturned)
    {
        return widgetsSold - widgetsReturned;

    }
    public static double calWidSalesAmt(int netWidgetsSold, double PRICE)
    {
        return netWidgetsSold * PRICE;
    }
    public static double calComm(int netWidgetsSold, double widgetsSalesAmount)
    {
        //Commision
        double commRate;
        if (netWidgetsSold <=100)
        {
            commRate = .1;
        }
        else if (netWidgetsSold < 200)
        {
            commRate = .15;
        }
        else if (netWidgetsSold < 300)
        {
            commRate = .2;
        }
        else
        {
            commRate = .25;
        }
        // Calculations
        return commRate * widgetsSalesAmount;
    }
    public static double calSalary(double SALARY, double commissionAmount)
    {
        return SALARY + commissionAmount;
    }
    public static void displayValues(int widgetsSold, int widgetsReturned, int netWidgetsSold, double widgetsSalesAmount, double commissionAmount, double monthlySalary)
    {
        System.out.println();
        System.out.println("Sales Person: LaRicia Leach");
        System.out.println("Widgets Sold: " + widgetsSold);
        System.out.println("Widgets Returned: " + widgetsReturned);
        System.out.println("Net Widgets Sold: " + netWidgetsSold);
        System.out.println("Widgets Sales Amount $" + widgetsSalesAmount);
        System.out.println("Commission Amount: $" + commissionAmount);
        System.out.println("Monthly Salary: $" + monthlySalary);
    }
}

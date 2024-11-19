/**
 * M5HW2_Leach
 */
import java.util.Scanner;
public class M5HW2_Leach
{

    public static void main(String[] args)
    {
        Scanner k = new Scanner(System.in);
        // variables
        String name, choice = "yes";
        System.out.print("Enter Sales Person Name: ");
        name = k.nextLine();
        while (choice.equalsIgnoreCase("yes"))
        {
            final double  widgetsSalesAmount, PRICE = 4.79, SALARY = 2000;
            double commRate, commissionAmount, monthlySalary;
            int widgetsSold, widgetsReturned, netWidgetsSold, totWidgetsSold = 0, month = 0, totWidgetsReturned = 0, weeks = 4, i;
            
            // for loop for widgets sold
            for(i = 1;i <= weeks; i++)
            {
                System.out.print("Enter Widgets sold for week #" + i + ": ");
                widgetsSold = k.nextInt();
                totWidgetsSold += widgetsSold;
            }
            
            // widgets returned for loop
            for(i = 1;i <= weeks; i++)
            {
                System.out.print("Enter Widgets returned for week #" + i + ": ");
                widgetsReturned = k.nextInt();
                totWidgetsReturned += widgetsReturned;
            }
    
            // Net widgets sold calculations
            netWidgetsSold = totWidgetsSold - totWidgetsReturned;
            
            // Widgets Sales Amount
            widgetsSalesAmount = netWidgetsSold * PRICE;
            

            //Commision
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
            commissionAmount = commRate * widgetsSalesAmount;
            monthlySalary = SALARY + commissionAmount;
            month += 1;

            // Result
            System.out.println();
            System.out.println("Sales Person: " + name);
            System.out.println("Month # " + month);
            System.out.println("Widgets Sold: " + totWidgetsSold);
            System.out.println("Widgets Returned: " + totWidgetsReturned);
            System.out.println("Net Widgets Sold: " + netWidgetsSold);
            System.out.println("Widget Sales Amount: $" + widgetsSalesAmount);
            System.out.println("Commission Amount: $" + commissionAmount);
            System.out.println("Monthly Salary: $" + monthlySalary);


            System.out.println();
            System.out.print("Would you like to run the program again? Enter yes or no: ");
            choice = k.next();
            
        }
        k.close();
        System.out.println();
        System.out.println("Program has exited!");
    }
}

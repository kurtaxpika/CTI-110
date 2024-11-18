import java.util.Scanner;

/**
 * M5HW1_starter_file
 */
import java.util.Scanner;
public class M5HW1_starter_file
 {

    public static void main(String[] args)
    {
        double average = 90;
        char grade;
        Scanner k = new Scanner(System.in);
            if (average >= 90)
                {
                    grade = 'A';
                }
            else if (average >= 80)
                {
                    grade = 'B';
                }
            else if (average >= 70)
                {
                    grade = 'C';
                }
            else if (average >= 60)
                {
                    grade = 'D';
                }
            else
                {
                    grade = 'F';
                }
            
            System.out.println("Grade is " + grade);
    }
}

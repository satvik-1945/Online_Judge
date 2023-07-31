import java.util.Scanner;

public class CalculateSum {
    public static void main(String[] args) {
        double num1, num2;
        Scanner scanner = new Scanner(System.in);

        // Input the first number
        num1 = scanner.nextDouble();

        // Input the second number
        num2 = scanner.nextDouble();

        // Close the scanner to release resources
        scanner.close();

        // Add two numbers
        double sum = num1 + num2;

        // Display the sum
        System.out.println(sum);
    }
}


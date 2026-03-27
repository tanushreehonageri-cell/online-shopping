import java.util.Scanner;

public class Calculator {

    // Method to perform calculation based on operator
    public static double calculate(double num1, double num2, char operator) {
        switch (operator) {
            case '+':
                return num1 + num2;
            case '-':
                return num1 - num2;
            case '*':
                return num1 * num2;
            case '/':
                if (num2 == 0) {
                    throw new ArithmeticException("Division by zero is not allowed.");
                }
                return num1 / num2;
            default:
                throw new IllegalArgumentException("Invalid operator. Use +, -, *, or /.");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // Input first number
            System.out.print("Enter first number: ");
            if (!scanner.hasNextDouble()) {
                System.out.println("Invalid input. Please enter a numeric value.");
                return;
            }
            double num1 = scanner.nextDouble();

            // Input operator
            System.out.print("Enter operator (+, -, *, /): ");
            String opInput = scanner.next();
            if (opInput.length() != 1) {
                System.out.println("Invalid operator format.");
                return;
            }
            char operator = opInput.charAt(0);

            // Input second number
            System.out.print("Enter second number: ");
            if (!scanner.hasNextDouble()) {
                System.out.println("Invalid input. Please enter a numeric value.");
                return;
            }
            double num2 = scanner.nextDouble();

            // Perform calculation
            double result = calculate(num1, num2, operator);
            System.out.printf("Result: %.2f %c %.2f = %.2f%n", num1, operator, num2, result);

        } catch (ArithmeticException | IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}
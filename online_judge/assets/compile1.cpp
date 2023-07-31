#include <iostream>

int main() {
    try {
        // Input the first number
        double num1;
        std::cin >> num1;

        // Input the second number
        double num2;
        std::cin >> num2;

        // Add two numbers
        double sum_result = num1 + num2;

        // Display the sum
        std::cout << sum_result << std::endl;
    }
    catch (const std::exception& e) {
        std::cout << "Invalid input. Please enter valid numbers." << std::endl;
    }

    return 0;
}

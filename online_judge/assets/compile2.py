def main():
    try:
        # Input the first number
        num1 = int(input())

        # Input the second number
        num2 = int(input())

        # Add two numbers
        sum_result = num1 * num2

        # Display the sum
        print(sum_result)

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()

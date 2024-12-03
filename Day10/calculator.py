def calculator():
    """
    A simple interactive calculator that supports basic arithmetic operations.
    Handles user input with error checking and provides a clean user interface.
    """
    # Define operations as a dictionary for more efficient and cleaner operation handling
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }

    while True:
        # Clear and concise menu display
        print("\n---> Calculator Menu <---")
        print("Operations: + - * /")
        print("Type 'q' to exit")

        # Get user input with error handling
        try:
            user_input = input("Enter operation: ").strip().lower()

            # Check for exit condition
            if user_input == 'q':
                print("Exiting calculator. Goodbye!")
                break

            # Validate operation
            if user_input not in operations:
                raise ValueError("Invalid operation")

            # Get numbers with error handling
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Handle division by zero
            if user_input == '/' and num2 == 0:
                print("Error: Cannot divide by zero!")
                continue

            # Perform calculation using dictionary of lambda functions
            result = operations[user_input](num1, num2)
            
            # Format output for readability
            print(f"{num1} {user_input} {num2} = {result}")

        except ValueError as e:
            # Catch and handle various input errors
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Run the calculator
if __name__ == "__main__":
    calculator()
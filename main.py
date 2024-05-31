# Import the logo module to display the logo
from logo import logo
# Define functions for basic arithmetic operations
def addition(a , b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        # Check for division by zero
        return "Error! Division by zero"
    return a / b
# Dictionary mapping operator symbols to corresponding functions
operations = {
    "+" : addition,
    "-" : subtraction,
    "*" : multiplication,
    "/" : division
}
# Main calculator function
def calculator():
    # Print the calculator logo
    print(logo)
    # Get the first number from the user
    num1 = float(input("What is the first number? "))
    # Boolean flag to control loop continuation
    should_continue = True
    # Main loop for calculator functionality
    while should_continue:
        # Display available operations
        for symbol in operations:
            print(symbol)
        # Get operation choice from the user
        operation_symbol = input("Pick an operation: ")
        # Get the second number from the user
        num2 = float(input("What is the next number? "))

        # Perform the calculation based on the chosen operation
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        # Print the result of the calculation
        print((f"{num1} {operation_symbol} {num2} = {answer}"))

        # Ask the user if they want to continue, start a new calculation, or exit
        decision = input(f"Type 'y' to continue calculating  with {answer}, type 'n' to start new calculation or type 'e' to exit: ")
        # Continue calculating with the result
        if decision == "y":
            num1 = answer
        # Start a new calculation
        # Note: Recursive calls may lead to stack overflow if used excessively.
        elif decision == "n":
            should_continue = False
            calculator()
        # Exit the calculator
        else:
            should_continue = False
            print("Bye Bye")
# Call the main calculator function to start the program
calculator()
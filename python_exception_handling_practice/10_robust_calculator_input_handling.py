'''
Exercise 10: Robust Calculator Input Handling

You are developing a calculator app that can perform basic arithmetic operations.
The app should robustly handle user input, ensuring that only numerical values are accepted and operations are performed correctly.

**Instructions**:

1. Ask the user to enter two numbers.
2. Ask the user to choose an operation (addition, subtractions, multiplication, or division).
3. Perform the operation and display the result.
4. Use a 'try-except' block to handle 'ValueError' and 'TypeError' exceptions.
5. No matter what happens, thank the user for using the calculator in a 'finally' block.

**Hints**:

- Use 'float()' to convert the input strings to numbers.
- Use an 'if-elif-else' structure to perform the chosen operation.
- In the 'except' blocks, handle 'ValueError' for non-numeric input and 'TypeError' for incorrect operations (like division by zero).
- Use the 'finally' block to print a thank-you message.
'''


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number. Please try again.")

def get_operation():
    operations = ['+', '-', '*', '/']
    while True:
        op = input("Choose an operation (+, -, *, /): ")
        if op in operations:
            return op
        print("Invalid operation. Please choose +, -, *, /")
        # why does this not need an "else"?


num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")
operation = get_operation()

try:
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2 
    print(f"The result is: {result}")
except TypeError:
    print("An unexpected type error occurred.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Thank you for using the calculator!")
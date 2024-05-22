'''
Exercise 3: The Safe Calculator

In a terminal-based calculator app, it's crucial to ensure that the user inputs are valid numbers before any arithmetic operation is performed.
Your task is to enhance the app's robustness by implementing input validation that prevents the program from crashing when a user enters non-numeric data.

**Instructions**:

1. Write a function 'safe_addition' that prompts the user for two numbers and returns their sum. 
It should handle an 'ValueError' exceptions that arise from non-numeric input.
2. Use a loop to allow the user to try entering the numbers again if they make an input error.
3. Print the result of the addition if the inputs are valid numbers.
4. Provide the user with the option to perform another addition or exit the program.

**Hints**:
- Use the 'try' block to attempt to convert the user input to floats
- Use the 'except' block to catch 'ValueError' and prompt the user to enter the numbers again.

'''

def safe_addition():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1 + num2
        except ValueError:
            print("Please enter only numbers. Try again.")



while True:
    result = safe_addition()
    print(f"The sum is: {result}")

    continue_input = input("Would you like to perform another addition? (yes/no): ").lower()
    if continue_input != 'yes':
        break
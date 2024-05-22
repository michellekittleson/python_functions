'''
Exercise 4: The Resilient Divider

In a data analysis context, dividing by zero can often occur and lead to program crashes.
Your task is to create a function that performs division but returns a specific message instead of crashing when a division by zero is attempted.

**Instructions**:

1. Write a function 'safe_divide' that takes two parameters, 'a' and 'b', and returns the ersult of 'a/b'.
2. Implement error handling to catch 'ZeroDivisionError' exceptions within the function.
3. If dividision by zero occurs, the function should return a message indicating that division by zero is not allowed.
4. Test hte function with user input and print the result or error message.

**Hints**:

- Use the 'try' block to attempt the division operation.
- Use the 'except' block to catch 'ZeroDivisionError' and return the appropriate message.
'''

# My version: 

# def safe_divide():
#     while True:
#         try:
#             a = float(input("Enter the first number: "))
#             b = float(input("Enter the second number: "))
#             return a / b
#         except ValueError:
#             print("Please enter only numbers. Try again. ")
#         except ZeroDivisionError:
#             print("The second number cannot be zero. Please try a different number.")

# while True:
#     result = safe_divide()
#     print(f"The quotient is {result}. ")

#     continue_input = input("Would you like to divide another set of numbers? (yes/no) ").lower()
#     if continue_input != "yes":
#         break

# Donovan's Version:

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Divsion by zero is not allowed."

while True:
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        result = safe_divide(numerator, denominator)
        print(f"The result of division is: {result}")
    except ValueError:
        print("Please enter only numbers.")

    continue_input = input("Would you like to performa another division? (yes/no): ").lower()
    if continue_input != 'yes':
        break
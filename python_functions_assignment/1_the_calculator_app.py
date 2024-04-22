'''
1. The Calculator App

Objective:
The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

Task 1: Create functions for each arithmetic operation.
Task 2: Implement user input to receive numbers and an operation choice.
Task 3: Ensure your program can handle division by zero and other potential errors.

'''

while True:
    operation = input("Which operation would you like to perform? [A]dditon, [S]ubtraction, [M]ultiplication, or [D]ivision? ")
    
    if operation == "A":
        add1 = int(input("Enter the first number: "))
        add2 = int(input("Enter the second number: "))
        sum = add1 + add2
        print(f"The sum of {add1} and {add2} is {sum}.")
    elif operation == "S":
        sub1 = int(input("Enter the first number: "))
        sub2 = int(input("Enter the second number: "))
        difference = sub1 - sub2
        print(f"The difference of {sub1} and {sub2} is {difference}. ")
    elif operation == "M":
        mult1 = int(input("Enter the first number: "))
        mult2 = int(input("Enter the second number: "))
        product = mult1 * mult2
        print(f"The product of {mult1} and {mult2} is {product}. ")
    elif operation == "D":
        div1 = int(input("Enter the first number: "))
        div2 = int(input("Enter the second number: "))
        if div2 == 0:
            print("Did you forget math class? You cannot divide a number by zero. ")
        else:
            quotient = div1 / div2
            print(f"The quotient of {div1} and {div2} is {quotient}. ")




# def subtraction():
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     difference = num1 - num2
#     print(f"The difference of {num1} and {num2} is {difference}. ")

# subtraction()

# def multiplication():
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     product = num1 * num2
#     print(f"The product of {num1} and {num2} is {product}. ")

# multiplication()

# def division():
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     if num2 == 0:
#         print("The second number of a quotient cannot be zero. ")
#     else:
#         quotient = num1 / num2
#         print(f"The quotient of {num1} and {num2} is {quotient}. ")

# division()
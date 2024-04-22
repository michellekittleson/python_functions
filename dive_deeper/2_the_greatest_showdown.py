# Task #1: Identify the Greatest

first_number = float(input("Enter the first number." ))
second_number = float(input("Enter the second number." ))
third_number = float(input("Enter the third number." ))

if first_number > second_number and first_number > third_number:
    print(f"The greatest number is {first_number}. ")

elif second_number > first_number and second_number > third_number:
    print(f"The greatest number is {second_number}. ")

elif third_number > first_number and third_number > second_number:
    print(f"The greatest number is {third_number}. ")


# Task #2: Identify the Smallest

first_number = float(input("Enter the first number." ))
second_number = float(input("Enter the second number." ))
third_number = float(input("Enter the third number." ))

if first_number < second_number and first_number < third_number:
    print(f"The smallest number is {first_number}. ")

elif second_number < first_number and second_number < third_number:
    print(f"The smallest number is {second_number}. ")

elif third_number < first_number and third_number < second_number:
    print(f"The smallest number is {third_number}. ")


# Task #3: Equality Check
    
first_number = float(input("Enter the first number." ))
second_number = float(input("Enter the second number." ))
third_number = float(input("Enter the third number." ))

if first_number > second_number and first_number > third_number and second_number != third_number:
    print(f"The greatest number is {first_number}. ")

elif second_number > first_number and second_number > third_number and first_number != third_number:
    print(f"The greatest number is {second_number}. ")

elif third_number > first_number and third_number > second_number and first_number != second_number:
    print(f"The greatest number is {third_number}. ")


# If two numbers are equal and greater

elif first_number == second_number and first_number > third_number:
    print(f"The largest number is {first_number}. There are two of them. The smallest number is {third_number}." )

elif first_number == third_number and first_number > second_number:
    print(f"The largest number is {first_number}. There are two of them. The smallest number is {second_number}." )

elif second_number == third_number and second_number > first_number:
    print(f"The largest number is {second_number}. There are two of them. The smallest number is {first_number}." )


# If two numbers are equal and smaller

elif first_number == second_number and first_number < third_number:
    print(f"The smallest number is {first_number}. There are two of them. The greatest number is {third_number}." )

elif first_number == third_number and first_number < second_number:
    print(f"The smallest number is {first_number}. There are two of them. The greatest number is {second_number}." )

elif second_number == third_number and second_number < first_number:
    print(f"The smallest number is {second_number}. There are two of them. The largest number is {first_number}." )


# If all three numbers are equal:

elif first_number == second_number == third_number:
    print(f"All three numbers are equal to {first_number}. ")

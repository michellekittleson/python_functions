'''
Apply various mathematical functions such as sum(), round(), sqrt(), ceil(), and floor().

You are working on a data analysis project that requires you to process a list of floating-point
numbers. Your task is to calculate the sum of all numbers, find the square root of each number, and
then round them up or down to the nearest integer. Additionally, you need to identify which numbers are
above the average after rounding.

**Instructions**:

1. Create a list of floating-point numbers.
2. Calculate the sum of the numbers using the sum() function and print the results
3. Use a loop to iterate over each number in the list.
4. Inside the loop, calculate the square root of each number using the sqrt() function from the math
   module.
5. Round each square root to the nearest integer using the round() function and then determine whether
   to round up or down using ceil() or floor() from the math module.
6. Use nested 'if' statements to compare each rounded number with the average of the list and print
   whether it is above or below the average. 
7. Ensure that the output is clear and informative.

'''

import math

numbers = [2.5, 3.6, 4.7, 5.8, 6.9]
total_sum = sum(numbers)
print(f"The sum of the numbers is: {total_sum}.")

average = total_sum / len(numbers)

for number in numbers:
    sqrt_number = math.sqrt(number)
    rounded_number = round(sqrt_number)
    if rounded_number < sqrt_number:
        rounded_number = math.ceil(sqrt_number)
    else:
        rounded_number = math.floor(sqrt_number)
    
    if rounded_number > average:
        print(f"{rounded_number} is above the average.")
    else:
        print(f"{rounded_number} is below the average.")
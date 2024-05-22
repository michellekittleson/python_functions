# Task 1: Start
# Begin by setting up a simple user input loop that asks the user to enter the temperature in Fahrenheit. 
# Ensure that your program only accepts numerical input and provides a friendly error message if 
# the user enters something that can't be converted to a number.

# while True:
#     try:
#         user_temperature = int(input("Enter the temperature in Fahrenheit: "))
#         print(f"You have entered {user_temperature} degreed Fahrenheit. ")
#     except ValueError:
#         print("Invalid input. Please enter a number. ")

#     continue_input = input("Would you like to enter another temperature? (yes/no): ").lower()
#     if continue_input != 'yes':
#         break

# Task 2: Temperature Conversion
# Write a function that converts the Fahrenheit temperature to Celsius. Remember that the
# formula is (Fahrenheit - 32) * 5/9.
# Use a try block to catch any potential errors during the conversion process, such as division by
# zero or overflow errors.

# Task 3: User Experience
# Implement an else block that prints the converted temperature in a user-friendly format.
# Add a finally block that thanks the user for using the weather forecast application, ensuring
# that this message is displayed regardless of whether an exception was caught or not.

def f_to_c():
    try:
        fahrenheit = int(input("Enter the temperature in Fahrenheit. "))
        celsius = round((fahrenheit - 32) * 5/9, 2)
        print(celsius)
    except ValueError:
        print("Input must be a number. Please try again. ")
    else:
        print(f"The temperature in Celsius is {celsius} degrees. ")
    finally:
        print("Thank you for using the weather forecast application. Come back soon! ")

f_to_c()
# Task 1: Start
# Ask the user for the number of servings the recipe is originally for and the number of servings they wish to make.
# Ensure that the user inputs are valid numbers and handle any ValueError that arises from improper input.


try:
    original_servings = int(input("Enter the number of servings the recipe was designed for: "))
    if original_servings > 0:
        print(f"Your recipe was made for {original_servings} servings.")
    else:
        print("Number of servings must be a positive number. ")

except ValueError:
    print("Make sure you enter a number of original servings.")

# Task 2: Quantity Calculation
# Calculate the adjustment factor by dividing the desired servings by the original servings.
# Use a 'try' block to catch any arithmetic errors that may occur during the calculation.

try:
    desired_servings = int(input("Enter the number of servings you would like to make. "))
    if desired_servings > 0:
        print(f"You would like to make {desired_servings} servings. ")
    else:
        print("Desired number of servings must be a positive number. ")
    adjustment_factor = desired_servings / original_servings
    rounded_adjustment = round(adjustment_factor, 2)
    print(f"The adjustment factor is {rounded_adjustment}.")
except ValueError:
    print("Make sure you enter a number of desired servings. ")



# Task 3: Serving Success
# If the calculation is successful, display the adjusted recipe quantities to the user.
# Use a finally block to print a message encouraging the user to enjoy their cooking, regardless of the outcome of the calculation.

finally:
    print("Thank you for using The Recipe Ratio Adjuster! Enjoy your cooking!")
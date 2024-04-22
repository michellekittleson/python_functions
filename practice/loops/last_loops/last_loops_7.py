# Scoring System Design: Create a list that includes only certain types of numbers.

# Use a list comprehension to iterate through numbers 1 to 30.
# Include a condition within the list comprehension to select only the multiples of three.
# Store the resulting list in a variable.

multiples_of_three = [number for number in range(1, 31) if number % 3 == 0]
print(multiples_of_three)
# The Skipping Rope Challenge 

# Initialize a countdown variable with the starting number.
# Create an empty list to store the numbers you land on.
# Write a while loop that counts down from the starting number.
# Use the continue statement to skip every other number.
# Append the numbers you land on to the list.
# Use the list slicing to display the final list of numbers.

count = 10

landed_numbers = []

while count > 0:
    count -= 1
    if count % 2 == 1:
        continue
    landed_numbers.append(count)

print("Numbers landed on:",landed_numbers[::-1])

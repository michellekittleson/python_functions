# Square Numbers Showcase: Generate a list of square numbers. You'll be creating
# a list that contains the squares of integers within a specific range.

# Use list comprehension to generate the squares of numbers from 1 to 10.
# Each element in the new list should be the square of an integer from the original range.

squares = [number**2 for number in range(1,11)]

print(squares)
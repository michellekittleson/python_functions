# Even Numbers Team Selection: Apply conditions within list comprehensions to
# filter data. You will be filtering a list to include only even numbers, which will be
# used to assign jerseys for a team event.

# Start with a list of numbers from 1 to 20.
# Use list comprehension to filter out the even numbers.
# Remember that an even number is divisible by 2 with no remainder.

numbers = list(range(1, 21))

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)
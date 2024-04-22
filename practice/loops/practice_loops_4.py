# Ask the user for the size of the multiplication table they wish to generate.
# Use nexted for loops to calculate the product of each pair of numbers.
# Display the multiplication table in a formatted manner.

table_size = int(input("Enter the size of the multiplication table: "))

for row in range(1, table_size + 1):
    for col in range(1, table_size + 1):
        product = row * col
        print(f"{product} \t", end="")
    print()
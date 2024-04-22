# Diverse Inventory Check: Use loop through a list with mixed data types using a 
# while loop and index numbers. You will also practice using if statements to
# perform different actions based on the data type of each item.

# Loop through the inventory list using a while loop and index numbers.
# Use if statements to check the data type of each item.
# Print a message for each item, depending on its data type.

# Could not get to work correctly

inventory = ["Apples", 120, "Oranges", 80, True, "Bananas", 150, False]

index = 0

while index < len(inventory):
    item = inventory[index]
    if type(item) == str:
        print(f"Item: {item}")
    elif type(item) == int:
        print(f"Quantity: {item}")
    elif type(item) == bool:
        status = "on sale" if item else "not on sale"
        print(f"Sale status: {status}")

        index += 1
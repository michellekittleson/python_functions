# Create a list of items in the inventory with their current quantities
# Use a for loop to iterate over each item
# Use an if statement to check if the quantity of an item is below the reorder threshold.
# Print out the names of the items that need to be reordered.

inventory = [
    ["Apples", 5],
    ["Bananas", 2],
    ["Oranges", 0],
    ["Milk", 1],
    ["Eggs", 12]
]

reorder_threshold = 3

for item in inventory:
    name, quantity = item
    if quantity < reorder_threshold:
        print(f"{name} needs to be reordered.")
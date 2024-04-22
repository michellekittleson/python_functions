# List of item prices
# Use a for loop to iterate through the list of prices
# Calculate the total cost by adding up the prices of all the items
# Print the total cost at the end.

item_prices = [2.99, 5.49, 3.25, 13.99, 4.75]

total_cost = 0

for price in item_prices:
    total_cost += price

print(f"The total cost of the shopping cart is: ${total_cost:.2f}")
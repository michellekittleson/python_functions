# The Smart Coffee Machine: Use while loops, lists, and if statements in Python to simulate a 
# coffee machine that offers different coffee types until the reservoir is empty.

# Initialize the coffee reservoir level
coffee_reservoir = 10
# List coffee types
coffee_types = ["Espresso", "Cappuccino", "Latte", "Americano", "Mocha"]

# Start dispensing coffee
while coffee_reservoir > 0:
    # Check if there are still coffee types available
    if coffee_types:
        # Dispense the first type of cofee
        current_coffee = coffee_types.pop(0)
        print(f"Dispensing {current_coffee}.")
        # Decrement the coffee amount 
        coffee_reservoir -= 1
        print(f"Coffee types left: {coffee_types}")
    else:
        print("No more coffee types available.")
        break

# Cofffee reservoir is empty
print("The coffee reservoir is now empty.")
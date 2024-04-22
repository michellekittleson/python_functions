# Create a program that rounds off prices to a user-friendly format.

# In retail applications, both online and in-store, displaying prices in a clear and precise
# manner is essential for customer satisfaction. Your task is to write a program that takes a 
# price as an input and rounds it to two decimal places, making it more user-friendly.

# Instructions:

# 1. Prompt the user to enter a price.
# 2. Use the round() function to round the price to two decimal places.
# 3. Display the rounded price in a format that is easy for customers to understand.
# 4. Provide the user with the option to enter a new price or exit the program.

while True:

    price_input = float(input("Enter the price of the item: "))
    rounded_price = round(price_input, 2)
    print(f"The price of the item is ${rounded_price}")

    new_price = input("Would you like to input a new price? (yes/no) ").lower()
    if new_price != "yes":
        break
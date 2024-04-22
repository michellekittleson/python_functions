# Create a program that generates a user-friendly summary of an e-commerce shopping cart.

# In an e-commerce application, it's important to provide customers with a clear and concise
# summary of their shopping cart before they proceed to checkout. Your task is to write a Python
# script that uses string concatenation to create a summary of the items in a shopping cart, 
# including product names, prices, and stock availability.

# 1. Define variables for a few products, their prices, and their stock availability.
# 2. Use string concatenation to build a summary of the cart.
# 3. Include product names, prices, and stock status (In Stock or Out of Stock) in the summary.
# 4. Display the cart summary to the user.

product_1 = "Wireless Mouse"
product_2 = "Gaming Keyboard"
product_3 = "USB-C Adapter"

price_1 = "$25"
price_2 = "$50"
price_3 = "$10"

in_stock_1 = True
in_stock_2 = False
in_stock_3 = True

cart_summary = "Your Cart Items:\n"
cart_summary += "- " + product_1 + ": " + price_1 +  (" (In Stock)" if in_stock_1 else " Out of Stock)") + "\n"
cart_summary += "- " + product_2 + ": " + price_2 +  (" (In Stock)" if in_stock_2 else " Out of Stock)") + "\n"
cart_summary += "- " + product_3 + ": " + price_3 +  (" (In Stock)" if in_stock_3 else " Out of Stock)") + "\n"

print(cart_summary)

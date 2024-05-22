'''
Exercise 2: The Simple Order Validator

An online bookstore is processing orders for a popular novel.
They need a simple system to ensure that customers enter a valid quantity when placing their orders.

**Instructions**:

1. Prompt the user to enter the quantity of books they wish to order.
2. Validate the input to ensure it is a positive integer.
3. If the input is valid, confirm the order by printing a message.
4. If the input is invalid (not an integer or a negative number), display an error message and prompt the user again.
5. Use a try/except block to catch non-numeric inputs.

**Hints**:

- Use a while loop to keep asking for input until a valid quantity is entered.
- Utilize the 'int()' function to convert the input to an integer and catch 'ValueError' for non-numeric inputs.
'''

def validate_order():
    while True:
        try:
            quantity = int(input("Enter the quantity of books you want to order: "))
            if quantity > 0:
                print(f"Thank you! You have ordered {quantity} books.")
            else:
                print("Invalid quantity. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

validate_order()
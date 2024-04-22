'''
Exercise 2: The Versatile Coffee Machine

You have a coffee machine that can make various types of coffee. You want to program it to prepare your coffee based on your selection.

**Instructions**:

1. Define a function called 'make_coffee()' that takes one parameter 'coffee_type' with a default value of "espresso".
2. Inside the function, print the message indicating the type of coffee being made.
3. Create a list of coffee types that the machine can make.
4. Use a loop to iterate over the list of coffee types.
5. Inside the loop, use an 'if' statement to check if the coffee type is "cappuccino". If it is, print a special message indicating that it's a favorite.
6. Call the 'make_coffee()' function with different arguments to simulate making different types of coffee.
7. Ensure that calling 'make_coffee()' without arguments defaults to making an espresso.
'''

def make_coffee(coffee_type="espresso"):
    print(f"Making a cup of {coffee_type} coffee!")

coffee_types = ['espresso', 'latte', 'cappuccino', 'americano', 'mocha']

for type in coffee_types:
    make_coffee(type)
    if type == 'cappuccino':
        print("You chose a favorite!")

make_coffee()
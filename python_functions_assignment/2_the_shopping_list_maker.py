'''
2. The Shopping List Maker

Objective:
The aim of this assignment is to create a program that helps users make a shopping list.

Task 1: Write a function that lets the user add items to a list.
Task 2: Include a feature to remove items from the list.
Task 3: Add a function that prints out the entire list in a formatted way.

'''
items = []

def shopping_list():
    while True:
        print("\nShopping List Maker")
        print("[A]dd an item ")
        print("[R]emove an item ")
        print("[V]iew list ")
        print("[E]xit")
        choice = input("What would you like to do? ")

        if choice == "A":
            new_item = input("Which item would you like to add? ")
            items.append(new_item)
            print(f"Added to shopping list: {new_item}! ")
        elif choice == "R":
            item_to_remove = input("Which item would you like to remove? ")
            if item_to_remove in items:
                items.remove(item_to_remove)
                print(f"Removed from shopping list: {item_to_remove}! ")
            else:
                print(f"{item_to_remove} was not found on the shopping list. ")
        elif choice == "V":
            print("On your shopping list: ")
            print(items)
        elif choice == "E":
            print("Exiting shopping list. ")
            break


shopping_list()
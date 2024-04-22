'''
Exercise 5: The Product Inventory Manager

You are developing a feature for an e-commerce app that allows the store manager to view and update the inventory of products.

**Instructions**:

1. Define a list called 'products' that contains the initial inventory of product names.
2. Create a function called 'manage_inventory()' that will display the current inventory, allow the manager to add new products, and remove products that are out of stock.
3. Inside the function, use a loop to display options for the manager: view inventory, add product, remove product, and exit.
4. Use list slicing and the 'len()' function to display the first 5 products in the inventory when viewing.
5. Allow the manager to add a product by entering its name, which will append to the 'products' list.
6. Allow the manager to remove a product by entering its name. Ensure the product exists in the list before attempting to remove it.
7. Use the 'input()' function to collect the manager's choices and product names.
'''

products = ['T-shirt', 'Jeans', 'Sneakers', 'Hat', 'Sunglasses', 'Jacket', 'Watch']

def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. View Inventory")
        print("2. Add Product")
        print("3. Remove Product")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nCurrent Inventory:")
            for product in products[:5]:
                print(product)
            if len(products) > 5:
                print("... and more")
        elif choice == "2":
            new_product = input("Enter the neame of the new product: ")
            products.append(new_product)
            print(f"{new_product} has been added to the inventory.")
        elif choice == "3":
            product_to_remove = input("Enter the name of the product to remove: ")
            if product_to_remove in products:
                products.remove(product_to_remove)
                print(f"{product_to_remove} has been removed from the inventory.")
            else:
                print(f"{product_to_remove} was not found in the inventory.")
        elif choice == "4":
            print("Exiting Inventory Managememt System.")
            break
        else:
            print("Invalid choice. Please try again.")

manage_inventory()
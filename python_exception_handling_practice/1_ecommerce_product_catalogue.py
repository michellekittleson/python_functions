'''
Exercise 1: E-commerce Product Catalog

Build a Python program to manage an e-commerce product catalog efficiently.
The program should facilitate adding new product categories, adding products, displaying all available 
categories, and conducting product searches within the catalog.
**Instructions**

1. Initialize a dictionary to represent your product catalog.
2. Implement functions to:
    - Add a new product category.
    - Add a product to an existing category.
    - Display all product categories with their respective products.
    - Search for a product across all categories.
3. Include error handling for situations such as adding a product to an unlisted category.
4. Ensure that the product search is case-insensitive.
5. Design the program to handle multiple additions and searches.

**Hints**

- Start by pre-populating your catalog dictionary with some categories and products.
- Utilize the 'lower()' or 'upper()' methods on strings for case-insensitive comparison.
- In your search function, check for the product's presence in every category.
- Leverage 'try' and 'except' blocks to gracefully handle any KeyError instances.

'''

def add_category(catalog, category):
    if category not in catalog:
        catalog[category] = []
        print(f"Category '{category}' added")
    else:
        print(f"Category '{category}' already exists. ")

def add_product(catalog, category, product):
    try:
        if product not in catalog[category]:
            catalog[category].append(product)
            print(f"Product '{product}' added to '{category}'.")
        else:
            print(f"Product '{product}' already exists in '{category}'.")
    except KeyError:
        print(f"Category '{category}' does not exist.")

def display_categories(catalog):
    for category, products in catalog.items():
        print(f"{category}: {', '.join(products)}")

def search_product(catalog, product):
    found = False
    for category, products in catalog.items():
        if product.lower() in [p.lower() for p in products]:
            found = True
            print(f"Product '{product}' was found.")
            break
    if not found:
        print(f"Product '{product}' not found.")



catalog = {"Electronics": ["Laptop", "Smartphone"], "Books": ["Fiction", "Non-Fiction"]}

add_category(catalog, "Clothing")
add_product(catalog, "Electronics", "Camera")
display_categories(catalog)
search_product(catalog, "laptop")
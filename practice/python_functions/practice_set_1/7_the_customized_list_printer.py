# Use custom separators and endings in the print() function, while also incorporating loops to 
# iterate over elements, and lists to store data.

# You are tasked with creating a program that prints out a shopping list.
# However, the user wants the list to be printed in a specific format, with custom
# separators beteween items and a custom ending to signify the end of the list.

# 1. Create a list of shopping items
# 2. Ask the user for their preferred separator (e.g., comma, slash, dash)
# 3. Ask the user for their preferred ending phrase (e.g., "End of list!", "That's all!")
# 4. Use a loop to print each item with the user's preferred separator and end the list
# with their chosen ending phrase.

shopping_list = ["apples", "bananas", "carrots", "bread", "milk"]
seperator = input("Please enter your preferred item separator. (e.g., ',', '/', '-'): ")
ending = input("Please enter your preferred ending phrase.: ")

print("Your shopping list: ", end="\n\n")
for item in shopping_list:
    if item == shopping_list[-1]:
        print(item)
    else:
        print(item, end=seperator + " ")
print("\n\n" + ending)
'''
Exercise 6: The Stats Breakdown

**Problem Statement**:
You are creating a feature for a sports analytics app that categorizes and displays player statistics.
The app takes a single string input of various stats separated by semicolons, where each stat is a category-value pair joined by a colon.
The program should print each stat on a new line with its category and value clearly labeled.

**Instructions**:

1. Write a function 'print_stats' that takes a string of stats and prints each one on a new line.
2. Each stat should be presented in the format: "Category: [CATEGORY], Value: [VALUE]".
3. Implement a loop that prompts the user to enter their first stats string.
4. Use the function to parse the stats and print them in a user-friendly format.
5. Ensure the program handles invalid formats by informing the user and asking for input again.

'''

def print_stats(stats_string):
    stats_list = stats_string.split(';') # splits the stat list by semi-colons
    for stat in stats_list: # [goals:4;fouls:1]
        category_value = stat.split(';')
        if len(category_value) == 2:
            category, value = category_value
            print(f"Category: {category}, Value: {value}")
        else:
            print(f"Invalid format for stat: {stat}")
            break

while True:
    stats_input = input("Enter your stats separated by semicolons (e.g., 'Goals:4;Assists:2;Fouls:1)")
    print_stats(stats_input)

    continue_input = input("Would you like to enter more stats? (yes/no)").lower()
    if continue_input != 'yes':
        break    
'''
Exercise 5: The Personalized Welcome Mat

You are developing a feature fort a hospitality app that personalizes the welcome experience for guests.
The app takes the guest's name as input and prints a welcome message, with the name beautifully centered within a design made of asterisks

**Instructions**:

1. Write a function 'create_welcome_message' that takes a string (the user's name) and returns a welcome message.
2. The welcome message should have the user's name centered within a line of asterisks.
3. Implement a loop that prompts the user to enter their name.
4. Use the function to generate the welcome message and print it using an f-string.
5. Ensure the program handles empty or invalid names by informing the user and asing for input again.

'''

def create_welcome_message(name):
    line_length = 30
    centered_name = name.center(line_length, '*') # Will put asterisks around the name
    return f"Welcome {centered_name} Welcome"

while True:
    user_name = input("Please enter your name for a personalized welcome message: ")
    if user_name.isalpha(): # makes sure the username is letters only
        welcome_message = create_welcome_message(user_name)
        print(welcome_message)
    else:
        print("Invalid neame. Please enter alphabetic characters only.")
    continue_input = input("Would you like to create another welcome message? (yes/no)").lower()
    if continue_input != 'yes':
        break
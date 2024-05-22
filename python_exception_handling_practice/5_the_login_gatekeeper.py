'''
Exercise 5: The Login Gatekeeper

In a software application, it's crucial to ensure that user credentials meet certain security standards.
Your task is to create a function that checks whether a username meets the required criteria and raises a custom exception if it does not.

**Instructions**:

1. Define a custom exception class named 'UsernameError' that inherits from the base 'Exception' class.
2. Write a function 'check_username' that takes a single parameter, 'username', and checks if it meets the crieteria (e.g., at least 6 characters long).
3. If the username does not meet the criteria, raise a 'UsernameError' with an appropriate error message.
4. Prompt the user to input a username and use a 'try-except' block to catch the 'UsernameError' and display the error message.

**Hints**:

- Use the 'raise' keuword to raise the custom exception with a message when the username is too short.
- In the 'except' block, catch the 'UsernameError' and print the message to inform the user.
'''

class UsernameError(Exception):
    def __init__(self, message):
        self.message = message

def check_username(username):
    if len(username) < 6:
        raise UsernameError("Username must be at least 6 characters long")

while True:
    username_input = input("Please enter your username: ")
    try:
        check_username(username_input)
        print("Username is valid.")
        break
    except UsernameError as e:
        print(f"Error: {e.message}") 
    
    try_again_input = input("Would you like to try a different username? (yes/no)").lower()
    if try_again_input != 'yes':
        break
'''
Exercise 7: The Name Tag Switcheroo

You are developing a playful feature for a social networking app that allows users to swap the first and last characters of their usernames.
The app takes a username as input and displays the modified version.

**Instructions**:

1. Write a function 'swap_characters' that takes a string and returns a new string with the first and last characters swapped.
2. Ensure the function handles usernames of any length, including single-character naes.
3. Implement a loop that prompts the user to enter their username.
4. Use the function to swap the characters and print the result in a fun and engaging way.
5. Provide the user with the option to try another username or exit the program.

'''

def swap_characters(username):
    if len(username) > 1:
        return username[-1] + username[1:-1] + username[0] # Coding ==> godinC
    return username

while True:
    username_input = input("Enter your username to see the magic swap: ")
    swapped_username = swap_characters(username_input)

    print(f"Ta-da! Your magical username is: {swapped_username}")

    continue_input = input("Want to try another username? (yes/no): ").lower()
    if continue_input != 'yes':
        break
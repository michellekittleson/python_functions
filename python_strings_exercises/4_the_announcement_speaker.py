'''
Exercise 4: The Announcement Speaker

You are creating a feature for a public address system app that allows users to input a message and then displays the message in uppercase,
which represents the announcement mode.

**Instructions**:

1. Write a function 'announce_message' that takes a string and returns the string in uppercase.
2. Implement a loop that prompts the user to enter their message.
3. Use the function to convert the message and print it using an f-string.
4. Ensure the program handles empty strings by informing the user and asking for input again.

'''

def announce_message(message):
    return message.upper()

while True:
    user_input = input("Enter your message for the announcement: ")
    if user_input.strip():
        announcement = announce_message(user_input)
        print(f"Announcement: {announcement}")
    else:
        print("No message entered. Please provide a message for the announcement.")
    continue_input = input("Do you want to make another announcement? (yes/no) ").lower
    if continue_input != 'yes':
        break
    
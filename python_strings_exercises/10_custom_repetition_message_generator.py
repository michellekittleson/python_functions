'''
Exercise 10: The Custom Repetition Message Generator

In many user interfaces, there's a need to display a message or a string repeatedly to grab attention or for aesthetic purposes.
You are tasked with developing a feature for a user interface toolkit that allows users to repeat a string a specified number of times
with each repetition separated by a dash ('-')

**Instructions**:

1. Write a function 'repeat_message' that takes a string and a number as arguments and returns the repeated string pattern.
2. Implement a loop that prompts the user to enter their message and the number of repetitions.
3. Use the function to generate the repeated string pattern and print the result.
4. Provide the user with the option to create a new repeated string pattern or exit the program.

'''

def repeat_message(message, times):
    return "-".join([message] * times)

while True:
    user_message = input("Enter the message you want to repeat: ")
    repeat_count = int(input("How many times would you like to repeat it? "))

    repeated_message = repeat_message(user_message, repeat_count)
    print(f"Repeated message: {repeated_message}")

    continue_input = input("Would you like to create another repeated message? (yes/no) ").lower
    if continue_input != 'yes':
        break
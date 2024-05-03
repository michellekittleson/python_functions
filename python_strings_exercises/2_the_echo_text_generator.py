'''
Exercise 2: The Echo Text Generator

You are tasked with developing a feature for a social media app that allows users to create a fun echo effort with their text posts.
This feature repeats each character in the text to create an echo-like pattern, making the posts more engaging and visually appealing.

**Instructions**:

1. Write a function 'generate_echo_text' that takes a 'text' string as a parameter and returns a new string with each character repeated twice.
2. Implement a loop that prompts the user to enter a string (representing a social media post or message).
3. Use the function to generate the echo text and print the result using an f-string.
4. Ensure the program handles empty strings and informs the user accordingly.


'''

def generate_echo_text(text):
    if text:
        return ''.join([char * 2 for char in text])
    else:
        return "The input text cannot be empty. Please enter some text."
    
while True:
    user_input = input("Enter your text to echo: ")

    echo_text = generate_echo_text(user_input)
    print(f"Your echoed text is: {echo_text}")

    continue_echo = input("Do you want to create another echo text? (yes/no): ").lower()
    if continue_echo != 'yes':
        break
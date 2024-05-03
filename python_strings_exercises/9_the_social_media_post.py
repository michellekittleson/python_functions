'''
Exercise 9: The Social Media Post Formatter

In the world of social media, users often like to stylize their posts with unique character replacememts.
You're tasked with developing a feature for a social media app that allows users to replace every instance of the letter 'a' with '@' and 'e' with '3'. 

**Instructions**:
1. Write a function 'stylize_post' that takes a string and returtns a sylized version of it according to the specified replacements.
2. Implement a loop that prompts the user to enter their post.
3. Use the function to apply the stylization and print the result.
4. Provide the user with the option to stylize a new post or exit the program.

'''

def stylize_post(post_string):
    stylized_chars = []
    for char in post_string:
        if char == 'a':
            stylized_chars.append('@')
        elif char == 'e':
            stylized_chars.append('3')
        else:
            stylized_chars.append(char)
    return ''.join(stylized_chars)

while True:
    user_post = input("Enter your user post: ")
    stylized_post = stylize_post(user_post)
    print(f"Stylized post: {stylized_post}")

    continue_input = input("Would you like to stylize another post? (yes/no)").lower
    if continue_input != 'yes':
        break
# Create a program that validates usernames based on length. This exercise will focus on using
# conditional statements and the len() function.

# In the digital age, usernames are crucial for identity on various platforms.
# Your task is to write a program that checks if a username is neither too short nor too long, 
# adhering to specific length crieteria.

# Instructions:

# 1. Prompt the user to enter a username.
# 2. Check if the username is between 5 and 15 characters long.
# 3. If the username meets the criteria, print a confirmation message.
# 4. If it does not meet the criteria, print a messge indicating the username length requirements.
# 5. Provide the user with the option to try a different username or exit the program.

while True:
    username = input("Enter a username: ")

    if 5 <= len(username) <= 15:
        print("Your username is the correct length.")
    else:
        print("Please choose a username that is between 5 and 15 characters.")
    
    continue_input = input("Do you want to try another username? (yes/no) ").lower()
    if continue_input != "yes":
        break


''''
3. Interactive Help Desk Bot

Task #1: Command Parser
Write a script that takes a user's text input and identifies if it contains 
one of the predefind commands (e.g., "help", "issue", "contact support").
If a command is found, print a response related to the command.

Task 2: Issue Categorizer
If the user's input contains the word "issue", further categorize the issue
based on keywords such as "login", "performance", "error", etc. 
Print out the category of the issue for the support team.

'''

user_input = input("What can we do for you today? ")
if "help" in user_input:
    print("Help is on the way!")
elif "issue" in user_input:
    if "login" in user_input:
        print("User is having an issue logging in.")
    elif "performance" in user_input:
        print("User is having an issue with performance.")
    elif "error" in user_input:
        print("User is experiencing an error.")
elif "contact support" in user_input:
    print("Let me send you the information to contact customer service.")

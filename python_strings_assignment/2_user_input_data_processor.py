import re

'''
Task 1: Input Length Validator

Write a script that checks the length of the user's first and last name.
Both should be at least 2 characters long. If not, print an error message.

'''

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

if len(first_name) >= 2:
    print(f"Your first name is {first_name}.")
else:
    print("Please enter a first name that is at least 2 characters long.")

if len(last_name) >=2:
    print(f"Your last name is {last_name}.")
else:
    print("Please enter a last name that is at least 2 characters long.")

'''
Task 2: Password Complexity Checker

Create a function that checks the complexity of a user's password.
The password must be at least 8 characters long, contain one uppercase letter, 
one lowercase letter, and one number. If the password does not meet these criteria,
print a message explaining the complexity requirements.

'''


def password_checker(ups):
    #user_password = input("Please enter your password: ")
    if len(ups) >= 8:
        print("Your password meets the length requirement.")
    else:
        print("Make sure your password is at least 8 characters long.")

def upper_lower_special(ups):
    regex = ("^(?=.*[a-z])(?=." + "*[A-Z])(?=.*\\d)" + "(?=.*[-+_!@#$%^&*., ?]).+$")
    p = re.compile(regex)
    if (ups == None):
        print("Your password is empty. Please start over and enter your password. ")
        return
    if(re.search(p, ups)):
        print("Congratulations! Your password meets the requirements. ")
    else:
        print("Your password does not meet the requirements. Please start over and enter your password. ")

user_password = input("Please enter your password: ")
password_checker(user_password)
upper_lower_special(user_password)



'''
Task 3: Email formatter
Implement a script that ensures all user email addresses are in a standard format. 

Help!

'''

def email_checker(em):
    element = "@"
    if em.index(element) == 0:
        print("You need at least 1 character before '@'. ")
    else:
        dot = "."
        dotposition=em.rfind(dot)
        print(dotposition)
        print(len(em))
        if dotposition != len(em) - 4:
            print("Email extension is not valid. ")
        else:
            print("Congratulations! Your email is in standard format.")

em = input("Enter your email: ")
email_checker(em)
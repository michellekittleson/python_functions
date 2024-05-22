'''
Exercise 9: Multi-Scenario Input Handling

In a software application that processes user data, it's essential to anticipate and handle different kinds of erroneous input.
Your task is to write a program that asks users for their age and ensures that the input is both a number and within a reasonable range.

**Instructions**:

1. Prompt the user to enter their age.
2. Use a 'try-except' block to handle the following scenarios:
    - The input is not a number ('ValueError').
    - The number is not within the range of 0 to 120 ('ValueError).
3. If an exception is raised, provide a specific error message for the type of exception and ask for the input again.
4. If the input is valid, print a confirmation message.

**Hints**:

- Use 'int()' to convert the input string to an integer and catch any 'ValueError' exceptions.
- Check the age range within the 'try' block and raise a 'ValueError' with a custom message if the age is out of range.
'''

while True:
    try:
        user_age = input("Enter your age: ")
        age = int(user_age)
        if age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 120.")
    except ValueError as ve:
        if "invalid literal" in str(ve):
            print("That's not a number. Please enter your age using digits.")
        else:
            print(ve)
    else:
        print(f"Thank you. Your age is recorded as {age}.")
        break
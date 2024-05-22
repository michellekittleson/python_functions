'''
Exercise 8: User Input Validation with Fallback

In user-driven appllications, it's common to require input that matches specific criteria.
Your task is to write a program that prompts the user for their favorite fruite from a predefined list.
If the input is not in the list, the program should handle the situation gracefully and ask for input again.

**Instructions**:

1. Create a list of fruits that are allowed inputs.
2. Prompt the user to enter their favorite fruit.
3. Use a 'try-except-else' block to validate the input.
4. If the input is not in the list, raise a 'ValueError' and handle it by asking for input again.
5. If the input is valid, print a confirmation message.

**Hints**:

- The 'else' block can be used to execute code when the 'try' block doesn't raise an exception.
- Use a loop to keep asking for input until a valid fruit is entered.
'''

# This does not work for me

allowed_fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

while True:
    try:
        favorite_fruit = input("Enter your favorite fruit: ").lower
        if favorite_fruit not in allowed_fruits:
            raise ValueError("Fruit not in the list.")
    except ValueError as ve:
        print(ve)
        print("Please choose a fruit from the list.")
    else:
        print(f"Great choice! Your favorite fruit is {favorite_fruit}.")
        break

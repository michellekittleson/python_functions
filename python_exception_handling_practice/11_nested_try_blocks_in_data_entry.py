'''
Exercise 11: Nested Try Blocks in Data Entry

You are creating a data entry module for a software application where users can add numerical data to a list.
The module should validate the input and handle errors when users enter invalid data or attempt incorrect operations.

**Instructions**:

1. Initialize an empty list to store numerical entries.
2. Prompt the user to enter a numer or 'done' to finish.
3. Use a nested 'try' block to handle the following:
    - Convert the input to a float and append it to the list.
    - If the user enters 'done', break out of the loop.
4. Use an 'else' block to confirm the entry has been added.
5. Handle 'ValueError' for non-numeric input and 'TypeError' for any type-related errors during conversion.
6. Use a 'finally' block within the nested 'try' to inform the user that they can continue entering data.
7. After the loop, print the list of entered numbers.

**Hints**:

- Use a 'while' loop to continuously prompt the user for input.
- Use 'float()' to attempt to convert the input to a number.
- Use an 'else' block after the 'try' block to print a confirmation message.
- Use a 'finally' block to print a message that encourages the user to keep entering data.
'''

def data_entry():
    data_list = []
    while True:
        user_input = input("Enter a number or type 'done' to finish: ")
        if user_input.lower() == 'done':
            break
        try:
            try:
                number = float(user_input)
            except ValueError:
                print("That's not a number. Please enter a valid number. ")
                continue
            else:
                data_list.append(number)
        except TypeError:
            print("An unexpected type error occurred. ")
        finally:
            print("You can enter another number or type 'done' to finish. ")
    print("Data entered:", data_list)

data_entry()
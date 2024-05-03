'''
Exercise 8: The Meeting Agenda Reverser

Imagine you're developing a feature for a meeting management app that allows users to reverse the order of items in their meeting agenda.
The app accepts a string representing the agenda items in order and outputs them in reverse order.

**Instructions**:

1. Write a function 'reverse_agenda' that takes a string of agenda items and returns a string with the items in reverse order.
2. Implement a loop that prompts the user to enter their agenda items separated by commas.
3. Use the function to reverse the order of the agenda items and print the result.
4. Provide the user with the option to enter a new agenda or exit the program.

'''

def reverse_agenda(agenda_string):
    # 'gym, breakfast, work'
    agenda_items = agenda_string.split(', ')
    # ['gym', 'breakfast', 'work]
    # ['work', 'breakfast', 'gym']
    reversed_agenda = agenda_items[::-1] # Will loop through list backwards
    # 'work, breakfast, gym'
    return ', '.join(reverse_agenda)

while True:
    user_agenda = input("Enter your meeting agenda item separated by commas: ")
    reversed_order = reverse_agenda(user_agenda)
    print(f"Reversed agenda order: {reversed_order}")

    continue_input = input("Would you like to reverse another agenda? (yes/no) ").lower()
    if continue_input != 'yes':
        break
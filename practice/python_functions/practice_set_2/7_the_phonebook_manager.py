'''
Exercise 7: The Phonebook Manager

You need to manage contact in a phonebook.
Your task is to create functions that can add a new contact and display all contacts, ensuring that you correctly handle variable scope.

**Instructions**:

1. Define a global list called 'phonebook' to store contacts as separate lists for names and numbers.
2. Define a function called 'add_contact()' that takes a name and number as arguments and adds them to the 'phonebook' lists.
3. Define a function called 'display_contacts()' that prints all the contacts in the 'phonebook'.
4. Use a loop to allow the user to choose between adding a contact or displaying all contacts.
5. Ensure that the 'phonebook' list is not reinitialized within the functions, preserving its global scope.
'''

phonebook_names = []
phonebook_numbers = []

def add_contact(name, number):
    global phonebook_names
    global phonebook_numbers
    phonebook_names.append(name)
    phonebook_numbers.append(number)

def display_contacts():
    global phonebook_names
    global phonebook_numbers
    for i in range(len(phonebook_names)):
        print(f"Name: {phonebook_names[i]}, Number: {phonebook_numbers[i]}")

while True:
    action = input("Choose an action: [A]dd contact, [D]isplay contacts, [Q]uit: ")
    if action == "A":
        name = input("Enter the contact's name: ")
        number = input("Enter the contact's phone number: ")
        add_contact(name, number)
    elif action == "D":
        display_contacts()
    elif action == "Q":
        break
    else:
        print("Invalid action. Please choose again.")
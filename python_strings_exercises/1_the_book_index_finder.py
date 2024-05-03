'''
Exercise 1: The Book Index Finder

You are deeloping a feature for an e-reader app that allows users to find the index of characters in a book or document.
This feature helps users to quickly navigate through the text by character references.

**Instructions**:

1. Write a function 'find_character_index' that takes a 'text' string and a 'character' as parameters and returns the index of the character in the text.
2. If the character is not found, the function should return a message stating that the character is not present.
3. Implement a loop that prompts the user to enter a string (representing a paragraph or line from a book) and a character to search for.
4. Use the function to find the index of the character and print the result using an f-string.
5. Ensure the program handles cases where the user may enter multiple characters instead of a single one.


'''

def find_character_index(text, character):
    if len(character) == 1:
        index = text.find(character)
        if index == -1:
            return f"The character '{character}' is not present in the text."
        else:
            return f"The index of the character '{character}' is: {index}"
    else:
        return "Please enter only a single character."

while True:
    text_input = input("Enter a line of text from the book: ")
    char_input = input("Enter the character to find: ")

    result = find_character_index(text_input, char_input)
    print(result)

    continue_search = input("Do you want to search for another character? (yes/no): ").lower()
    if continue_search != 'yes':
        break
    
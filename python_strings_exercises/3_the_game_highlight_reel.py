'''
Exercise 3: The Game Highlight Reel

You are developing a feature for a sports app that allows users to input a series of game highlights and then displays each event separately for easy reading and analysis.
This feature is particularly useful for users who want to quickly create summaries of key moments in a match or game.

**Instructions**:

1. Write a function 'format_highlights' that takes a string of highlights separated by commas and returns a list of individual plays.
2. Implement a loop that prompts the user to enter the string of highlights
3. Use the function to format the highlights and print each play on a new line using an f-string.
4. Ensure the program handles empty strings by infomring the user and asking for input again.


'''

def format_highlights(highlight_string):
    if highlight_string.strip():
        return [play.strip() for play in highlight_string.split(',')]
    else: 
        return[]
    
while True:
    user_input = input("Enter the game highlights, separated by commas: ")
    formatted_highlights = format_highlights(user_input)

    if formatted_highlights:
        print("Game highlights: ")
        for play in formatted_highlights:
            print(f"- {play}")
    else:
        print("No highlights entered. Please provide the highlights of the game.")
    continue_input = input("Do you want to enter more highlights? (yes/no) ").lower()

    if continue_input != 'yes':
        break
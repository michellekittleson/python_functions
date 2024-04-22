# Task 1: Random Choice Game
# Create a game where a player has a list of items. They have to guess which item in the list was
# selected. Use random.choice() to select the item and take the user's guess via input. Provide
# feedback on whether they guessed correctly or not.

import random

items = ["marker", "pencil", "chromebook", "paper airplane", "chair"]

item = random.choice(items)
guess = input("Which item do you guess a student threw across the room today in math class?")
if guess == item:
    print(f"Congratulations, you guessed correctly! A student threw a {item} across the room today!")
else:
    print("Nope, guess again!")
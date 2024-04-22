# Quiz Master Shuffle: Randomize lists and iterate over them, which is useful for creating quizzes, 
# games, and other applications where random order is required.

# Import the random module to shuffle the list of questions.
# Use the random.shuffle() method to randomize the order of the quiz questions.
# Use a for loop to iterate through the shuffled list and present each question.
# Print out each question to the user.

import random

questions = ["What is the capital of France?", "What is 2 + 2?", "Who wrote Macbeth?", "What is the boiling point of water?", "How many continents are there?"]

random.shuffle(questions)

for question in questions:
    print(question)
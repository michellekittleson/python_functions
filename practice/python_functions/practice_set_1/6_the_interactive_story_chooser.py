# Use the input() function to capture user input, along with conditional statements to direct
# the flow of a program, and lists to store and manipulate data.

# You are creating an interactive story where the reader can choose their own adventure.
# At each stage of the story, the reader is presented with a choice that determines the
# direction of the narrative. Your task is to write a Python script that guides the 
# reader through the first decision point of the story.

# 1. Present the reader with a brief introduction to the story and a choice to make.
# 2. Capture the reader's choice using the input() function.
# 3. Depending on the choice, display the outcome of their decision.
# 4. Use a list to store possible choices and outcomes.

print("You wake up in a mysterious forest. Two paths lie before you. ")
choices = ["left", "right"]
outcomes = ["You encounter a friendly elf who offers you a map.",
            "You stumble upon a sleeping dragon."]

# We use an f string here rather than putting the question in the input because we want 
# the question to appear in a new line when it is printed.

print(f"Do you go left or right? (Type 'left' or 'right'.)")
decision = input().lower()

if decision not in choices:
    print("Confused, you decide to wait for a clearer sign of which path to take. ")
elif decision == "left":
    outcome_index = choices.index("left")
    print(outcomes[outcome_index])
else:
    outcome_index = choices.index("right")
    print(outcomes[outcome_index])

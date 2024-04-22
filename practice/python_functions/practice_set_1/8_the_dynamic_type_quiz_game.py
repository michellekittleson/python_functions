# Use type conversion functions such as int(), float(), str(), and bool(). You will also use
# loops to iterate over questions and lists to store the quiz data.

# You are tasked with developing a quiz game that challenges players to answer questions that require
# answers in different data types. The game should prompt the user for an answer, convert the answer 
# to the required type, and verify its correctness.

# 1. Create separate lists for questions, correct answers, and the required answer types.
# 2. Use a loop to iterate over the questions and present them to the user one by one.
# 3. For each question, prompt the user for their answer and convert it to the required type using
# the corresponding type conversion function.
# 4. Compare the user's converted answer to the correct answer and provide immediate feedback.
# 5. Keep a count of the number of correct answers and display the user's score at the end of the game.

questions = [
    "What is 10 plus 4?",
    "Enter a decimal number between 1 and 2",
    "What is the string representation of the number 20?",
    "Is Python a programming language? (True/False)"
]

correct_answers = [14, 1.5, "20", True]
answer_types = [int, float, str, bool]

score = 0

for i in range(len(questions)):
    user_answer = input(questions[i] + " ")
    try:
        if answer_types[i] == bool:
            converted_answer = user_answer.lower() in ["true", "t", "1", "yes", "y"]
        else:
            converted_answer = answer_types[i](user_answer)
        if converted_answer == correct_answers[i]:
            print("Correct!")
            score += 1
        else: 
            print("Wrong answer.")
    except ValueError:
        print("Invalid input type.")
    
print(f"Your final score is {score}/{len(questions)}") 

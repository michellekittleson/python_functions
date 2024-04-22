'''
4. The Quiz Game

Objective:
The aim of this assignment is to create a quiz game that asks questions and checks answers.

Task 1: Develop a list of questions and answers.
Task 2: Write a function that quizzes the user and takes their answers.
Task 3: Score the quiz and give the user feedback on their performance.

'''

questions = ["What is 25 times 5? ", "What is the average of 3 and 5? ", "How many keys on a piano keyboard? ", "The president of the United States in 2024 is Joe Biden. (True/False)"]
correct_answers = [125, 4, 88, True]
answer_types = [int, int, int, bool]

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
            score +=1
        else:
            print("Wrong answer.")
    except ValueError:
        print("Invalid input type.")
    
print(f"Your final score is {score}/{len(questions)}")

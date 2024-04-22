'''
3. The Grade Analyzer

Objective:
The aim of this assignment is to analyze a set of grades and provide statistics.

Task 1: Code a function to calculate the average grade.
Task 2: Implement a function to find the highest and lowest grade.
Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).

'''
individual_grades = [87, 92, 99, 75, 100]

def average_grade():
    average = sum(individual_grades) / len(individual_grades)
    print(f"The average grade is {average}")

average_grade()

def highest_grade():
    highest = max(individual_grades)
    print(f"The highest grade is {highest}.")

highest_grade()

def lowest_grade():
    lowest = min(individual_grades)
    print(f"The lowest grade is {lowest}.")

lowest_grade()

def letter_grade():
    for i in range(len(individual_grades)):
        if 90 <= i <= 100:
            print("A")

letter_grade()

# Need help with this part

def letter_grade(grades):
    for grade in grades:
        if grade >= 90:
            print("A")
        elif grade >= 80:
            print("B")
        elif grade >= 70:
            print("C")
        elif grade >= 60:
            print("D")
        else:
            print("F")
letter_grade(individual_grades)
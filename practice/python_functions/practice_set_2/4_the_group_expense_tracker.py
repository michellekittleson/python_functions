'''
Exercise 4: The Group Expense Tracker

You are creating a program to track expenses for a group of friends on a trip. The program will calculate the total expenses and identify the highest spender.

**Instructions**:

1. Define a function called 'track_expenses()' that takes a variable number of numerical arguments representing individual expenses.
2. Inside the function, calculate the sum of the expenses and print the total.
3. Also, determine the highest expense and print the person associated with it.
4. Outside the function, use a while loop to prompt each user to enter their expense until they enter 'done'.
5. Use 'input()' to accept the expense amount from each user and store these in a list.
6. After collecting all expenses, call the 'track_expenses' function with the list of expenses as arguments using the splat operator (*).
'''

def track_expenses(*expenses): # splat operator (*) provides an unlimited amount of numerical arguments
    total_expenses = sum(expenses)
    print(f"The total expenses are: {total_expenses} ")

    highest_expense = max(expenses)
    spender = expenses.index(highest_expense)+1
    print(f"Person {spender} is the highest spender with an expense of: {highest_expense}")

group_expenses = []

while True:
    expense_input = input("Enter an expense amount or 'done' to finish. ")

    if expense_input.lower() == 'done':
        break
    else:
        expense = float(expense_input)
        group_expenses.append(expense)

track_expenses(*group_expenses)
'''
Exercise 6: The Payment Splittler

In a group of friends, expenses are often shared. Your task is to create a function that calculates how much each person must pay or be reimbursed after a shared expense.

**Instructions**:

1. Define a function called 'split_payment()' that takes a list of expenses and the number of friends in an argument.
2. The function should calculate the total expenses and the individual share.
3. Return both the total and the individual share from the function.
4. Outside the function, use a loop to allow the user to input the cost of each expense and add it to a list.
5. After all expenses are entered, call the 'split_payment()' function with the list of expenses and the number of friends.
6. Display the total expenses and how much each person must pay or be reimbursed.
'''


def split_payment(expenses, number_of_friends):
    total_expenses = sum(expenses)
    individual_share = total_expenses / number_of_friends
    return total_expenses, individual_share

expenses = []

number_of_friends = int(input("Enter the number of friends: "))

while True:
    expense = input("Enter an expense or 'done' to finish. ")
    if expense.lower() == 'done':
        break
    expenses.append(float(expense))

total, share = split_payment(expenses, number_of_friends)
print(f"\nTotal expenses: ${total:.2f}")
print(f"Each person must pay: ${share:.2f}")

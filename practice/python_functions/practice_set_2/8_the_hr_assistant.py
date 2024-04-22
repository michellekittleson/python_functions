'''
Exercise 8: The HR Assistant

You are tasked with managing employee records for a small company. 
Your job is to reate functions that can add new employee skills, calculate average age, and display all employee information using lists instead of dictionaries.

**Instructions**:

1. Define a global list called 'employees' to store employee details, where each employee is represented as a list with elements '[name, age, department]'.
2. Define a function called 'add_employee' that takes name, age, and department as argumets and adds them as a list to the 'employees' list.
3. Define a function called 'calculate_average_age' that computes and returns the average age of all employees.
4. Define a function called 'display_employees' that prints all the employee details in a formatted manner.
5. Use a loop to allow the user to choose between adding an employee, calculating the average age, or displaying all employees.
6. Ensure that the 'employees' list is not reinitialized within the function, maintaining its global scope.
'''

employees = []

def add_employee(name, age, department): # adds the arguments as a list to 'employees' list
    global employees
    employees.append([name, age, department])

def calculate_average_age(): # Computes and returns the average age of all employees
    global employees 
    total_age = sum(employee[1] for employee in employees)
    return total_age / len(employees) if employees else 0

def display_employees(): # Prints all employee details in a formatted manner
    global employees
    for employee in employees:
        print(f"Name: {employee[0]}, Age: {employee[1]}, Department: {employee[2]}")

while True:
    action = input("Choose an action: [A]dd an employee, [C]alculate average age, [D]isplay all employees, [Q]uit: ").upper()
    if action == "A":
        name = input("Enter the employee's name: ")
        age = int(input("Enter the employee's age: "))
        department = input("Enter the employee's department: ")
        add_employee(name, age, department)
    elif action == "C":
        average_age = calculate_average_age()
        print(f"The average age of employees is {average_age:.2f}")
    elif action == "D":
        display_employees() 
    elif action == "Q":
        break
    else:
        print("Invalid action. Please choose again.")

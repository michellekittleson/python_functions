tasks = []

def add_task(added_task):
    added_task = input("Enter the task you would like to add: ")
    tasks.append(added_task)
    print(f"{added_task} has been added to the To Do List.")

def complete_task():
   completed_task = input("Enter the task you would like to check off of your list: ")
   print(f"{completed_task} has been marked complete.")
   del completed_task

def delete_task():
   deleted_task = input("Enter the task you would like to delete: ")
   print(f"{deleted_task} has been deleted from the list.")
   del deleted_task

while True:
    print("\n1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")
    choice = input("Enter your choice: ")
    
    
    if choice == '1':
      add_task(added_task)
    elif choice == "2":
      print(f"Your tasks are: {tasks}")
    elif choice == "3":
      complete_task(completed_task)
    elif choice == "4":
      pass
    elif choice == "5":
      print(f"Exiting program.")
      break
    else:
      print(f"Please enter a valid input.")
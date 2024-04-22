'''
5. The Fitness Tracker

Objective:
The aim of this assignment is to create a program that tracks fitness activities and calories burned.

Task 1: Develop a function to log different fitness activities and their duration. For instance, activities = [’Dancing’, ‘Swimming’, ‘Biking’] and duration = [10, 20, 15] where Dancing corresponds to 10 minutes, Swimming corresponds to 20 minutes, and Biking corresponds to 15 minutes.
Task 2: Write a simple function that estimates calories burned based on the activity and duration. For instance, Total calories burned = Duration (in minutes)*3.5
Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.

'''
total_calories = 0

def log_fitness_activities():
    activity = input("Enter the activity (dancing, swimming, biking): ")
    if activity == "dancing":
        time_dancing = int(input("How many minutes did you dance? "))
        dancing_calories = time_dancing * 7
        total_calories += dancing_calories
        print(f"Congratulations! You have burned {dancing_calories} calories dancing!")
    elif activity == "swimming":
        time_swimming = int(input("How many minutes did you swim? "))
        swimming_calories = time_swimming * 6
        total_calories += swimming_calories
        print(f"Congratulations! You have burned {swimming_calories} calories swimming!")

log_fitness_activities()

def calories_burned():
    pass
def summary():
    pass

activities = ['Dancing', 'Swimming', 'Biking']
duration = [10, 20, 15]

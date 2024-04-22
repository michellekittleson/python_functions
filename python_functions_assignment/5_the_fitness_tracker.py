'''
5. The Fitness Tracker

Objective:
The aim of this assignment is to create a program that tracks fitness activities and calories burned.

Task 1: Develop a function to log different fitness activities and their duration. For instance, activities = [’Dancing’, ‘Swimming’, ‘Biking’] and duration = [10, 20, 15] where Dancing corresponds to 10 minutes, Swimming corresponds to 20 minutes, and Biking corresponds to 15 minutes.
Task 2: Write a simple function that estimates calories burned based on the activity and duration. For instance, Total calories burned = Duration (in minutes)*3.5
Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.

'''

activities = []
duration = []
calories = []

def log_fitness_activities(activities, duration):

    while True:
        activity = input("Enter the activity (dancing, swimming, biking): ")
        minutes = input("How long are you doing the activity in minutes? ")
        activities.append(activity)
        duration.append(minutes)
        if len(activities) >= 3:
            break
        print(activities)
        print(duration)

def calories_burned(calories):
    for time in duration:
        calories.append(int(time) * 3.5)

def summary(activities, duration, calories):
    for i in range(len(activities)):
        print(f"{activities[i]} burned {calories[i]} over {duration[i]} minutes.")

log_fitness_activities(activities, duration)
calories_burned(calories)
summary(activities, duration, calories)



activities = ['Dancing', 'Swimming', 'Biking']
duration = [10, 20, 15]

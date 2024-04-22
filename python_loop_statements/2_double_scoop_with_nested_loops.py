# Task 1: Your Mood Tracker
# Simulate a mood tracker that records your mood at three different times of the day (morning,
# afternoon, evening) for each day of the week. Use nested loops to implement this: the outer loop
# should iterate over the days, and the inner loop should iterate over the times of the day. For each time,
# randomly select a mood from a predefined list and print it.

# Example Outcome: An example would be "On Tuesday afternoon you were sad" "On Tuesday night you
# were happy" "On Wednesday morning you were tired"

import random

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_of_day = ["morning", "afternoon", "evening"]
mood = ["Happy", "Sad", "Energetic", "Calm"]

for day in days:
    for time in time_of_day:
        intermittent_mood = random.choice(mood)
        print(f"On {day} {time}, you were {intermittent_mood}.")
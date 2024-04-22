# Honoring the High Achievers: Iterate over a subset of a list using a for loop. You
# will extract and print the names of the top students in a class.

# Create a list of student names.
# Use slicing to select the top three students.
# Use a for loop to iterate through the sliced list.
# Trint each name with a congratulatory message.

students = ["Student #1", "Student #2", "Student #3", "Student #4", "Student #5"]
top_3 = students[:3]
for student in top_3:
    print(f"Congratulations, {student}, you are among the top performers!")

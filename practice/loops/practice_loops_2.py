# You have 30 students and 5 rows in the classroom.
# Each row can seat an equal number of students.
# Use a loop with the range dunction to assign and print a seat number for each student.
# Seat numbers should start at 1 and increase sequentially.

total_students = 30
rows = 5

students_per_row = total_students // rows

for row in range(1, rows + 1):
    for seat in range(1, students_per_row +1):
        seat_number = (row-1) * students_per_row + seat
        print(f"Row {row} - Seat {seat}: Student {seat_number}")


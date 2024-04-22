# Task #1

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week = temperatures[7:14]
print(second_week)


# Task #2: Extract all the temperatures above 100.

above_100 = temperatures[24:]
print(above_100)

# Should I have done this using some sort of > 100 rather than slicing?



# Task #3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
temperatures.reverse()
fifth_to_tenth = temperatures[4:10]
print(fifth_to_tenth)

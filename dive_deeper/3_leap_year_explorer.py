# Task #1: Leap Year Checker

year = int(input("Enter a year." ))

if year % 400 == 0:
    print(f"The year {year} is a leap year!")
elif year % 100 == 0:
    print(f"The year {year} is NOT a leap year.")
elif year % 4 == 0:
    print(f"The year {year} is a leap year!")
else:
    print(f"The year {year} is NOT a leap year.")
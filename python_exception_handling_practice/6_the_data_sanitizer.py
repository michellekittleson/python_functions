'''
Exercise 6: The Data Sanitizer

In data processing applications, it's common to encounter a mix of valid and invalid data entries.
Your task is to write a program that attempts to convert a list of string values to integers, gracefully handling any values that cannot be converted.

**Instructions**:

1. Create a list of strings where some represent integer values and others are non-numeric.
2. Iterate over the list and attempt to convert each string to an integer.
3. If a string cannot be converted to an integer, catch the 'ValueError' and print a warning message.
4. Store the successfully converted integers in a new list called 'parsed_data'.

**Hints**:

- Use a 'try-except' block within your loop to catch conversion errors.
- Print a warning message in the 'except' block for each non-convertible string.
'''

data_entries = ['100', '200', 'three', '400', '5ive']
parsed_data = []

for entry in data_entries:
    try:
        parsed_data.append(int(entry))
    except ValueError:
        print(f"Warning: '{entry}' is not a valid integer and will be skipped.")

print(f"Parsed Data: {parsed_data}")

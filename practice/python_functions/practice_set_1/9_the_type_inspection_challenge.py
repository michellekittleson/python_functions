'''
Use isinstance() and type() to inspect the types of various elements in a list.

You are creating a program that categorizes elements in a list based on their data type.
The program should iterate over a mixed-type list, identify the data type of each element, and 
sort the elements into separate lists according to their type.

1. Create a mixed-type list with various data types (e.g., integers, floats, strings, booleans).
2. Initialize separate lists to hold elements of each data type.
3. Use a loop to iterate over the mixted-type list.
4. For each element, use isinstance() or type() to determine the element's type.
5. Append the element to the corresponding list based on its type.
6. Use shorthand if statements to streamline the type-checking logic.
7. Print out the categorized lists after processing the entire mixed-type list.

'''

mixed_list = [10, 3.14, "Python", False, 42, "Code", 2.718, True]
integers = []
floats = []
strings = []
booleans = []

for element in mixed_list:
    if isinstance(element, int) and not isinstance(element, bool):

# "and not" is necessary because booleans are a subclass of integers and include 0 and 1.

        integers.append(element)
    elif isinstance(element, float):
        floats.append(element)
    elif isinstance(element, str):
        strings.append(element)
    elif isinstance(element, bool):
        booleans.append(element)
    else:
        print(f"Unknown type: {type(element)}")

print(f"Integers: {integers}")
print(f"Floats: {floats}")
print(f"Strings: {strings}")
print(f"Booleans: {booleans}")
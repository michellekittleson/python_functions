# Task #1:  Given the two lists: submitted = ["Alice", "Bob", "Charlie", "David"] attended = ["Charlie", "Eve", "Alice", "Frank"]Find out which students both submitted their assignments and attended the class.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

both = set(submitted) & set(attended)

print(both)

# Should I be using set? I don't believe we learned this, I found it on the internet.


# Task #2: Check if the two lists are identical in terms of their content, regardless of order.

if submitted is attended:
    print("They are identical!")
else:
    print("They are not identical.")


# Task #3: Using list methods, remove any student from the attended list who did not submit their assignment.

attended.remove("Eve")
attended.remove("Frank")
print(attended)

# Is there a way to do this besides just removing students one at a time?
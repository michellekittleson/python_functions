# Task 1: Loop Condition Exploration
# Write a while loop with a condition that will never be true (an infinite loop). Inside the loop,
# print a statement. Then, use a break statement to exit the loop after 5 iterations.
x = 0

while True:
    x += 1
    if x == 6:
        break
    print(x) 



# Task 2: Conditional Exit
# Modify the infinite loop from Task 1 to include a condition that will eventually be true and
# remove the break statement. The loop should terminate naturally once the condition is met.

x = 0
while x < 6:
    x += 1
    print(x)


# Lucky Draw Simulation: Use loops in conjunction with random selection, simulating real-world scenarios
# where random dras or selections are required.

# Import the random module to use its choice selection capabilities.
# Create a list of participant names, including "Alex".
# Use a while loop to repeatedly draw a name randomly from the list of participants.
# The loop should only terminate when "Alex" is drawn.
# Ensure the loop does not produce any output until "Alex" is drawn.


# My try:
import random
names = ["Alex", "Bob", "Patrick"]
picked_name = []

while picked_name != "Alex":
    picked_name = random.choice(names)
else:
    print("Alex is drawn!")


# Video Explanation:
participants = ["John", "Lila", "Sarah", "Alex", "Max"]

while "Alex" not in random.choices(participants, k=1):
    pass
print("Congratulations, Alex! You've won the lucky draw")

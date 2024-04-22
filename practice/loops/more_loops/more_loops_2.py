# Random Walk Simulation: Simulate random processes and make use of random choices in a controlled loop.

# Import the random module to utilize its random selection feature.
# Define a list of directions that the entity can take.
# Use a for loop to simulate 10 steps.
# In each iteration, randomly select a direction and simulate taking a step in that direction.
# Print out the direction of each step.

import random
directions = ["North", "South", "East", "West"]

for step in range(10):
    step_direction = random.choice(directions)
    print(f"Step {step + 1}: The entity moves 10 steps to the {step_direction}.")
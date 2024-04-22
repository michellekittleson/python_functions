# Dynamic Color Generation: Work with random number generation and apply it 
# to practical scenarios such as creating color values.

# Import the random module
# Create a loop that will run a specified number of times to generate random color values.
# In each iteration, generate three separate numbers ranging from 0 to 255, representing the Red, Green, and Blue (RGB) componenets of a color.
# Print out the generated RGB color value in a readable format.

import random

num_colors = 10

for _ in range(num_colors):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    print(f"generated RGB color: ({red}, {green}, {blue})")
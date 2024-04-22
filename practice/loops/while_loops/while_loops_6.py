# The Smart Traffic Light System: Use while loops and with an infinite loop and a break condition, 
# as well as to practice using lists and the count method in Python.

# Create a list of colors representing the light sequence.
# Initialize a counter for the green light.
# Use an infinite while loop to cycle through the traffic light colors.
# Inside the loop, use the count method to track the number of times "green" appears.
# Break the loop when the green light has appeared a specific number of times.
# Print a message each time the light changes and when the loop breaks for maintenance.

traffic_lights = ["red", "yellow", "green", "yellow"]
green_count = 0

while True:
    for color in traffic_lights:
        print(f"The traffic light is now {color}.")
        if color == "green":
            green_count += 1
            if green_count == 3:
                print("Maintenance time! The cycle will stop.")
                break
    if green_count == 3:
        break
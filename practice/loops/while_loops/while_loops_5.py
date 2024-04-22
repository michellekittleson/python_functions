# The Intelligent Elevator System: Use while loops, lists, and the membership operator in Python 
# to simulate an intelligent elevator system that stops at specific floors based on a list of requests.

# Initialize the starting floor
current_floor = 5
# List of requested stops
requested_stops = [1, 3, 4]

# Star the elevator
while current_floor > 0:
    # Check if the current floor is a requested stop
    if current_floor in requested_stops:
        print(f"Stopping at floor {current_floor}.")
        requested_stops.remove(current_floor)
    # Move the elevator down a floor
    current_floor -= 1
    print(f"Descending to floor {current_floor}.")

# Ground floor reached
print("The elevator has reached the ground floor.")
# The Patient Queue: Use a while loop to manage a queue system.

# Initialize the number of patients in the queue
patients = 5

# Process the queue
while patients > 0:
    print(f"Patient number {patients} please come in.")
    patients -= 1 # Call the next patient

# All patients have been called
print("There are no more patients in the queue.")
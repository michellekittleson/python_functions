# Booth types: ["Food", "Games", "Music", "Crafts"]
# Schedule times: ["10:00 AM", "1:00 PM", "3:00 PM", "5:00 PM"]
# Items needed: ["Grill", "Tickets", "Instruments", "Paint"]

# Use a loop to iterate over the booth types.
# For each booth type, print the type of booth, the schedule time, and the item needed.
# Ensure that each booth type is matched with the correct schedule time and item needed from the list provided.


booth_types = ["Food", "Games", "Music", "Crafts"]
schedule_times = ["10:00 AM", "1:00 PM", "3:00 PM", "5:00 PM"]
items_needed = ["Grill", "Tickets", "Instruments", "Paint"]

for i in range(len(booth_types)):
    booth = booth_types[i]
    time = schedule_times[i]
    item = items_needed[i]
    print(f"{booth} Booth - Schedule: {time}, Item needed: {item}")

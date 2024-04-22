# List representing caves, "True" indicates the cave with the treasure

caves = [False, False, True, False, False]

# Iterate over the caves
for index, cave in enumerate(caves):
    # Check if the cave has the treasure
    if cave:
        print(f"Treasure found in cave {index +1}!")
        break # Stop searching once the treasure is found
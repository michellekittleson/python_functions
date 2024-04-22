# Task 1: The for Loop DJ Set
# Using the provided genres list, write a for loop that prints out each genre with a custom
# message. Extend this task by adding a counter that displays the number of the track before the
# genre.

# Our playlist of genres
genres = ["Jazz", "Rock", "Hip-hop", "Classical"]
track = genres.index

for genre in genres:
    if genre == "Jazz":
        print(f"Track 1 - {genre}: A classic genre that loves the saxophone!")
    elif genre == "Rock":
        print(f"Track 2 - {genre}: A guitar player's dream!")
    elif genre == "Hip-hop":
        print(f"Track 3 - {genre}: Where you'll find the best beats!")
    elif genre == "Classical":
        print(f"Track 4 - {genre}: The best way to communicate feelings through music without words!")

# Task 2: The Remix Artist with while
# Convert the for loop from Task 1 into a while loop. Ensure it performs the same function but
# also includes a condition to stop the loop if a certain genre is played for instance Hip-hop.

genres = ["Jazz", "Rock", "Hip-hop", "Classical"]

track_num = 0

stop_play = False

while stop_play == False:
    if genres[track_num] == "Hip-hop":
        print("We don't do Hip-hop in this house!")
        stop_play = True
    else:
        print(f"{genres[track_num]} is playing.")
    track_num += 1

#     for genre in genres:
#         if genre == "Hip-hop":
#             stop_play = True
#             break
#         print(f"We are now playing {genre} music.")


# Task 3: Light Show Technician Loop
# Using the range() function, loop through the genres list by index. For each genre, print out
# the track number and a message that the light show is ready. Modify the loop to skip a genre if
# it's not suitable for the light show, for instance Classical genre.

genres = ["Jazz", "Rock", "Hip-hop", "Classical"]
for i in range(len(genres)):
    if genres[i] == "Classical" or genres[i] == "Jazz":
        print("There's no light show for this!")
    else: 
        print(f"The light show is ready for Track number {i + 1}, it is a {genres[i]} show!")        

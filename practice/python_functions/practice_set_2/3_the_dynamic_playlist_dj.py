'''
Exercise 3: The Dynamic Playlist DJ

You are developing a feature for a music app that allows users to create a custom playlist and play the songs in sequence.

**Instructions**:

1. Define a function called 'play_songs()' that takes one parameter 'song_list'.
2. Inside the function, use a loop to iterate over 'song_list'.
3. For each song in the list, print a message indicating that the song is now playing.
4. Before calling the function, prompt the user to enter the number of songs they want to add to the playlist.
5. Use a loop and 'input()' to accept song names from the user, based on the number they provided, and store them in a list.
6. Call the 'play_songs()' function with the user-created list of songs as an argument.
'''

def play_songs(song_list):
    for song in song_list:
        print(f"Now playing: {song} ")

num_songs = int(input("How many songs would you like to add to the playlist? "))

user_playlist = []

for i in range(num_songs):
    song_name = input(f"Enter song {i+1}: ")
    user_playlist.append(song_name)

play_songs(user_playlist)
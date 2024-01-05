import pandas as pd
import random

from pandas.core.array_algos.take import _view_wrapper

def list_available_playlists():
    # Load the DataFrame from the playlist table
    playlist_df = pd.read_csv('data/playlist.csv')

    # Display the list of available playlists
    available_playlists = playlist_df['id_playlist'].unique()
    print("\033[1m Available Playlists: \033[0;0m")
    for i in range(1, len(available_playlists), 1):
        print(" ", available_playlists[i])

def choose_random_music(tableMusic_df):
    # Choose a music randomly
    random_music = tableMusic_df.sample(n=1)

    return random_music

def view_playlist_songs(playlist_name):
    while True:
        # Load the DataFrame from the playlist table
        playlist_df = pd.read_csv('data/playlist.csv', names=['id_playlist', 'duration_playlist', 'id_music', 'rating_playlist', 'average_rating_musics', 'num_ratings'])

        # Check if the user wants to exit
        if playlist_name == '0':
            print(" Quitting...")
            break

        # Locate the playlist based on the name
        selected_playlist = playlist_df[playlist_df['id_playlist'].str.lower() == playlist_name.lower()]

        # Check if the playlist was found
        if not selected_playlist.empty:
            # Get the IDs of the songs in the playlist
            songs_ids = selected_playlist['id_music']

            # Load the DataFrame from the music table
            tableMusic_df = pd.read_csv('data/tableMusic.csv', names=['id_music', 'style', 'type', 'title', 'songwritter', 'year', 'artist', 'rating_global', 'rating_user', 'duration'])

            # Filter the songs from the desired playlist
            songs_info = tableMusic_df[tableMusic_df['id_music'].isin(songs_ids)][['title', 'style', 'year', 'artist', 'rating_global']]

            # Display the songs in the playlist with global rating in table format
            print("\nSongs in the playlist:")
            print(songs_info.to_markdown(index=False))

            while True:
                # Ask the user what they want to do
                option = input("""\n\033[1m further info: \033[0;0m\n\033[1m 1 \033[0;0m duration\n\033[1m 2 \033[0;0m rating\n\033[1m 0 \033[0;0m back\n (enter a number) => """)


                if option == '1':
                    # Get information about the playlist
                    playlist_duration = selected_playlist.iloc[0]['duration_playlist']
                    print(f"\nPlaylist duration: {playlist_duration} minutes")
                elif option == '2':
                    # Get information about the playlist
                    playlist_rating = selected_playlist.iloc[0]['rating_playlist']
                    print(f"\n Playlist rating: {playlist_rating}")
                elif option == '0':
                    break
                else:
                    print(" \033[1m WARNING: \033[0;0mInvalid option. Please try again.")
            return
        else:
            print(f"\033[1m WARNING: \033[0;0m Playlist '{playlist_name}' not found. Please try again.")

# Call the function to allow the user to choose a playlist and view the songs

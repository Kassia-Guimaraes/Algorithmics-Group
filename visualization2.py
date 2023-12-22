import pandas as pd
import random

def list_available_playlists():
    # Load the DataFrame from the playlist table
    playlist_df = pd.read_csv('data/playlist.csv', names=['id_playlist', 'duration_playlist', 'id_music', 'rating_playlist', 'average_rating_musics', 'num_ratings'])

    # Display the list of available playlists
    available_playlists = playlist_df['id_playlist'].unique()
    print("Available Playlists:")
    print(available_playlists)

def choose_random_music(tableMusic_df):
    # Choose a music randomly
    random_music = tableMusic_df.sample(n=1)

    return random_music

def view_playlist_songs():
    while True:
        # Load the DataFrame from the playlist table
        playlist_df = pd.read_csv('data/playlist.csv', names=['id_playlist', 'duration_playlist', 'id_music', 'rating_playlist', 'average_rating_musics', 'average_rating_musics'])

        # Display the list of available playlists
        list_available_playlists()

        # Ask the user for the playlist name
        playlist_name = input("Enter the name of the playlist you want to view (or 'exit' to quit): ")

        # Check if the user wants to exit
        if playlist_name.lower() == 'exit':
            print("Exiting the application...")
            break

        # Locate the playlist based on the name
        selected_playlist = playlist_df[playlist_df['id_playlist'] == playlist_name]

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
                option = input("\nDo you want to view the duration of the playlist, its rating, or the song that is playing? (Type 'duration', 'rating', 'play' or 'exit'): ")

                if option.lower() == 'duration':
                    # Get information about the playlist
                    playlist_duration = selected_playlist.iloc[0]['duration_playlist']
                    print(f"\nPlaylist Duration: {playlist_duration} minutes")
                elif option.lower() == 'rating':
                    # Get information about the playlist
                    playlist_rating = selected_playlist.iloc[0]['rating_playlist']
                    print(f"\nPlaylist Rating: {playlist_rating}")
                elif option.lower() == 'play':
                    # Choose a music randomly
                    random_music = choose_random_music(tableMusic_df)

                    # Display information about the random music
                    print("\nPlaying song:")
                    print(random_music.to_markdown(index=False))
                elif option.lower() == 'exit':
                    print("Returning to the playlist selection...")
                    break
                else:
                    print("Invalid option. Please try again.")
        else:
            print(f"Playlist '{playlist_name}' not found. Please try again.")

# Call the function to allow the user to choose a playlist and view the songs
view_playlist_songs()

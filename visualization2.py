import pandas as pd
import random

def list_available_playlists():
    # Load the DataFrame from the playlist table
    playlist_df = pd.read_csv('data/playlist.csv', names=['id_playlist', 'duration_playlist', 'id_music', 'rating_playlist', 'average_rating_musics', 'num_ratings'])

    # Display the list of available playlists
    available_playlists = playlist_df['id_playlist'].unique()
    print("\033[1m Available Playlists: \033[0;0m")
    for i in range(1, len(available_playlists), 1):
        print("\033[1m", i, "\033[0;0m", available_playlists[i])

def choose_random_music(tableMusic_df):
    # Choose a music randomly
    random_music = tableMusic_df.sample(n=1)

    return random_music

def view_playlist_songs():
    while True:
        # Load the DataFrame from the playlist table
        playlist_df = pd.read_csv('data/playlist.csv', names=['id_playlist', 'duration_playlist', 'id_music', 'rating_playlist', 'average_rating_musics', 'num_ratings'])

        # Display the list of available playlists
        list_available_playlists()

        # Ask the user for the playlist name
        playlist_name = input(" pick a playlist (type '0' to quit) => ")

        # Check if the user wants to exit
        if playlist_name == '0':
            print("Quitting...")
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
                option = input("""\n\033[1m Available info: \033[0;0m\n\033[1m 1 \033[0;0m duration\n\033[1m 2 \033[0;0m rating\n\033[1m 3 \033[0;0m play\n\033[1m 0 \033[0;0m back\n (enter a number) => """)


                if option == '1':
                    # Get information about the playlist
                    playlist_duration = selected_playlist.iloc[0]['duration_playlist']
                    print(f"\nPlaylist Duration: {playlist_duration} minutes")
                elif option == '2':
                    # Get information about the playlist
                    playlist_rating = selected_playlist.iloc[0]['rating_playlist']
                    print(f"\nPlaylist Rating: {playlist_rating}")
                elif option == '3':
                    # Choose a music randomly
                    random_music = choose_random_music(tableMusic_df)

                    # Display information about the random music
                    print("\nPlaying song:")
                    print(random_music.to_markdown(index=False))
                elif option == '0':
                    print("Returning to the playlist selection...")
                    break
                else:
                    print("Invalid option. Please try again.")
        else:
            print(f"Playlist '{playlist_name}' not found. Please try again.")

# Call the function to allow the user to choose a playlist and view the songs

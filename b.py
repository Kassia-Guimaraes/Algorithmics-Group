import pandas as pd
from dataBase import get_new_id

tm = pd.read_csv("data/tableMusic.csv", sep=",")

def automatic_playlist():
    while True:
        music_rating_max = tm[(tm['rating_global'] > 4)].sample(10)
        music_rating_min = tm[(tm['rating_global'] <= 4)].sample(5)

        playlist_df = pd.concat([music_rating_max, music_rating_min])
        duration_total = playlist_df['duration'].sum()

        if duration_total <= 3600:
            break

    return playlist_df

def create_playlist():
    created_playlists = []

    while True:
        flag = input("Do you want to create a new automatic playlist? (Y/N) ").strip().lower()

        if flag != 'y':
            break

        playlist_id = get_new_id()
        name_playlist = f'play_auto_{playlist_id}'

        play_auto = automatic_playlist()
        play_auto['id_playlist'] = name_playlist

        created_playlists.append(play_auto)

        count_style = play_auto['style'].value_counts()
        duration_playlist = play_auto['duration'].sum()
        play_auto['duration_playlist'] = duration_playlist

        print(f"Playlist '{name_playlist}' created successfully!")
        print(play_auto[['id_music', 'title', 'rating_global', 'style', 'year']].to_markdown(index=False))
        print("\nSongs per style:")
        print(count_style)

        rating_playlist = float(input("What grade do you give to the playlist (1-5)? "))
        average_rating = "{:.1f}".format(play_auto['rating_global'].mean())
        id_songs_playlist = list(set(play_auto['id_music']))

        new_playlist_auto = {"id_playlist": name_playlist, "duration_playlist": duration_playlist,
                              "id_music": id_songs_playlist, "rating_playlist": rating_playlist,
                              "average_rating_musics": average_rating}

        created_playlists_df = pd.concat(created_playlists, ignore_index=True)

        # Print the DataFrame of the current playlist
        print(f"\nPlaylist '{name_playlist}':")
        print(play_auto[['id_music', 'title', 'style', 'duration', 'duration_playlist']])

    return created_playlists_df

created_playlists_df = create_playlist()

# Print the DataFrame with all created playlists
#print("\nAll Created Playlists:")
#print(created_playlists_df[['id_playlist', 'id_music', 'title', 'style', 'duration', 'duration_playlist']])
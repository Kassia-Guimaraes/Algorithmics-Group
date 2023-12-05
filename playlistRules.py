import pandas as pd
from dataBase import get_new_id #generate id fuc

tm = pd.read_csv("data/tableMusic.csv", sep=(","))

def create_play():
    while True:
        music_rating_max = tm[(tm['rating_global'] > 4)].sample(10) # 10 songs with rating > 4
        music_rating_min = tm[(tm['rating_global'] <= 4)].sample(5) # 5 songs with rating <= 4

        playlist = pd.concat([music_rating_max, music_rating_min])
        duration_total = playlist['duration'].sum() # total playlist duration

        if duration_total <= 3600: # total duration <= 60 minutes, 3600 seconds
            break

    return playlist # return the playlist DataFrame

created_playlists = []  # store all created playlists

# Main
while True:
    flag = input("Do you want to create a new automatic playlist? (Y/N) ").strip().lower()

    if flag != 'y':
        break

    new_playlist_id = get_new_id()  # get a new unique playlist ID
    name_playlist = f'play_auto_{new_playlist_id}'  # save as play_auto and the playlist number

    play_auto = create_play()
    play_auto['id_playlist'] = name_playlist  # assign the playlist ID

    created_playlists.append(play_auto) # add new playlist_auto to the list

    count_style = play_auto['style'].value_counts()

    # Add the 'duration_playlist' column to the DataFrame
    duration_playlist = play_auto['duration'].sum()
    play_auto['duration_playlist'] = duration_playlist
    
    print(f"Playlist '{name_playlist}' created successfully!")
    print(play_auto[['id_music','title', 'rating_global', 'style', 'year']])
    print("\nSongs per style:")
    print(count_style)
    
    rating_playlist = float(input("What grade do you give to the playlist (1-5)? ")) #user rating playlist
    average_rating = "{:.1f}".format(play_auto['rating_global'].mean()) #averange rating songs in playlist
    id_songs_playlist = list(set(play_auto['id_music']))

    new_playlist_auto = {"id_playlist": name_playlist, "duration_playlist": duration_playlist, "id_music": id_songs_playlist, "rating_playlist": rating_playlist, "average_rating_musics": average_rating}

# Create a DataFrame containing all created playlists
created_playlists_df = pd.concat(created_playlists, ignore_index=True)

# Print the DataFrame with all created playlists
print("\nAll Created Playlists:")
print(created_playlists_df[['id_playlist', 'id_music', 'title', 'style', 'type', 'duration', 'duration_playlist']])
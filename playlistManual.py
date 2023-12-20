import pandas as pd
from filterStyle import applyFilters

#Get the user parameters
def getUsersFilters(df): #df = tableMusic_df
    available_columns = df.columns.tolist()
    filterList = []

    while True:
        print("Available columns:")
        for i, column in enumerate(available_columns, start=1): #menu starts in 1
            print("\033[1m", i, "\033[0;0m ", column)
        print("\033[1m", "0", "\033[0;0m ", "(next)")

        try:
            choice = int(input("Choose a column to filter: "))

            if choice == 0: #next
                break
            elif 1 <= choice <= len(available_columns):
                selected_column = available_columns[choice - 1] #array index, value - 1
                filterList.append(selected_column) #list with parameters
                print(f"Selected column: {filterList}\n")
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:  
            print("Invalid choice. Please enter a number.")

    print("Selected filters:", filterList)
    return filterList #return array with filters, used on apllyFilters

# "filtersList" is the array of the columns to filter, "loc_df" is the the path to the csv file 
def createPlaylist(filtersList, loc_df):
    selectedSongs_df = pd.DataFrame()
    filtered_songs_df = applyFilters(filtersList, loc_df) #menu with filters
    name_playlist = input("Enter a name for your playlist: ") #playlist name

    add_playlist_df = pd.DataFrame()

    while True:
        try:
            selected_song_id = int(input("Enter the ID of the song you want to add (0 to finish, -1 to create new filters): "))
            
            if selected_song_id == 0:
                break
            elif selected_song_id == -1: #add new filters
                new_filters_list = getUsersFilters(tableMusic_df)
                filtered_songs_df = applyFilters(new_filters_list, loc_df)
            else:
                selected_song = tableMusic_df[tableMusic_df['id_music'] == selected_song_id] #select songs per id to add on playlist
                selectedSongs_df = pd.concat([selectedSongs_df, selected_song])

                print(f"Added song to the playlist: {name_playlist}\n{selectedSongs_df[['id_music', 'title', 'artist', 'style', 'year']].to_markdown(index=False)}\n")

        except ValueError:
            print("Invalid value. Please enter a valid song ID.")

    duration_playlist = selectedSongs_df['duration'].sum()
    print(f'Duration Playlist: {duration_playlist}')

    average_rating = "{:.1f}".format(selectedSongs_df['rating_global'].mean()) #averange rating songs in playlist
    
    print(f"\nYour Created Playlist: {name_playlist}\t Duration Playlist: {duration_playlist}\n{selectedSongs_df[['id_music', 'title', 'artist', 'style', 'year']].to_markdown(index=False)}")
    rating_playlist = float(input("What grade do you give to the playlist (1-5)? ")) #user rating playlist

    id_songs_playlist = list(set(selectedSongs_df['id_music']))

    for id_songs in id_songs_playlist: #loop for add all songs in csv file
        add_music = {'id_playlist': name_playlist, 'duration_playlist': duration_playlist,'id_music': id_songs,'rating_playlist': rating_playlist,'average_rating_musics': average_rating}
        playlist_manual_df = pd.DataFrame([add_music]) #dictionary to dataFrame
        add_playlist_df = pd.concat([add_playlist_df,playlist_manual_df], ignore_index=True) #concat all songs in only dataframe

    new_playlist = pd.concat([playlist_df,add_playlist_df]) #concat the new playlist with rest of playlists
    new_playlist = new_playlist.set_index('id_playlist')

    #new_playlist.to_csv('jukebotify/data/playlist.csv') #add in csv file
    return selectedSongs_df #return the playlist

# Main program
tableMusic_df = pd.read_csv("data/tableMusic.csv", sep=',')
playlist_df = pd.read_csv('data/playlist.csv')
filters_list = getUsersFilters(tableMusic_df)
createPlaylist(filters_list, "data/tableMusic.csv")
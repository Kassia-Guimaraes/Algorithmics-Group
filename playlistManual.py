import pandas as pd
from a import applyFilters

#Get the user parameters
def get_user_filters(df): #df = tablemusic_df
    available_columns = df.columns.tolist()
    filter_list = []

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
                filter_list.append(selected_column) #list with parameters
                print(f"Selected column: {filter_list}\n")
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:  
            print("Invalid choice. Please enter a number.")

    print("Selected filters:", filter_list)
    return filter_list #return array with filters, used on apllyFilters

# "filtersList" is the array of the columns to filter, "loc_df" is the the path to the csv file 
def create_playlist(filtersList, loc_df):
    selected_songs_df = pd.DataFrame()
    filtered_songs_df = applyFilters(filtersList, loc_df) #menu with filters
    name_playlist = input("Enter a name for your playlist: ") #playlist name

    while True:
        try:
            selected_song_id = int(input("Enter the ID of the song you want to add (0 to finish, -1 to create new filters): "))
            
            if selected_song_id == 0:
                break
            elif selected_song_id == -1: #add new filters
                new_filters_list = get_user_filters(tableMusic_df)
                filtered_songs_df = applyFilters(new_filters_list, loc_df)
            else:
                selected_song = tableMusic_df[tableMusic_df['id_music'] == selected_song_id] #select songs per id to add on playlist
                selected_songs_df = pd.concat([selected_songs_df, selected_song])

                print(f"Added song to the playlist: {name_playlist}\n{selected_songs_df[['id_music', 'title', 'artist', 'style', 'year']].to_markdown(index=False)}\n")

        except ValueError:
            print("Invalid value. Please enter a valid song ID.")

    print(f"\nYour Created Playlist: {name_playlist}\n{selected_songs_df[['id_music', 'title', 'artist', 'style', 'year']].to_markdown(index=False)}")

    return selected_songs_df #return the playlist

# Main program
tableMusic_df = pd.read_csv("data/tableMusic.csv", sep=',')
filters_list = get_user_filters(tableMusic_df)
create_playlist(filters_list, "data/tableMusic.csv")
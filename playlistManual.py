import pandas as pd
from a import applyFilters
import pandas as pd

def get_user_filters(df):
   # Getting the list of all available columns
    available_columns = df.columns.tolist()

    # Initializing the list of filters
    filter_list = []

    # Displaying the menu for the user
    while True:
        print("Available columns:")
        for i, column in enumerate(available_columns, start=1):
            print("\033[1m", i, "\033[0;0m ", column)

        print("\033[1m", "0", "\033[0;0m ", "(next)")

        try:
            choice = int(input("Choose a column to filter: "))

            if choice == 0:
                break
            elif 1 <= choice <= len(available_columns):
                selected_column = available_columns[choice - 1]
                filter_list.append(selected_column)
                print(f"Selected column: {filter_list}\n")
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Returning the final list of chosen parameters
    print("Selected filters:", filter_list)
    return filter_list

# Function to create a playlist based on predefined filters
def create_playlist(filters_list, df):

    # applyFilters returns a DataFrame with filtered songs
    filtered_songs_df = applyFilters(filters_list, df)

    # Get user inputs for playlist name and selected song IDs
    name_playlist = input("Enter a name for your playlist: ").strip().lower().replace(' ', '_')
    selected_song_ids = int(input("Enter the IDs of the songs you want to add: "))

    # Filter the songs based on user-selected IDs
    selected_songs_df = tableMusic_df[tableMusic_df['id_music']==selected_song_ids]

    # Create a new column for the playlist name
    selected_songs_df['id_playlist'] = name_playlist

    return selected_songs_df

# Main program
tableMusic_df = pd.read_csv("data/tableMusic.csv", sep=(','))
filters_list = get_user_filters(tableMusic_df)
# Create a playlist based on user inputs
user_playlist = create_playlist(filters_list, 'data/tableMusic.csv')

# Display the created playlist
print("\nYour Created Playlist:")
print(user_playlist[['id_playlist', 'id_music', 'title', 'artist', 'style', 'year']].to_markdown(index=False))
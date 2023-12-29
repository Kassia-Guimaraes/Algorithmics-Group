import pandas as pd
from auxiliarFunctions import getPlaylist
from auxiliarFunctions import getPlaylist
import errorCodes as ec


### .PY file to test removeSong.py functions ###

def removeSongDatabase():
    #Reads TableMusic and Playlist CSVs into dataframe variables
    tableMusic_df = pd.read_csv('data/tableMusic.csv')
    playlist_df = pd.read_csv('data/playlist.csv')

    #Shows all the available songs
    print("These are the songs in the data base: ")
    print(tableMusic_df)

    #Testing function that removes a song from the entire database (tableMusic and playlists)
    print("Choose one song to remove from the data base")
    songId = input(" Enter song id => ")
    try:
        removeSongDataBase(tableMusic_df, playlist_df, int(songId))
    except:
        print("\033[1m WARNING: \033[0;0minvalid input")
        removeSongDatabase()
    print(tableMusic_df)
    print(playlist_df)




# function responsible for remove a song for the database and for the playlist in the same time.
def removeSongDataBase(tableMusic, playlists, id):
    #the condition sees if the index is in the dataframe tableMusic
    if id in tableMusic["id_music"].values:
       # .drop is the pandas function to remove anything; and get boolean array of music id matches
       tableMusic.drop(tableMusic[tableMusic["id_music"] == id].index,inplace=True)
       playlists.drop(playlists[playlists["id_music"] == id].index, inplace = True)
       #tableMusic and playlists are the dataframes where the music is going to be removed.
       tableMusic.to_csv("data/tableMusic.csv", index=False)
       playlists.to_csv("data/playlist.csv", index=False)
    else :
        print("\033[1m WARNING: \033[0;0mThis song is not in our system. Please chose a valid option => ")


def removeSongPlaylist(playlists, playListName):
    songId = input(" Enter index of song to be removed from " + playListName + "(0 to return) => ")
    #gets chosen playlist
    playlist = getPlaylist(playlists,playListName)

    #checks if chosen id is in playlist
    if songId in str(playlist["id_music"].values):
        #get boolean array of playlist matches
        playListMatch = playlists["id_playlist"] == playListName
        #get boolean array of music id matches
        idMatch = playlists["id_music"] == int(songId)
        #get indexes of songs to remove from playlist
        removeIndex = playlists[playListMatch & idMatch].index
        #removes from playLists dataframe the specified song of the specified playlist
        playlists.drop(removeIndex, inplace = True)

        try:
            playlists.to_csv("data/playlist.csv", index = False)
            print(getPlaylist(playlists, playListName))
        #error message from file errorCode
        except:
            return ec.file_open
    elif songId == "0":
        return
    else :
        print("\033[1m WARNING: \033[0;0mNonexistent song/playlist.")
        removeSongPlaylist(playlists, playListName)

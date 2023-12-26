import pandas as pd
import removeSong
from auxiliarFunctions import getPlaylist

### .PY file to test removeSong.py functions ###

def removeSongFun():
    #Reads TableMusic and Playlist CSVs into dataframe variables
    tableMusic_df = pd.read_csv('data/tableMusic.csv')
    playlist_df = pd.read_csv('data/playlist.csv')

    #Shows all the available songs
    print("These are the songs in the data base: ")
    print(tableMusic_df)

    #Testing function that removes a song from the entire database (tableMusic and playlists)
    print("Choose one song to remove from the data base")
    songId = input("Enter song id: ")
    songId = int(songId)
    removeSong.removeSongDataBase(tableMusic_df, playlist_df, songId)

    print(tableMusic_df)
    print(playlist_df)

    #Testing function that removes a song from a playlist
    print("These are the playlists:")
    print(playlist_df)

    playListName = input("Enter a playlist name: ")
    songId = input("Enter index song to be removed from the playlist: ")
    songId = int(songId)
    removeSong.removeSongPlaylist(playlist_df, playListName, songId)

    print(getPlaylist(playlist_df, playListName))

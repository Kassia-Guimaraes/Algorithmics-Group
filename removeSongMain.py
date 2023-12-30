import pandas as pd
import removeSong
from auxiliarFunctions import getPlaylist
import errorCodes as ec

### .PY file to test removeSong.py functions ###

#Reads TableMusic and Playlist CSVs into dataframe variables
tableMusic_df = pd.read_csv('data\\tableMusic.csv')
playlist_df = pd.read_csv('data\\playlist.csv')

#Shows all the available songs
print("These are the songs in the data base: ")
print(tableMusic_df)

errorCode = removeSong.removeSongDataBase(tableMusic_df, playlist_df)

print(ec.messages[errorCode])

   
#Testing function that removes a song from a playlist
print("These are the playlists:")
print(playlist_df)

errorCode = removeSong.removeSongPlaylist(tableMusic_df, playlist_df)
print(ec.messages[errorCode])

    

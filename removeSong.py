from auxiliarFunctions import getPlaylist
import errorCodes as ec

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


def removeSongPlaylist(playlists, playListName, id):
    #gets chosen playlist
    playlist = getPlaylist(playlists,playListName)

    #checks if chosen id is in playlist
    if id in playlist["id_music"].values:
        #get boolean array of playlist matches
        playListMatch = playlists["id_playlist"] == playListName
        #get boolean array of music id matches
        idMatch = playlists["id_music"] == id
        #get indexes of songs to remove from playlist
        removeIndex = playlists[playListMatch & idMatch].index
        #removes from playLists dataframe the specified song of the specified playlist
        playlists.drop(removeIndex, inplace = True)

        try:
            playlists.to_csv("data/playlist.csv", index = False)
        #error message from file errorCode
        except:
            return ec.file_open
    else :
        print("\033[1m WARNING: \033[0;0mNonexistent song/playlist. Please chose a valid option => ")
        removeFromPlaylist(playlists, playListName)

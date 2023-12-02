from auxiliarFunctions import getPlaylist

def removeSongDataBase(tableMusic, playlists, id):
    
    if id in tableMusic["id_music"].values:
       tableMusic.drop(tableMusic[tableMusic["id_music"] == id].index,inplace=True)
       playlists.drop(playlists[playlists["id_music"] == id].index, inplace = True)
       tableMusic.to_csv("tableMusic.csv",index=False)
       playlists.to_csv("playlist.csv",index=False)     
    else : 
        print("This song does not exist in our system. Please chose a valid option:")
        
def removeSongPlaylist(playlists, playlistName, id):
    #gets chosen playlist
    playlist = getPlaylist(playlists,playlistName)
    
    #checks if chosen id is in playlist
    if id in playlist["id_music"].values:
        #get boolean array of playlist matches
        playListMatch = playlists["id_playlist"] == playlistName
        #get boolean array of music id matches
        idMatch = playlists["id_music"] == id
        #get indexes of songs to remove from playlist
        removeIndex = playlists[playListMatch & idMatch].index
        #removes from playLists dataframe the specified song of the specified playlist
        playlists.drop(removeIndex, inplace = True)
        playlists.to_csv("playlist.csv",index = False)     
    else : 
        print("The chosen playlist doesnt exist or the song is not in the playlist. Please chose a valid option:")

    
    

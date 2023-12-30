import pandas as pd
from auxiliarFunctions import getPlaylist
import errorCodes as ec
import auxiliarFunctions as af

tableMusic = pd.read_csv('data\\tableMusic.csv')

# function responsible for remove a song for the database and for the playlist in the same time.
def removeSongDataBase(tableMusic, playlists):
    #the condition sees if the index is in the dataframe tableMusic
    #Testing function that removes a song from the entire database (tableMusic and playlists)
    print("Choose one song to remove from the data base")
    
    songId = input("Enter song id: ")
    try:
        songId = int(songId)
        
    except:
        return ec.sintax
    
    if not((songId == tableMusic["id_music"]).any()):
        return ec.song_not_found   
   
    # .drop is the pandas function to remove anything; and get boolean array of music id matches
    tableMusic.drop(tableMusic[tableMusic["id_music"] == songId].index, inplace=True)
    playlists.drop(playlists[playlists["id_music"] == songId].index, inplace = True)
        
         
    try: 
        tableMusic.to_csv("data\\tableMusic.csv", index= False) 
        print(tableMusic)
        
    except:
        return ec.file_open
    
    print(tableMusic)
    return ec.successfull_execution

#function that remove a song from a playlist
def removeSongPlaylist(songDataBase, playlists):
    
    #gets chosen playlist
    playListName = input("Enter a playlist name: ")
    playlist = getPlaylist(playlists, playListName)
    
    numSongs = len(playlist)
    
    #if it's empyte the condition will return an error
    if numSongs <= 0 :
        return ec.playlist_not_found

    #user input of the playlist  
    print("You chose the playlist: ", playListName)    
    
    # music that the user wishes to remove in the playlist 
    songId = input("Enter index song to be removed from the playlist: ")
    
    #the input of the music have to be an integer as it is being taken from the column 
    # 'id_music'. if it´s not it will return an error.
    try:
        songId = int(songId)
        
    except:
        return ec.sintax
    
 
    if not ((songId == playlist["id_music"]).any()):
        return ec.song_not_found_playlist
     
    songRating = songDataBase['rating_global'][songId == songDataBase["id_music"]].item()
    #calculate the new average song rating and put with one decimal place.
    newAverageSongRating = af.subtractFromAverage(playlist["average_rating_musics"][0], numSongs, songRating)
    newAverageSongRating = round(newAverageSongRating, 1)
    
    playlists["average_rating_musics"][(playlists["id_playlist"] == playListName)] = newAverageSongRating
    
    #get boolean array of playlist matches
    playListMatch = playlists["id_playlist"] == playListName
    #get boolean array of music id matches
    idMatch = playlists["id_music"] == songId
    #get indexes of songs to remove from playlist
   
    removeIndex = playlists[playListMatch & idMatch].index
 
    #removes from playLists dataframe the specified song of the specified playlist
    playlists.drop(removeIndex, inplace = True)
       
    
    try:
        playlists.to_csv("data\\playlist.csv", index = False)  
    
    except:
        # error message from file errorCode
        return ec.file_open 
       
    print(getPlaylist(playlists, playListName).to_markdown(index=False))
    
    return ec.successfull_execution   
    

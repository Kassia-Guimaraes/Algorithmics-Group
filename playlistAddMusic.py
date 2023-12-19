import pandas as pd
import errorCodes as ec
import auxiliarFunctions as af

def addMusic(playlists, songDataBase):
    
    playListName = input("Enter a playlist name: ")
    
    playlist = af.getPlaylist(playlists, playListName)
    playlist.reset_index(inplace = True, drop = True)
    #checks if chosen playlist is in playlist file:
    numSongs = len(playlist)
    
    if numSongs <= 0 :
        return ec.playlist_not_found

      
    print("you chose the playlist: ", playListName)
   
    
    chooseMusic = input("Choose the music you want to add using the index contained in 'id_music': ")
      
    try:
        userIdMusic = int(chooseMusic)
        
    except:
        return ec.sintax

    
    if ((userIdMusic < 0) or ((userIdMusic == playlist['id_music']).any())): 
        return ec.playlist_duplicate
    
    if not((userIdMusic == songDataBase["id_music"]).any()):
        return ec.song_not_found
    
    songRating = songDataBase.loc[userIdMusic == songDataBase["id_music"]]['rating_global'].item()
    print(songRating)
    newAverageSongRating = af.addToAverage(playlist["average_rating_musics"][0], numSongs, songRating)
    newAverageSongRating = round(newAverageSongRating,1)
    
    playlists["average_rating_musics"][(playlists["id_playlist"] == playListName)] = newAverageSongRating
    
    newRow = [playListName, playlist["duration_playlist"][0], userIdMusic, playlist["rating_playlist"][0],
              newAverageSongRating, playlist["num_ratings"][0]]
   
    playlists.loc[len(playlists)] = newRow
    
    try: 
        playlists.to_csv("data\\playlist.csv", index = False)  
    
    except:
        return ec.file_open
    
    return ec.successfull_execution

    
   
   
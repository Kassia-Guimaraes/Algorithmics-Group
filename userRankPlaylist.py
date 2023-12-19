import pandas as pd
import errorCodes as ec
from auxiliarFunctions import getPlaylist, addToAverage

def addRank(playlists):
    
    playListName = input("Enter a playlist name: ")
    playlist = getPlaylist(playlists, playListName)
    #checks if chosen playlist is in playlist file:
    if len(playlist) <= 0 :
        return ec.playlist_not_found

    playlist.reset_index(inplace = True, drop = True)
    
    print("you chose the playlist: ", playListName)
    
    userRating = input("Rate the chosen playlist (from 1 to 5): ")
    
    try:
        userRating = float(userRating)
    except:
        return ec.sintax
    
    if not(userRating >= 0 and userRating <= 5): 
        return ec.invalid_rating
    
    #Get column with the playlist ranking
    playlistRatingColumn = playlist["rating_playlist"]
    
    #Get one element of the column -> ranking of the playlist
    currentRank = playlistRatingColumn[0]
    
    playlistNumberOfReviewColumn = playlist["num_ratings"]
    currentNumberOfReview = playlistNumberOfReviewColumn[0]
    
    newAverage = addToAverage(currentRank, currentNumberOfReview, userRating)
    newAverage = round(newAverage,1)
    
    playlists["rating_playlist"].mask(playlists["id_playlist"] == playListName,newAverage,inplace=True)
    playlists["num_ratings"].mask(playlists["id_playlist"] == playListName,currentNumberOfReview+1,inplace=True)
    
    try: 
        playlists.to_csv("data\\playlist.csv", index = False)  
    
    except:
        return ec.file_open
    
    return ec.successfull_execution
    
    
    
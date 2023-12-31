import pandas as pd
import errorCodes as ec
import math
from auxiliarFunctions import getPlaylist, addToAverage

#this function add the rank into a playlist
def addRank(playlists, chosenPlaylist):
    #the playlist will try to find the playlist the user want using the auxiliar function getPlaylist
    playlist = getPlaylist(playlists, chosenPlaylist)
    #checks if chosen playlist is in playlist file:
    if len(playlist) <= 0 :
        return ec.playlist_not_found

#reset the index from the playlist chosen is needed for the average formula
    playlist.reset_index(inplace = True, drop = True)

    print("you chose the playlist: ", chosenPlaylist)
    #user input
    userRating = input("Rate the chosen playlist (from 1 to 5): ")
    #the user input can be a decimal number, but if it's something different it will return a sintax error.
    try:
        userRating = float(userRating)
    except:
        return ec.sintax
    #the values accepted are between 1 and 5
    if not(userRating > 0 and userRating <= 5):
        return ec.invalid_rating

    #Get column with the playlist ranking
    playlistRatingColumn = playlist["rating_playlist"]

    #Get one element of the column -> ranking of the playlist
    currentRank = playlistRatingColumn[0]

    if math.isnan(currentRank):
        currentRank = 0

    #Get the number of ratings from the playlist chosen
    playlistNumberOfReviewColumn = playlist["num_ratings"]
    #This is the current number of ratings before the changes
    currentNumberOfReview = playlistNumberOfReviewColumn[0]

    #calculate the average with the information above.
    newAverage = addToAverage(currentRank, currentNumberOfReview, userRating)
    newAverage = round(newAverage, 1)

    # new average after the user rating
    playlists["rating_playlist"][playlists["id_playlist"] == chosenPlaylist] = newAverage
    # the number of ratings is the last one plus (+) 1 (the user that have already done the rating)
    playlists["num_ratings"][playlists["id_playlist"] == chosenPlaylist] = currentNumberOfReview+1

    #try save in the file, and if not return an error message.
    try:
        playlists.to_csv("data/playlist.csv", index = False)

    except:
        return ec.file_open

    #print the playlist after the changes
    playlist = getPlaylist(playlists, chosenPlaylist)
    print(playlist)

    #error code = 0
    return ec.successfull_execution

import pandas as pd
import errorCodes as ec
import auxiliarFunctions as af

# the specific function addMusic, add a music from the data base to a playlist
def addMusic(playlists, songDataBase):

    playlists_list = sorted(list(playlists['id_playlist'].drop_duplicates()))
    print("\033[1m AVAILABLE PLAYLISTS \033[0;0m")
    for id in playlists_list:
        print(" ", id)
    playListName = input(" Enter a playlist name => ")

    #checks if chosen playlist is in playlist file:
    playlist = af.getPlaylist(playlists, playListName)
    #reset the index from the playlist chosen.
    playlist.reset_index(inplace = True, drop = True)
    #variable takes the size of the playlist
    numSongs = len(playlist)
    #if it's empyte the condition will return an error
    if numSongs <= 0 :
        return ec.playlist_not_found

    #user input of the playlist
    print("you chose the playlist: ", playListName)

    #music that the user wishes to add in the playlist
    print(songDataBase)
    chooseMusic = input(" Add a song to " + playListName + "(pick an 'id_music')=> ")
    #the input of the music have to be an integer as it is being taking from the column 'id_music'. if it´s not it will return an error.
    try:
        userIdMusic = int(chooseMusic)

    except:
        return ec.sintax

    #the input must be a number that is present in the column íd_music' and that is not already in the playlist chosen, or it will return an error.
    if ((userIdMusic <= 0) or ((userIdMusic == playlist['id_music']).any())):
        return ec.playlist_duplicate

    if not((userIdMusic == songDataBase["id_music"]).any()):
        return ec.song_not_found

    #get the current global rating of that music.
    songRating = songDataBase['rating_global'][userIdMusic == songDataBase["id_music"]].item()

    #calculate the new rating of the song and put with one decimal place.
    newAverageSongRating = af.addToAverage(playlist["average_rating_musics"][0], numSongs, songRating)
    newAverageSongRating = round(newAverageSongRating, 1)

    playlists["average_rating_musics"][(playlists["id_playlist"] == playListName)] = newAverageSongRating

    #create new row with the update of the informations of the average.
    newRow = [playListName, playlist["duration_playlist"][0], userIdMusic, playlist["rating_playlist"][0],
              newAverageSongRating, playlist["num_ratings"][0]]

    #insert in the dataframe playlists the new row.
    playlists.loc[len(playlists)] = newRow
    print("these be the playlists\n",playlists)
    #save the file with the new information, if not, return an error.
    try:
        playlists.to_csv("data/playlist.csv", index = False)
        print(playlists)

    except:
        return ec.file_open

    return ec.successfull_execution
playlist_df = pd.read_csv('data/playlist.csv')
tableMusic_df = pd.read_csv('data/tableMusic.csv')
addMusic(playlist_df,tableMusic_df)

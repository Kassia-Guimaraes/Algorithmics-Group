import pandas as pd
import errorCodes as ec
import auxiliarFunctions as af

# menu to pick a playlist from a selection
def pickPlaylist(playlist_csv):
    playlists_list = sorted(list(map(str.lower, playlist_csv['id_playlist'].drop_duplicates())))
    playListName = ""
    input_message = " enter a playlist name => "
    while playListName not in playlists_list:
        print("\033[1m AVAILABLE PLAYLISTS \033[0;0m")
        for id in playlists_list:
            print(" ", id)
        playListName = input(input_message).lower()
        input_message = " \033[1m WARNING: \033[0;0minvalid input\n enter a playlist name => "
    return playListName

# the specific function addMusic, add a music from the data base to a playlist
def addMusic(playlists, songDataBase, playlist):

    playListName = playlist

    #checks if chosen playlist is in playlist file:
    playlist = af.getPlaylist(playlists, playListName)
    #reset the index from the playlist chosen.
    playlist.reset_index(inplace = True, drop = True)
    #variable takes the size of the playlist
    numSongs = len(playlist)
    #if it's empty the condition will return an error
    if numSongs <= 0 :
        return ec.playlist_not_found

    #user input of the playlist
    print("you chose the playlist: ", playListName)

    #music that the user wishes to add in the playlist
    print(songDataBase.to_markdown(index=False))
    chooseMusic = input(" Enter the id of the song to add to " + playListName + " (0 to abort) => ")
    #the input of the music have to be an integer as it is being taking from the column 'id_music'. if it´s not it will return an error.
    try:
        userIdMusic = int(chooseMusic)

    except:
        print("\033[1m WARNING: \033[0;0mInvalid input")
        return

    #the input must be a number that is present in the column íd_music' and that is not already in the playlist chosen, or it will return an error.
    if ((userIdMusic < 0) or ((userIdMusic == playlist['id_music']).any())):
        print("\033[1m WARNING: \033[0;0mSong already in playlist")
        return ec.playlist_duplicate

    if userIdMusic == 0:
        return

    if not((userIdMusic == songDataBase["id_music"]).any()):
        print("\033[1m WARNING: \033[0;0mSong not found")
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
    print("these are the playlists\n",playlists)
    #save the file with the new information, if not, return an error.
    try:
        playlists.to_csv("data/playlist.csv", index = False)
        playlist = af.getPlaylist(playlists, playListName)
        print(playlist.to_markdown(index=False))
        print("\033[1m SUCCESS: \033[0;0mSong added to playlist ", playListName)
    except:
        return ec.file_open

    return ec.successfull_execution

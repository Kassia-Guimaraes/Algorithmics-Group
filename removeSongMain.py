import pandas as pd
from auxiliarFunctions import getPlaylist
from auxiliarFunctions import getPlaylist
import errorCodes as ec


### .PY file to test removeSong.py functions ###

def removeSongDataBaseMenu():
    #Reads TableMusic and Playlist CSVs into dataframe variables
    tableMusic_df = pd.read_csv('data/tableMusic.csv')
    playlist_df = pd.read_csv('data/playlist.csv')

    #Shows all the available songs
    print(" These are the songs in the data base: ")
    print(tableMusic_df)

    #Testing function that removes a song from the entire database (tableMusic and playlists)
    songId = input(" Enter id of the song you wish to remove (0 to abort) => ")
    if songId == "0":
        return
    try:
        removeSongDataBase(tableMusic_df, playlist_df, int(songId))
    except:
        print("\033[1m WARNING: \033[0;0minvalid input")
        removeSongDataBaseMenu()
    print(tableMusic_df)
    return tableMusic_df


# function responsible for remove a song for the database and for the playlist in the same time.
def removeSongDataBase(tableMusic, playlists, id):
    import auxiliarFunctions as af
    #the condition sees if the index is in the dataframe tableMusic
    if id in tableMusic["id_music"].values:

        playlistsToUpdate = playlists["id_playlist"][playlists["id_music"]==id]

        for playListName in playlistsToUpdate:

            playlist = getPlaylist(playlists, playListName)
            playlist.reset_index(inplace = True, drop = True)
            numSongs = len(playlist)

            songRating = tableMusic['rating_global'][id == tableMusic["id_music"]].item()
            #calculate the new average song rating and put with one decimal place.
            newAverageSongRating = af.subtractFromAverage(playlist["average_rating_musics"][0], numSongs, songRating)
            newAverageSongRating = round(newAverageSongRating, 1)

            playlists["average_rating_musics"][(playlists["id_playlist"] == playListName)] = newAverageSongRating

       # .drop is the pandas function to remove anything; and get boolean array of music id matches
        tableMusic.drop(tableMusic[tableMusic["id_music"] == id].index,inplace=True)
        playlists.drop(playlists[playlists["id_music"] == id].index, inplace = True)
       #tableMusic and playlists are the dataframes where the music is going to be removed.
        tableMusic.to_csv("data/tableMusic.csv", index=False)
        playlists.to_csv("data/playlist.csv", index=False)
        print("\033[1m SUCCESS: \033[0;0mSong removed from database ")
    else:
        print("\033[1m WARNING: \033[0;0mThis song is not in our system. Please chose a valid option => ")


def removeSongPlaylist(tableMusic, playlists, playListName):
    import auxiliarFunctions as af
    print(getPlaylist(playlists, playListName))
    songId = ""
    while songId == "":
        try:
            songId = int(input(" Enter id of song to be removed from " + playListName + " (0 to return) => "))
        except:
            # if songId == "0":
            #     return
            # else:
            print("\033[1m WARNING: \033[0;0mInvalid input.")
    #gets chosen playlist
    playlist = getPlaylist(playlists,playListName)
    numSongs = len(playlist)

    #checks if chosen id is in playlist
    print("playlist[id_music].values ", playlist["id_music"].values)
    if int(songId) in map(int, playlist["id_music"].values):
    # if (" " + str(songId) + " ") in str(playlist["id_music"].values):


        songRating = tableMusic['rating_global'][(songId == tableMusic["id_music"])].item()
        #calculate the new average song rating and put with one decimal place.
        newAverageSongRating = af.subtractFromAverage(list(playlist["average_rating_musics"])[0], numSongs, songRating)
        newAverageSongRating = round(newAverageSongRating, 1)

        playlists["average_rating_musics"][(playlists["id_playlist"] == playListName)] = newAverageSongRating


        #get boolean array of playlist matches
        playListMatch = playlists["id_playlist"] == playListName
        #get boolean array of music id matches
        idMatch = playlists["id_music"] == int(songId)
        #get indexes of songs to remove from playlist
        removeIndex = playlists[playListMatch & idMatch].index
        #removes from playLists dataframe the specified song of the specified playlist
        playlists.drop(removeIndex, inplace = True)
        print("\033[1m SUCCESS: \033[0;0mSong removed from playlist ", playListName)
        try:
            playlists.to_csv("data/playlist.csv", index = False)
            print(getPlaylist(playlists, playListName))

        #error message from file errorCode
        except:
            return ec.file_open
    elif songId == 0:
        return
    else :
        print("\033[1m WARNING: \033[0;0mInvalid input.")
        removeSongPlaylist(tableMusic, playlists, playListName)

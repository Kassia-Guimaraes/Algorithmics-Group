import pandas as pd 
from errorCodes import *
from auxiliarFunctions import getPlaylist
import auxiliarFunctions as af
import errorCodes as ec

# Read the playlists and music tables
playlist_df = pd.read_csv('data/playlist.csv')
tableMusic_df = pd.read_csv('data/tableMusic.csv')

def aviableUser():
    rating_min_user_df = tableMusic_df[(tableMusic_df['rating_user'] < 4)] #songs with user aviable < 4
    #print(f"rating_min_user_df:\n{rating_min_user_df}")
    id_songs_to_remove = rating_min_user_df['id_music'].tolist() #id songs list with user aviable < 4
    #print(f"\nid_songs_to_remove: {id_songs_to_remove}")

    return id_songs_to_remove

def playlistUpdate(): #update all playlists, excluding songs with user aviable < 4
    id_songs_to_remove = aviableUser()
    print(f"\nId songs to remove: {id_songs_to_remove}")
    list_playlists = playlist_df['id_playlist'].drop_duplicates().tolist() #list with playlists name 

    for playlist_name in list_playlists: #id songs per playlist

        per_playlist_df = getPlaylist(playlist_df, playlist_name)
        id_songs_per_playlist = per_playlist_df['id_music'].tolist() #verify id songs list in specify playlist 
        #print(f"id_songs_per_playlist {playlist_name}: {id_songs_per_playlist}")

        for songId in id_songs_to_remove: #get id's to remove
            if int(songId) in map(int, id_songs_per_playlist):
                songRating = tableMusic_df['rating_global'][(songId == tableMusic_df["id_music"])].item() #calculate the new average song rating and put with one decimal place.
                newAverageSongRating = af.subtractFromAverage(list(per_playlist_df["average_rating_musics"])[0], len(id_songs_per_playlist), songRating)
                newAverageSongRating = round(newAverageSongRating, 1)

                newAverageSongRating = playlist_df["average_rating_musics"][(playlist_df["id_playlist"] == playlist_name)] 

                #get boolean array of playlist matches
                playListMatch = playlist_df["id_playlist"] == playlist_name
                #get boolean array of music id matches
                idMatch = playlist_df["id_music"] == int(songId)
                #get indexes of songs to remove from playlist
                removeIndex = playlist_df[playListMatch & idMatch].index
                #removes from playlist_df dataframe the specified song of the specified playlist
                playlist_df.drop(removeIndex, inplace = True)
                title_per_id = (tableMusic_df[tableMusic_df['id_music']==songId]).iloc[0] #for print all songs titles 
                title_music = title_per_id['title']
                print(f"\033[1m SUCCESS: \033[0;0mSong {title_music} removed from playlist ", playlist_name)
                try:
                    playlist_df.to_csv("data/playlist.csv", index = False)
                    print(getPlaylist(playlist_df, playlist_name))

                #error message from file errorCode
                except:
                    return ec.file_open
            else: 
                continue
    return

def autoPlaylistUpdate():
    playlist_prefix = 'play_auto_' #specif playlist name
    # Filter playlists by prefix name
    filtered_playlist_df = playlist_df[playlist_df['id_playlist'].str.startswith(playlist_prefix)]
    id_songs_to_remove = aviableUser()

    # Check if there are playlists with the playlist prefix name
    if not filtered_playlist_df.empty:
        list_playlists = filtered_playlist_df['id_playlist'].drop_duplicates().tolist()

        for playlist_name in list_playlists: #id songs per playlist

            per_playlist_df = getPlaylist(filtered_playlist_df, playlist_name)
            id_songs_per_playlist = per_playlist_df['id_music'].tolist() #verify id songs list in specify playlist 
            print(f"id_songs_per_playlist {playlist_name}: {id_songs_per_playlist}")

            for songId in id_songs_to_remove: #get id's to remove
                if int(songId) in map(int, id_songs_per_playlist):
                    songRating = tableMusic_df['rating_global'][(songId == tableMusic_df["id_music"])].item() #calculate the new average song rating and put with one decimal place.
                    newAverageSongRating = af.subtractFromAverage(list(per_playlist_df["average_rating_musics"])[0], len(id_songs_per_playlist), songRating)
                    newAverageSongRating = round(newAverageSongRating, 1)

                    newAverageSongRating = playlist_df["average_rating_musics"][(playlist_df["id_playlist"] == playlist_name)] 

                    #get boolean array of playlist matches
                    playListMatch = playlist_df["id_playlist"] == playlist_name
                    #get boolean array of music id matches
                    idMatch = playlist_df["id_music"] == int(songId)
                    #get indexes of songs to remove from playlist
                    removeIndex = playlist_df[playListMatch & idMatch].index
                    #removes from playlist_df dataframe the specified song of the specified playlist
                    playlist_df.drop(removeIndex, inplace = True)
                    print("\033[1m SUCCESS: \033[0;0mSong removed from playlist ", playlist_name)
                    try:
                        playlist_df.to_csv("data/playlist.csv", index = False)
                        print(getPlaylist(playlist_df, playlist_name))

                    #error message from file errorCode
                    except:
                        return ec.file_open
                else: 
                    continue
    else: # playlist not found 
        print(messages[playlist_not_found])

    return

playlistUpdate()
# import the time module
import time
import pandas as pd
import updatePlaylist
import musicReview

def songPlaybackMenu(table):
    # Solicitar ao usuário o título  da música
    songs_list = sorted(list(table['title'].drop_duplicates()))
    print("\033[1m AVAILABLE SONGS \033[0;0m")
    for title in songs_list:
        print(" ", title)

    song_input = input(" What song do you want to play => ").lower()
    playback(table.loc[table['title'].str.lower() == song_input])

# # define the countdown func.
def playback(song):

    print("Now playing: ",list(song['title'])[0])
    duration = int(song['duration'])
    while duration:
        mins, secs = divmod(duration, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        duration -= 1
    musicReview.song_rating(list(song['title'])[0])
    updatePlaylist.autoPlaylistUpdate()

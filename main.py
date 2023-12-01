import pandas as pd
import removeSong

tableMusic = pd.read_csv('tableMusic.csv')
print("These are the available songs: ")
print(tableMusic)

while True:
    index_song = input("Enter index song: ")
    index_song = int(index_song)
    index_song = index_song-1
    removeSong.removeSong(tableMusic, index_song)
    print("The song of index "+str(index_song+1)+". These are the new available songs: ")
    print(tableMusic)
 

   
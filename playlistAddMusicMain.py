import pandas as pd
from playlistAddMusic import addMusic
import errorCodes as ec

playlist_df = pd.read_csv('data/playlist.csv')
tableMusic_df = pd.read_csv('data/tableMusic.csv')

print(playlist_df)

errorCode = addMusic(playlist_df, tableMusic_df)

print(ec.messages[errorCode])

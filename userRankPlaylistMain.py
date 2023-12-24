import pandas as pd
from userRankPlaylist import addRank
import errorCodes as ec

playlist_df = pd.read_csv('data/playlist.csv')
print(playlist_df)

errorCode = addRank(playlist_df)

print(ec.messages[errorCode])
    
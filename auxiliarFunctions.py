# get an especific playlist from a playlist_df
def getPlaylist(playlists, playListName):
    return playlists[playlists["id_playlist"] == playListName]

# formula to calculate an average
def addToAverage(average, size, value):
    return (size * average + value) / (size + 1)

def subtractFromAverage(average, size, value):
    return ((average * size) - value) / (size - 1)
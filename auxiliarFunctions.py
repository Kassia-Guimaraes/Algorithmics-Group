# get an especific playlist from a playlist_df
def getPlaylist(playlists, playlistName):
    return playlists[playlists["id_playlist"] == playlistName]
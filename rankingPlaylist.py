import pandas as pd

# Carregar o DataFrame da tabela de playlists
playlist_df = pd.read_csv('data/playlist.csv')

# Contar a prevalência de playlists com base nas avaliações
rankingPlaylist_df = playlist_df.groupby('id_playlist')['rating_playlist'].mean().reset_index()
rankingPlaylist_df.columns = ['id_playlist', 'Playlist rating']

# Classificar as playlists pela avaliação média em ordem descendente
rankingPlaylist_df = rankingPlaylist_df.sort_values(by='Playlist rating', ascending=False)

# Mostrar o ranking das playlists
print("Playlist ranking:")
print(rankingPlaylist_df.head())


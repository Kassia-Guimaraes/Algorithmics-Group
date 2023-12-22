import pandas as pd

def songRecurrence():
    # Carregar dados do arquivo CSV de playlists
    playlist_df = pd.read_csv('data/playlist.csv')

    # Carregar dados do arquivo CSV de músicas
    tableMusic_df = pd.read_csv('data/tableMusic.csv', index_col='id_music')

    # Realizar a junção (merge) entre os DataFrames usando o ID da música
    mergedID_df = pd.merge(playlist_df, tableMusic_df, left_on='id_music', right_index=True)

    # Contar a presença de músicas nas playlists
    count_music_df = mergedID_df['title'].value_counts().reset_index()
    count_music_df.columns = ['title', 'Prevalence on playlists']

    # Ordenar as músicas por presença
    count_music_df = count_music_df.sort_values(by='Prevalence on playlists', ascending=False)

    # Exibir as músicas mais frequentes
    print(count_music_df.head())

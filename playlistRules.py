import pandas as pd

tm = pd.read_csv("./tableMusic.csv", sep=(","))

def create_play(name_playlist):
    while True:
        music_rating_max = tm[(tm['rating_global'] > 4)].sample(10) #10 songs rt > 4
        music_rating_min = tm[(tm['rating_global'] <= 4)].sample(5) #5 songs rt <= 4

        playlist = pd.concat([music_rating_max, music_rating_min])
        duration_total = playlist['duration'].sum() #duração total da playlist

        if duration_total <= 3600: #duração total deve ser <= 60 minutos, 3600 segundos
            break

    playlist['id_playlist'] = name_playlist
    return playlist #retorna o nome da playlist 

created_playlists = []  # guarda todas as playlists criadas

# Main
count_playlist = 0
while True:
    flag = input("Deseja criar uma nova playlist automática? (S/N) ").strip().lower()

    if flag != 's':
        break

    count_playlist += 1
    name_playlist = f'play_auto_{count_playlist}' #salva como play_auto e o número da playlist

    play_auto = create_play(name_playlist)
    created_playlists.append(play_auto)

    count_style = play_auto['style'].value_counts()

    # Adiciona a coluna 'duration_playlist' ao DataFrame
    play_auto['duration_playlist'] = play_auto['duration'].sum()

    print(f"Playlist '{name_playlist}' criada com sucesso!\nTotal playlist duration: {play_auto['duration_playlist']}")
    print(play_auto[['title', 'rating_global', 'style', 'year']])
    print("\nSongs per style:")
    print(count_style)

# Cria um DataFrame contendo todas as playlists criadas
created_playlists_df = pd.concat(created_playlists, ignore_index=True)

# Imprime o DataFrame com todas as playlists criadas
print("\nTodas as Playlists Criadas:")
print(created_playlists_df[['id_playlist', 'id_music', 'title', 'style', 'type', 'duration', 'duration_playlist']])

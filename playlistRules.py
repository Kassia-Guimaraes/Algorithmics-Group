import pandas as pd
import numpy as np

tm = pd.read_csv("./tableMusic.csv", sep=(","), index_col='id_music')

def crt_play():
    while True:
        msc_rt_max = tm[(tm['rating_global'] > 4)].sample(10)  # 10 músicas com rating > 4 
        msc_rt_min = tm[(tm['rating_global'] <= 4)].sample(5)  # 5 músicas com rating <= 4

        playlist = pd.concat([msc_rt_max, msc_rt_min])  # mesclando músicas
        drt_total = playlist['duration'].sum() #calculo da soma das durações

        if drt_total <= 3600:
            break  # sair do loop se a duração total for menor ou igual a 3600

    return playlist  # retornando o DataFrame da playlist

play_auto = crt_play() #pega a playlist criada
count_style = play_auto['style'].value_counts() # contando músicas por estilo

print("Total playlist duration:", play_auto['duration'].sum())
print("Playlist:")
print(play_auto[['title', 'rating_global', 'style', 'year']])
print("\nSongs per style:")
print(count_style)
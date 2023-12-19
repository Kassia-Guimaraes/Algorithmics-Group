#teste

import pandas as pd


playlist = pd.read_csv('data\\playlist.csv')

print(playlist["id_playlist"]=="best_rock")
teste = playlist["average_rating_musics"][(playlist["id_playlist"]=="best_rock")]

print(teste)
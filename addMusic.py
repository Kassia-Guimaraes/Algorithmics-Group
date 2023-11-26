import pandas as pd
import numpy as np

tableMusic = pd.read_csv("./tableMusic.csv", sep=(","), index_col='id_music')
#style  type    title   songwritter year    artist  rating_global   rating_user duration

title_music = str(input("Digite o nome da música que deseja adicionar: "))
title_music = title_music.title()

style_music = input("Qual o estilo da música? ")
style_music = style_music.title()

type_music = input("Qual a tipologia da música? ")		
type_music = type_music.title()

songwritter_music = input("Qual o nome do autor da música? ")	
songwritter_music = songwritter_music.title()

year_music = int(input("Qual o ano de lançamento da música? "))

artist_music = input("Quem canta a música? ")	
artist_music = artist_music.title()

rating_global_music = int(input("Qual a avaliação global da música? "))	
rating_user_music = int(input("Qual a avaliação que você dá para a música? "))	

duration_music = input("Qual a duração da música? ")
duration_music = duration_music.split(":")
minutes = int(duration_music[0])
seconds = int(duration_music[1])
duration_music = (minutes*60)+seconds

new_music = {'style': style_music, 'type': type_music, 'title': title_music, 'songwritter': songwritter_music, 'year': year_music, 'artist': artist_music, 'rating_global': rating_global_music,  'rating_user':rating_user_music, 'duration': duration_music}

tableMusic = tableMusic.append(new_music, ignore_index=True)
print(tableMusic)
print("teste")
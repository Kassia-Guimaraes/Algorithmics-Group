import pandas as pd
import numpy as np

tm = pd.read_csv("./tableMusic.csv", sep=(","), index_col='id_music')
#style  type    title   songwritter year    artist  rating_global   rating_user duration

title_music = str(input("What's the title of the song? "))
title_music = title_music.title()

style_music = input("What's the style? ")
style_music = style_music.title()

type_music = input("What's the typology? ")
type_music = type_music.title()

songwritter_music = input("What's the songwritter name? ")	
songwritter_music = songwritter_music.title()

year_music = int(input("what year was the song released? "))

artist_music = input("Who sings the music? ")	
artist_music = artist_music.title()

rating_global_music = int(input("What's the global rating of the song? "))	
rating_user_music = int(input("What's your rating of the song? "))	

duration_music = input("What's the duration of the song? ")
duration_music = duration_music.split(":")
minutes = int(duration_music[0])
seconds = int(duration_music[1])
duration_music = (minutes*60)+seconds

new_music = {'style': style_music, 'type': type_music, 'title': title_music, 'songwritter': songwritter_music, 'year': year_music, 'artist': artist_music, 'rating_global': rating_global_music,  'rating_user':rating_user_music, 'duration': duration_music}

tm = tm.append(new_music, ignore_index=True)
print(tm)
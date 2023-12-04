import pandas as pd
import numpy as np

tableMusic_df = pd.read_csv("data/tableMusic.csv", sep=(","))

def addMusic():
    title_new_music = str(input("What's the title of the song? ")).title()
    style_new_music = input("What's the style? ").title()
    type_new_music = input("What's the typology? ").title()
    songwriter_new_music = input("What's the songwriter name? ").title()
    year_new_music = int(input("what year was the song released? "))
    artist_new_music = input("Who sings the songs? ").title()
    rating_global_new_music = int(input("What's the global rating of the song? "))
    rating_user_new_music = int(input("What's your rating of the song? "))	

    duration_new_music = input("What's the duration of the song? ")
    duration_new_music = duration_new_music.split(":")
    minutes = int(duration_new_music[0])
    seconds = int(duration_new_music[1])
    duration_new_music = (minutes*60)+seconds

    id_new_music = tableMusic_df.index.max() + 1 #id_music vai de 1 até x o index do pandas vai de 0 até x -1
    id_new_music = int(id_new_music)

    new_music_line = {'style': style_new_music, 'type': type_new_music, 'title': title_new_music, 'songwriter': songwriter_new_music, 'year': year_new_music, 'artist': artist_new_music, 'rating_global': rating_global_new_music,  'rating_user':rating_user_new_music, 'duration': duration_new_music, 'id_music' : id_new_music}

    newMusic = tableMusic_df.append(new_music_line, ignore_index=True)

    add_to_table = addMusic()
    newTable = add_to_table.set_index('id_music') #exportar com o index na coluna 'id_music'

    print(newTable) 
    #newTable.to_csv('./tableMusic.csv')
    
    return newTable #tabela já adicionada

addMusic()
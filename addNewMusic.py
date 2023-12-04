import pandas as pd
import numpy as np

tm = pd.read_csv("./tableMusic.csv", sep=(","))

def addMusic():
    ttl_new_msc = str(input("What's the title of the song? "))
    ttl_new_msc = ttl_new_msc.title()

    stl_new_msc = input("What's the style? ")
    stl_new_msc = stl_new_msc.title()

    tp_new_msc = input("What's the typology? ")
    tp_new_msc = tp_new_msc.title()

    songwritter_new_msc = input("What's the songwritter name? ")	
    songwritter_new_msc = songwritter_new_msc.title()

    year_new_msc = int(input("what year was the song released? "))

    art_new_msc = input("Who sings the songs? ")	
    art_new_msc = art_new_msc.title()

    rt_global_new_msc = int(input("What's the global rating of the song? "))	
    rt_user_new_msc = int(input("What's your rating of the song? "))	

    drt_new_msc = input("What's the duration of the song? ")
    drt_new_msc = drt_new_msc.split(":")
    minutes = int(drt_new_msc[0])
    seconds = int(drt_new_msc[1])
    drt_new_msc = (minutes*60)+seconds

    id_new_music = tm.index.max() + 1 #id_music vai de 1 até x o index do pandas vai de 0 até x -1
    id_new_music = int(id_new_music)

    new_msc_line = {'style': stl_new_msc, 'type': tp_new_msc, 'title': ttl_new_msc, 'songwritter': songwritter_new_msc, 'year': year_new_msc, 'artist': art_new_msc, 'rating_global': rt_global_new_msc,  'rating_user':rt_user_new_msc, 'duration': drt_new_msc, 'id_music' : id_new_music}

    newMusic = tm.append(new_msc_line, ignore_index=True)

    add_to_table = addMusic()
    newTable = add_to_table.set_index('id_music') #exportar com o index na coluna 'id_music'

    print(newTable) 
    #newTable.to_csv('./tableMusic.csv')
    
    return newTable #tabela já adicionada

addMusic()
import pandas as pd
import numpy as np
from addStyle import *

def checkInput(query, warning):
    variable = ""
    while variable == "":
        try:
            variable = int(input(query))
        except:
            print("\033[1m WARNING: \033[0;0m" + warning)
            continue
        return variable

def song_style(theFilter):
    for i in range(0, len(theFilter), 1):
        print("\033[1m", str(i+1), "\033[0;0m ", str(theFilter[i]))
    # print("\033[1m", "0", "\033[0;0m ", "(next)")
    print("\033[1m", 0, "\033[0;0m ", "(add new style)")
    choice = str(checkInput(" What's the style? (pick number) => ", " please enter a number"))
    if choice == "0":
        new_style = addStyle()
        if new_style == "0":
            song_style(theFilter)
        else:
            return new_style
    else:
        return (theFilter[int(choice)-1])

tableMusic_df = pd.read_csv("data/tableMusic.csv", sep=(","))

def addMusic():
    title_new_music = str(input(" What's the title of the song? ")).title()

    styles_list = refresh_styles_list()
    style_new_music = song_style(styles_list)

    type_new_music = input(" What's the typology? ").title()
    songwriter_new_music = input(" What's the songwriter name? ").title()
    year_new_music = checkInput(" what year was the song released? ", "please enter a number")
    artist_new_music = input(" Who sings the songs? ").title()
    rating_global_new_music = checkInput(" What's the global rating of the song? ", "please enter a number")
    rating_user_new_music = checkInput(" What's your rating of the song? ", "please enter a number")

    duration_new_music = ""
    while duration_new_music == "":
        try:
            duration_new_music = input(" What's the duration of the song(min:sec)? ").split(":")
            minutes = int(duration_new_music[0])
            seconds = int(duration_new_music[1])
        except:
            print("\033[1m WARNING: \033[0;0mplease use the format min:sec")
            duration_new_music = ""
            continue
        duration_new_music = (minutes*60)+seconds
    id_new_music = tableMusic_df.index.max() + 2  # id_music goes from 1 to x, the pandas index goes from 0 to x -1
    id_new_music = int(id_new_music)

    new_music_line_dict = {'style': style_new_music, 'type': type_new_music, 'title': title_new_music,'songwriter': songwriter_new_music, 'year': year_new_music, 'artist': artist_new_music,'rating_global': rating_global_new_music, 'rating_user': rating_user_new_music, 'duration': duration_new_music, 'id_music': id_new_music}

    # Convert the dictionary to a DataFrame
    new_music_line = pd.DataFrame([new_music_line_dict], index=[id_new_music])  # Explicitly provide the index

    # Replace append() with concat()
    newMusic = pd.concat([tableMusic_df, new_music_line], ignore_index=False)

    print(newMusic[['id_music', 'title', 'artist','style','duration']].to_markdown(index=False))
    # newTable.to_csv('./tableMusic.csv')  # Uncomment to save the updated DataFrame

    return newMusic  # Updated DataFrame

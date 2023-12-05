import pandas as pd
import os.path

# pd.set_option('display.max_columns', 1000)

filtered_songs = pd.read_csv('data/tableMusic.csv')

filter_list = ["year", "artist", "style", "type"]

# create list of all elements of given category used to create menu
def category_list(category):
    try:
        print(filtered_songs)
        # print(filtered_songs.loc[:, category])
        return (list(filtered_songs.loc[:, category].drop_duplicates()))
    except:
        print("erro")
        return

# retrieve the songs with a given filter
def filterSongs(theFilter):
    picked_filter = 0
    filtered_songs = pd.read_csv('data/tableMusic.csv')
    while picked_filter == 0:
        try:
            filtered_songs.set_index(theFilter, inplace = True)
            return filtered_songs.loc[[filter[int(input("=> "))-1]]]
        except:
            picked_filter = 0
            print("Invalid choice.\n")
            filter_menu(theFilter)

# output menu for given filter
def filter_menu(a):
    print("\033[1m" + "FILTER " + a.upper() + "\n(press a number)" + "\033[0;0m")
    for i in range(0, len(filter), 1):
        print("\033[1m", str(i+1), "\033[0;0m ", str(filter[i]))
    return len(filter)

for i in range(0, len(filter_list), 1):
    try:
        filter = category_list(filter_list[i])
        filter_menu(filter_list[i])
        filtered_songs = filterSongs(filter_list[i])
    except Exception as e:
        print(e)

print(filtered_songs)

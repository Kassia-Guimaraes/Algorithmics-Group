from numpy import empty
import pandas as pd
import os.path

# pd.set_option('display.max_columns', 1000)

filtered_songs = pd.read_csv('data/tableMusic.csv')

filter_list = ["style", "songwriter", "type", "artist"]

# create list of all elements of given category used to create menu
def category_list(category):
    try:
        # print(filtered_songs.loc[:, category])
        return (list(filtered_songs.loc[:, category].astype(str).drop_duplicates()))
    except:
        return

# retrieve the songs with a given filter
def filterSongs(theFilter):
    picked_filter = 0
    while picked_filter == 0:
        try:
            picked_filter = filter[int(input())-1]
            print("The " + theFilter + " picked was " + picked_filter + "\n")
            filtered_songs.set_index(theFilter, inplace = True)
            return filtered_songs.loc[picked_filter]
        except Exception as e:
            picked_filter = 0
            print("Invalid choice.\n")
            print(e)
            filter_menu(theFilter)

# output menu for given filter
def filter_menu(a):
    print("\033[1m" + "FILTER " + a.upper() + "\n(press a number)" + "\033[0;0m")
    for i in range(0, len(filter), 1):
        print("\033[1m" + str(i+1) + "\033[0;0m " + str(filter[i]))
    return len(filter)

# def applyFilters(array):
for i in range(0, len(filter_list), 1):
    try:
        filter = category_list(filter_list[i])
        print(filter)
        filter_menu(filter_list[i])
        filtered_songs = filterSongs(filter_list[i])

        # if len(filter) == 1:
        #     print("continues")
        #     continue
        # else:
        #     filter_menu(filter_list[i])
        #     filtered_songs = filterSongs(filter_list[i])
    except Exception as e:
        print("Exception")

print(filtered_songs)

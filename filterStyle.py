import pandas as pd
import os.path
import addStyle

def category_list(category):
    if category == "style":
        return addStyle.refresh_styles_list()
    else:
        tm = pd.read_csv('tableMusic.csv')
        return (list(tm.loc[:, category].drop_duplicates()))

# standard message to be reused for other filtering messages
def filter_menu(a):
    print(a + " - press a number:")
    for i in range(0, len(filter), 1):
        print(str(i+1) + " " + str(filter[i]))

# retrieves the songs with a given filter
def filterSongs(theFilter):
    picked_filter = 0
    while picked_filter == 0:
        try:
            # picked_filter = filter[int(input())-1]
            # print("The " + theFilter + " picked was " + str(picked_filter) + "\n")
            # tm = pd.read_csv('tableMusic.csv')
            # tm.set_index(theFilter, inplace = True)
            # return tm.loc[picked_filter]
            if theFilter == "style":
                picked_filter = filter[int(input())-1]
                print("The " + theFilter + " picked was " + str(picked_filter) + "\n")
                tm = pd.read_csv('tableMusic.csv')
                tm.set_index(theFilter, inplace = True)
                return tm.loc[picked_filter]
            else:
                picked_filter = filter[int(input())-1]
                print("The " + theFilter + " picked was " + str(picked_filter) + "\n")
                # filtered_songs.set_index(theFilter, inplace = True)
                # return filtered_songs.loc[picked_filter]
                return filtered_songs
        except:
            picked_filter = 0
            print("Invalid choice.\n")
            filter_menu(theFilter)

# define styles with addStyle.py function
filter = category_list("style")

filter_menu("Style")

filtered_songs = filterSongs("style")

filter = category_list("artist")

filter_menu("Artist")

filtered_songs = filterSongs("artist")

print(filtered_songs)

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
def pick_message(a):
    print(a + " - press a number:")
    for i in range(0, len(filter), 1):
        print(str(i+1) + " " + str(filter[i]))

def filterSongs(theFilter):
    picked_filter = 0
    while picked_filter == 0:
        try:
            picked_filter = filter[int(input())-1]
            print("The " + theFilter + " picked was " + str(picked_filter) + "\n")
            tm = pd.read_csv('tableMusic.csv')
            tm.set_index(theFilter, inplace = True)
            return tm.loc[picked_filter]
        except:
            picked_filter = 0
            print("Invalid choice.\n")
            pick_message("Style")

# define styles with addStyle.py function
filter = category_list("style")

pick_message("Style")

filtered_songs = filterSongs("style")

print(filtered_songs)

import pandas as pd
import os.path

pd.set_option('display.max_columns', 1000)

filter_list = ["year", "artist", "style", "type"]

# create list of all elements of given category used to create menu
def category_list(category, table):
    try:
        return (list(table.loc[:, category].drop_duplicates()))
    except:
        print("erro")
        return

# retrieve the songs with a given filter
def filterSongs(theFilter, table, filterArray):
    picked_filter = 0
    while picked_filter == 0:
        try:
            table.set_index(theFilter, inplace = True)
            return table.loc[[filterArray[int(input(" => "))-1]]]
        except:
            picked_filter = 0
            print("Invalid choice.\n")
            filter_menu(theFilter, filterArray)

# output menu for given filter
def filter_menu(theArray, theFilter):
    print("\n" + "\033[1m" + "FILTER " + theArray.upper() + "\n(press a number)" + "\033[0;0m")
    for i in range(0, len(theFilter), 1):
        print("\033[1m", str(i+1), "\033[0;0m ", str(theFilter[i]))
    return len(theFilter)

def applyFilters(filtersList, table):
    filtered_songs = pd.read_csv(table)
    for i in range(0, len(filtersList), 1):
        try:
            filter = category_list(filtersList[i], filtered_songs)
            filter_menu(filtersList[i], filter)
            filtered_songs = filterSongs(filtersList[i], filtered_songs, filter)
        except Exception as e:
            print(e)
    print(filtered_songs)

applyFilters(['artist', 'year', 'songwriter', 'type'], 'data/tableMusic.csv')

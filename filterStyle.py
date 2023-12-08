import pandas as pd
import os.path

# pd.set_option('display.max_columns', 1000)

# create list of all elements of given category used to create menu
def category_list(category, table):
    try:
        return (list(table.loc[:, category].drop_duplicates()))
    except:
        print("erro")
        return

# retrieve the songs with a given filter
def filterSongs(theFilter, table, filterArray):
    selection = 0
    selectionArray = []
    filter_menu(theFilter, filterArray)

    # present the same menu while input is invalid
    while selection == 0:

        # select multiple elements of a column
        while(selection in range(len(filterArray))):
            try:
                selection = int(input("\033[5m => "))-1
                if selection in range(len(filterArray)):
                    selectionArray.append(filterArray[selection])
                    selectionArray = list(dict.fromkeys(selectionArray))
                else:
                    break
            except:
                break
            print("current selection", selectionArray)
        if(selection == -1):
            print(selection)
            table.set_index(theFilter, inplace = True)
            print("current selection", selectionArray)
            if selectionArray != []:
                table = table.loc[selectionArray]
                print(table)
                return table
            else:
                return table
        else:
            selection = 0
            filter_menu(theFilter, filterArray)
            print("current selection", selectionArray)
            print("Invalid choice.\n")

# output menu for given filter
def filter_menu(theArray, theFilter):
    print("\n" + "\033[1m" + "FILTER " + theArray.upper() + "\n(press a number)" + "\033[0;0m")
    for i in range(0, len(theFilter), 1):
        print("\033[1m", str(i+1), "\033[0;0m ", str(theFilter[i]))
    print("\033[1m", "0", "\033[0;0m ", "(next)")
    return len(theFilter)

# "filtersList" is the array of the columns to filter; "table" is the the path to the csv file
def applyFilters(filtersList, table):
    filtered_songs = pd.read_csv(table)
    for i in range(0, len(filtersList), 1):
        try:
            filter = category_list(filtersList[i], filtered_songs)
            # filter_menu(filtersList[i], filter)
            filtered_songs = filterSongs(filtersList[i], filtered_songs, filter)
        except Exception as e:
            print(e)
    print(filtered_songs)

# only "applyFilters" needs to be called
applyFilters(['artist', 'year', 'songwriter', 'type', 'style'], 'data/tableMusic.csv')

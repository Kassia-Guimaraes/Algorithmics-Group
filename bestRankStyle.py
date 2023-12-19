import pandas as pd
#Retrieves all the songs of a certain style

def getSongsOfStyle(tableMusic, style):
    #returns a subset of the dataframe "tableMusic"
    #with the songs of style corresponding to the argument "style"
    return tableMusic[tableMusic["style"] == style]    

# the function ranking that create a ranking of the style selected, 
# if it's greater than 3, and sort in descending order.
def rankingStyle(songs):
    bestSongs = songs[songs["rating_global"] > 3] 
    return bestSongs.sort_values("rating_global", ascending=False)


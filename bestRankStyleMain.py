import pandas as pd

def rankByStyle():
    import bestRankStyle
    tableMusic = pd.read_csv('data/tableMusic.csv')
    print(" here are the music styles:")
    #print only one value using .unique. for not repeat the same result. it makes the code more clean.
    for item in list(pd.unique(tableMusic["style"])):
        print(" ", item)
    styleInput = input(" enter a music style => ")
    #returns the best musics from one style
    songStyle = bestRankStyle.getSongsOfStyle(tableMusic,styleInput)
    if songStyle.empty:
        print("\033[1m WARNING: \033[0;0mstyle not found")
        rankByStyle()
    else:
        bestRankStyle = bestRankStyle.rankingStyle(songStyle)
        print(" here are the best ranking "+styleInput+" songs: ")
        print(" ", bestRankStyle)

import pandas as pd

def rankByStyle():
    import bestRankStyle
    tableMusic = pd.read_csv('data/tableMusic.csv')
    print(" Filter best songs by style")
    #print only one value using .unique. for not repeat the same result. it makes the code more clean.
    for item in list(pd.unique(tableMusic["style"])):
        print(" ", item)
    styleInput = input(" enter a music style (0 to return) => ")
    #returns the best musics from one style
    songStyle = bestRankStyle.getSongsOfStyle(tableMusic,styleInput)
    if styleInput == "0":
        return
    elif songStyle.empty:
        print("\033[1m WARNING: \033[0;0mstyle not found")
        rankByStyle()
    else:
        bestRankStyle = bestRankStyle.rankingStyle(songStyle)
        print(" Here are the best ranking "+styleInput+" songs: ")
        print(" ", bestRankStyle)

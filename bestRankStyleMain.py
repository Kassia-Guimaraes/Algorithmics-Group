import pandas as pd

def rankByStyle():
    import bestRankStyle
    tableMusic = pd.read_csv('data/tableMusic.csv')
    print("Here are the music Styles:")
    #print only one value using .unique. for not repeat the same result. it makes the code more clean.
    print(pd.unique(tableMusic["style"]))
    styleInput = input("Enter a music style:")
    #returns the best musics from one style
    songStyle = bestRankStyle.getSongsOfStyle(tableMusic,styleInput)
    bestRankStyle = bestRankStyle.rankingStyle(songStyle)
    print("Here are the best ranking "+styleInput+" songs: ")
    print(bestRankStyle)

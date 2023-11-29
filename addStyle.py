import pandas as pd

styles = []
tm = pd.read_csv("./tableMusic.csv", sep=(","), index_col='id_music')
styles = (list(tm.loc[:, "style"].drop_duplicates()))
def addStyle():
    styles.append(input())
print("add a sytle")
addStyle()

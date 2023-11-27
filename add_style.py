import pandas as pd

styles = []
tm = pd.read_csv('tableMusic.csv')
styles = (list(tm.loc[:, "style"].drop_duplicates()))
def addStyle():
    styles.append(input())
print("add a sytle")
addStyle()

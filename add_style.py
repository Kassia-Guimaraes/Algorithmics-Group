import pandas as pd

styles = []
df = pd.read_csv('tableMusic.csv')
styles = (list(df.loc[:, "style"].drop_duplicates()))
def addStyle():
    styles.append(input())
print("add a sytle")
addStyle()

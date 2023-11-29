import pandas as pd
import os.path
from pandas.core.internals.blocks import new_block

styles = []
tm = pd.read_csv("./tableMusic.csv", sep=(","), index_col='id_music')
styles = (list(tm.loc[:, "style"].drop_duplicates()))

# read populate styles with the "styles.csv" from previous execution, if it exists
if(os.path.isfile('styles.csv')):
    styles = (list(pd.read_csv('styles.csv').loc[:, "0"]))
    print("Current styles:" + ', '.join(styles))
# otherwise extract styles from tableMusic.csv
else:
    tm = pd.read_csv('tableMusic.csv')
    styles = (list(tm.loc[:, "style"].drop_duplicates()))
    print("Current styles:" + ', '.join(styles))

def addStyle():
    new_Style = (input())
    if new_Style == 0:
        print("Operation cancelled")
    else:
        styles.append(new_Style)
        print(f"The style {new_Style} was added successfully!")
print("What new style would you like to add?\nPress 0 to cancel")
addStyle()
styles_Df = pd.DataFrame(styles)
# create/update styles.csv with the new style
styles_Df.to_csv('styles.csv', index=False, na_rep="NAN!")
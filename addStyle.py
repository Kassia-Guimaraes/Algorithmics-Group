import pandas as pd
import os.path
from pandas.core.internals.blocks import new_block

def refresh_styles_list():
    # read populate styles with the "styles.csv" from previous execution, if it exists
    if(os.path.isfile('data/styles.csv')):
        return (list(pd.read_csv('data/styles.csv').loc[:, "0"]))
    # otherwise extract styles from tableMusic.csv
    else:
        tm = pd.read_csv('data/tableMusic.csv')
        return (list(tm.loc[:, "style"].drop_duplicates()))

def addStyle():
    styles = refresh_styles_list()
    print("Current styles: " + ', '.join(styles))
    new_Style = (input("What new style would you like to add?\nPress 0 to cancel\n=> "))
    if new_Style == "0":
        print("Operation cancelled")
    else:
        print(styles)
        styles.append(new_Style)
        styles_Df = pd.DataFrame(styles)
        # create/update styles.csv with the new style
        styles_Df.to_csv('data/styles.csv', index=False, na_rep="NAN!")
        print(f"The style {new_Style} was added successfully!")
    return new_Style

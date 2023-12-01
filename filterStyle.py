import pandas as pd
import os.path
import addStyle

# define styles with addStyle.py function
styles = addStyle.refresh_styles_list()

def pick_style_message():
    print("Pick the style:\n")
    for i in range(0, len(styles), 1):
        print(str(i+1) + " " + str(styles[i]) + "\n")

pick_style_message()

picked_style = 0
while picked_style == 0:
    try:
        picked_style = styles[int(input())-1]
        print("The style picked was " + str(picked_style))
    except:
        picked_style = 0
        print("Your choice is out of range.\n")
        pick_style_message()
# def picked_style_songs():
#     tm = pd.read_csv('tableMusic.csv')
#     return (list(tm.loc[:, "style"].drop_duplicates()))

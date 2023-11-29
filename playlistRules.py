import pandas as pd
import numpy as np
from IPython.display import display

tm = pd.read_csv("./tableMusic.csv", sep=(","), index_col='id_music')

drt_limit = 3600 #seconds
msc_limit_rt5 = 10 #10 rt >= 4
msc_limit_rt4 = 5 #10 rt < 4

#parameters
year = int(input("Search by specific year: "))
search_per_year = tm[tm['year']== year]

drt_total = search_per_year[['duration']].sum() #Soma da duração das músicas
count_elements = search_per_year[['title']].count() #conta quantos elementos têm na lista

while count_elements < 15:
    new_year = year - 1
    search_per_new_year = tm[tm['year']== new_year]
    search_per_year = pd.concat([search_per_year, search_per_new_year])

    count_elements = search_per_year[['title']].count() 

display(count_elements)
display(search_per_year[['title', 'artist', 'duration','style','year']])
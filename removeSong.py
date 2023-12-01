def removeSong(tableMusic,index):
    
    ret = index in tableMusic.index
    if index in tableMusic.index:
        tableMusic.drop(index, inplace=True)      
    else : 
        print("This index does not exist in our system. Please chose a valid option:")
        
        
    
    
    
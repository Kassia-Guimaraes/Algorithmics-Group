import pandas as pd
import random #Aleatory numbers

class IDGenerator: #Generator id class
    def __init__(self): #take id's in use
        self.last_id = 0
        self.used_ids = set()

    def generate_id(self): #new id
        self.last_id += 1
        while self.last_id in self.used_ids: #Keep generating a new ID unique
            self.last_id += 1
        self.used_ids.add(self.last_id)  #Add new ID to used IDs
        return self.last_id #Return last id created

# Instance of the IDGenerator class
id_generator = IDGenerator()

# Function to obtain ID
def get_new_id():
    return id_generator.generate_id()
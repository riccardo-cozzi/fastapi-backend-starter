import os
import json 

def load_users():
    dat_path = "../data/sampledata.json"
    with open(dat_path) as f:
        users = json.load(f)
    
    return list(users.values())

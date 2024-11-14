# JSON : big sets are normally stored and extracted by JSON, and it is a plain text, but it has a format of an object.
# plain-text refers to the value seperated with column.

# loading the JSON into a dataframe;

import pandas as pd
sagar = pd.read_json('data.json')
print(sagar.to_string())

print('...........................................')

# Dictonary as a JSON, if your data is not in JSON file but it is in python dictonary, then

import pandas as pd
data = {                # it is not neccesay to give the index 
    "Duration":{
        "0":64.3, 
        "1":75.6, 
        "2":49.5, 
        "3":93, 
        "4": 38, 
        "5": 83
        },
    "Pulse":{
        "0":129, 
        "1":190, 
        "2":100, 
        "3":140, 
        "4": 139, 
        "5": 172  
        },
    "MaxPulse":{
        "0":150, 
        "1":168, 
        "2":190, 
        "3":200, 
        "4":219, 
        "5":120
        },
    "Calories":{
        "0":499, 
        "1":394, 
        "2":594, 
        "3":600, 
        "4":524, 
        "5":420
        }
    }

sagar_new = pd.DataFrame(data)
print(sagar_new)



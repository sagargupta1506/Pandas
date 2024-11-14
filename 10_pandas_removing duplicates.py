# Remove duplicate value : first you need to find the duplicates values, via a duplicate() method

# loading and reading the original dataframe

import pandas as pd
sagar = pd.read_csv('Raw_data.csv')
print(sagar.to_string())

print('..................................................')
# returns True for every row that is duplicate otherwise return False
import pandas as pd
sagar = pd.read_csv('Raw_data.csv')
print(sagar.duplicated())

print('..................................................')
# removing the duplicate from the data set. via drop_duplicate()
import pandas as pd
sagar = pd.read_csv('Raw_data.csv')
sagar.drop_duplicates(inplace=True)
print(sagar.to_string())

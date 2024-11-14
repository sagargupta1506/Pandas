#  Quick View of your data: one of the most used methond for a quick overvies of the datframe is the head() method.
# this method returns headers and a specified number of rows.

# Here we shall print the first 10 rows in the dataframe from data.csv file.

import pandas as pd
sagar = pd.read_csv('data.csv')
print(sagar.head(10))  # by default it call the head funcion, which print the 5 rows.

print('........................................')

print(sagar.tail(10))         # tail

print('.................................')

# What if you want the information about the data in the dataframe : by using info()

import pandas as pd
df = pd.read_csv('data.csv')
print(df.info())
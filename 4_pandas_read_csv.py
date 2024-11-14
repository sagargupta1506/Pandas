# read csv files: (comma separated file/value), it a simple way to store the big and biggest data set.
# csv file contains plain text.

# loading the csv file into dataframe

import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string())         # to print the whole data use to_string()

print('..........................................')

# loading data withour to_string()
print(df)
print('............................................')

# max_rows: you can check your system's maximum rows with..

import pandas as pd
print(pd.options.display.max_rows)

print('................................................')
# yes, we can increae the max number of rows to display the entire dataframe.

import pandas as pd
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)




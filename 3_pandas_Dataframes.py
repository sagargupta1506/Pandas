# DataFrame : It is a 2d data structure like 2-d array, with table including rows and columns

import pandas as pd
data = {'cal':[420,380,390], 'duration':[50,65,45]}
sagar = pd.DataFrame(data)
print(sagar)
print('..........................')

# to access the particular index, pandas use the loc attributes to return one or more specified row.

print(sagar.loc[0])
print('...........................')

# to return more than one value we use the 2d array concept.
print(sagar.loc[[1,2]])
print('............................')

# named indexing : with the index argument, you can name your own index.what ever you want to add.

import pandas as pd
data = {'cal':[420,380,390], 'duration':[50,65,45]}
sagar = pd.DataFrame(data,index=['day1', 'day2', 'day3'])
print(sagar)
print('.............................')

# access the particular index with new index name
print(sagar.loc['day2'])      # the output in series based.
print('..............................')  
      

# to access more than one data 
print(sagar.loc[['day2', 'day3']])
print('...............................')


# load the data from the csv file into the dataframe.
# ie, file_name data.csv

import pandas as pd
fileload = pd.read_csv('C:/Users/sagar/OneDrive/Desktop/Sagar Gupta/Coding/Udemy')


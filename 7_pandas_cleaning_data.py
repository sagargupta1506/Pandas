# Cleaning data : It means fixing the raw(bad) data in your data set.
# raw data could be : empty data, data in a wrong format, duplicate data and wrong data.

# empty cell: it always gives wrong result, so we always have to remove the rows that contain raw data.

# loading and reading the original dataframe

import pandas as pd
sagar = pd.read_csv('Raw_data.csv') 
print(sagar.to_string())

print('..................................................')

# Here we shall return a new data frame with no empty cell.

import pandas as pd
sagar = pd.read_csv('Raw_data.csv') 
sagar_new = sagar.dropna()
print(sagar_new.to_string())      # to access the complete data

print('..................................................')


# If at any case you want to change the original data frame, than use the input= True argument.
# It will remove all the rows who have the null value.
# Nan = Not a number
import pandas as pd
sagar1 = pd.read_csv('Raw_data.csv')
sagar1.dropna(inplace=True)
print(sagar1.to_string())

print('..................................................')

# Replacing the empty value : now we shall use fillna() method, which allow us to replace the empty cell with a value.

import pandas as pd
sagar2 = pd.read_csv('Raw_data.csv')
sagar2.fillna(130, inplace=True)  # where the place is empty it fil with 130.
print(sagar2.to_string())

print('..................................................')


# To replace the empty value for one column, you need to specify the column name.

import pandas as pd
sagar2 = pd.read_csv('Raw_data.csv')
sagar2["Calories"].fillna(130, inplace=True) 
print(sagar2.to_string())

print('..................................................')
# here we can also replace the empty cell using mean(), median(), and mode().

# calculate the MEAN and replace the empty value with it.

import pandas as pd
sagar3 = pd.read_csv('Raw_data.csv')
x = sagar3["Calories"].mean()
sagar3["Calories"].fillna(x, inplace=True)
print(sagar3.to_string())

print('..................................................')
# Calculate the MEDIAN and replace any empty value in it.
import pandas as pd
sagar4 = pd.read_csv('Raw_data.csv')
x = sagar4["Calories"].median()
sagar4["Calories"].fillna(x, inplace=True)
print(sagar3.to_string())

print('..................................................')

# Calculate the MODE and replace with any empty value in it.

import pandas as pd
sagar3 = pd.read_csv('Raw_data.csv')
x = sagar3["Calories"].mode()[0]        # [0] indexing, starts from 0, and further and it put-up the frequently coming value.
sagar3["Calories"].fillna(x, inplace=True)
print(sagar3.to_string())


# Data in a wrong format : to fix this problem there are two ways.
# first, removing the rows and second, convert all the cells in the same format.

# loading and reading the original dataframe
import pandas as pd
sagar =  pd.read_csv('Raw_data.csv')
print(sagar.to_string())

print('..................................................')
# Now let's try to convert all the cells in the date column into dates. by using the method, to_datetime()

import pandas as pd
sagar1 = pd.read_csv('Raw_data.csv')
sagar1["Date"] = pd.to_datetime(sagar1['Date'])       # here we are doing overwrite.
print(sagar1.to_string())


print('..................................................')
# Here now we shall remove the rows with a null value in the 'Date' column only.

sagar1['Date'] = pd.to_datetime(sagar1['Date'])
sagar1.dropna(subset='Date', inplace=True)
print(sagar1.to_string())
 
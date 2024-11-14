# Pandas Series : A pandas series is like a column in a table. it is like '1D' array which holds data of any type

import pandas as pd
sagar = [1,7,2,9,4]         # list
sagar_new = pd.Series(sagar)
print(sagar_new)


# labeling : it can be used to accesss a specified value.
print('...............')

print(sagar_new[0])     # access a particular index value


print('......................')
# with creating label you can create your own label or index name(anything)

sagar_new = pd.Series(sagar, index=['s', 't', 'u','v','w'])
print(sagar_new)

print('................')
print(sagar_new['u'])


print('...................')
# you can also use a key or value object like a dictonary, when creating a series.
# Here we shall create a simple pandas series from a dictonary

import pandas as pd
calories = {'day1':420, 'day2':380, 'day3':330, 'day4':500}
sagar_New = pd.Series(calories)
print(sagar_New)

print('.......................')
# Now we create a variable result and access the specific day using the keys and, we have 2 keys at same time, so we are using list/array to store it.

import pandas as pd
calories = {'day1':420, 'day2':380, 'day3':330, 'day4':500}
result = pd.Series(calories, index=['day1', 'day2'])
print(result)

print('..............................')

# DataFrame: Datasets in pandas are usually multidimensional tables, and they are called DataFrame.

# Series are like columns, and DataFrames are like the whole table.

# Creating a DataFrame, and it is created by using the 2 series.

import pandas as pd
sagar = {'cal':[420, 380, 330, 500], 'duration':[50, 40, 45, 40]}
sagar1 = pd.DataFrame(sagar)
print(sagar1)
# Wrong Data :  its only a wrong data
# loading and reading dataframe.
# just like, 199 is written as 1.99


import pandas as pd
sagar = pd.read_csv('data.csv')
print(sagar.to_string())

print('.............................................................')
# Here we shall the set the "Duration" = 45 in row no 6
import pandas as pd
sagar = pd.read_csv('data.csv')
sagar.loc[5,'Duration'] = 45                                        # loc is a function of numpy
print(sagar.to_string())

print('...............................................')
# if we have a larger data set and need to correct the value, we can use loop, in "Duration" column, condition, if value is higher than 120 then set it to 120.
import pandas as pd
sagar1 = pd.read_csv('data.csv')
for i in sagar1.index:
    if sagar1.loc[i, "Duration"] > 120:
        sagar1.loc[i, "Duration"] = 120

print(sagar1.to_string())


print('..................................................')
# We can also remove the rows of wrong data in larger dataset.


import pandas as pd
sagar1 = pd.read_csv('data.csv')
for i in sagar1.index:
    if sagar1.loc[i, "Duration"] > 120:
        sagar1.drop(i,inplace=True)         #change

print(sagar1.to_string())





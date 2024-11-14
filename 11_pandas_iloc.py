# iloc  : integer location funcion
# dataframe.iloc[row_ind, column]

# selecting in sigle element

import pandas as pd
data = {'name':['sagar','sanjay','piyush','ayush'],
        'age':[25, 30, 22, 28],
        'country':['dubai','india','isral','russia']}

df = pd.DataFrame(data)
print(df)

print('................................................')
# to access a specific element india

element = df.iloc[1, 2]
print(element)

print('..................................................')
# to select specific rows and columns
subset = df.iloc[1:3, 0:2]
print(subset)
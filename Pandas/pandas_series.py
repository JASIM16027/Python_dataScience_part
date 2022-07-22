import pandas as pd
import numpy as np

lst = ['J', 'a', 's', 'i', 'm', 'U', 'd', 'd', 'i', 'n']
data = np.array(lst)
# Creating a series from array
res = pd.Series(data)
# create series form a list
ser = pd.Series(lst)
print(res)
print(ser)

# Accessing Element from Series with Position
print(ser[:5])
print(ser[5:])


ds = pd.Series(data, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# accessing a element using index element
print(ds[7])

# Indexing a Series using indexing operator [] :

df = pd.read_csv('nba.csv')

print(df)
series = pd.Series(df['Name'])
data1 = series.head(10)
print(data1)
print(df[3:6])

# value shows 3-6 [4x9 rows]
print(df.loc[3:6])

print(df.iloc[3:6])
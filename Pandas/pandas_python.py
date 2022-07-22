"""
Advantages
Fast and efficient for manipulating and analyzing data.
Data from different file objects can be loaded.
Easy handling of missing data (represented as NaN) in floating point as well as non-floating point data
Size mutability: columns can be inserted and deleted from DataFrame and higher dimensional objects
Data set merging and joining.
Flexible reshaping and pivoting of data sets
Provides time-series functionality.
Powerful group by functionality for performing split-apply-combine operations on data sets.

Pandas generally provide two data structure for manipulating data, They are:

Series
DataFrame


"""

import pandas as pd
import numpy as np

data = pd.DataFrame()
print("Data = {}\n".format(data))

list1 = ['Jasim', 'Karim', 'Rahim', 'Jewel']
dictionary = {
    "Name":['Alok', 'Jasim', 'A.Karim', 'A.Rahim', 'Shanto'],
    'Age' :[23, 24, 25, 23, 24],
    "Address":['Tangail', 'Jhenaidah', 'Dhaka', 'Nator', 'Rajshahi'],
    "Qualification": ['B.Sc', 'B.Sc', 'M.Sc', 'B.Sc', 'B.Sc']
}
df = pd.DataFrame(dictionary)

data = pd.DataFrame(list1)
print("Data = {}\n{}\n".format(data, df))

df1 = pd.DataFrame(df[['Name', 'Qualification']])
num = np.array(df1)
print(df1)
print(num)



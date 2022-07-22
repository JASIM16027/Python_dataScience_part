import pandas as pd
"""
dictionary = {
    "Name":['Alok', 'Jasim', 'A.Karim', 'A.Rahim', 'Shanto'],
    'Age' :[23, 24, 25, 23, 24],
    "Address":['Tangail', 'Jhenaidah', 'Dhaka', 'Nator', 'Rajshahi'],
    "Qualification": ['B.Sc', 'B.Sc', 'M.Sc', 'B.Sc', 'B.Sc'],
    "Score": [80, 70, 65, 80, 90]
}

data = pd.DataFrame(dictionary, index=[True, False, True, False, True])
print(data.loc[False], '\n\n')
print(data.loc[True], '\n\n')

print(data.iloc[4], '\n\n')

# Applying a boolean mask to a dataframe :

df = pd.DataFrame(dictionary, index=[0, 1, 2, 3, 4])
print(df[[True, False, True, False, True]], '\n\n')

data1 = pd.read_csv('employee_inf.csv')
dat = pd.DataFrame(data1, index=[0, 1, 2, 3, 4, 5, 6])

print(dat[[True, False, True, False, True, False, True]])


# Masking data based on column value :
# # using a comparison operator for filtering of data
da = pd.DataFrame(dictionary)
print(da['Qualification']=='B.Sc')

data_p = pd.read_csv('employee_inf.csv', index_col='Name')
# using greater than operator for filtering of data
print(data_p['Age']> 25)

print(data_p['Age']==25)

#  Masking data based on index value :

df1 = pd.DataFrame(dictionary, index=[0, 1, 2, 3, 4])

mask = df1.index ==0

print(df1[mask])
"""

df = pd.read_csv('employee_inf.csv')
data = pd.DataFrame(df, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(data)
mask = data.index >= 7
print(data[mask])

# retrieving multiple columns by indexing operator
print(df[['Name', 'Team', 'College', 'Salary']])

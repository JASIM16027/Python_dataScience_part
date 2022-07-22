import pandas as pd

d1 = {
    "Name":['Alok', 'Jasim', 'A.Karim', 'A.Rahim', 'Shanto'],
    'Age' :[23, 24, 25, 23, 24],
    "Address":['Tangail', 'Jhenaidah', 'Dhaka', 'Nator', 'Rajshahi'],
    "Qualification": ['B.Sc', 'B.Sc', 'M.Sc', 'B.Sc', 'B.Sc'],
    "Score": [80, 70, 65, 80, 90]
}

d2 = {
    "Name":['Rakib', 'Tamim', 'Arif', 'Ashlam', 'Shaikot'],
    'Age' :[23, 24, 25, 23, 27],
    "Address":['Tangail', 'Jhenaidah', 'Dhaka', 'Nator', 'Rajshahi'],
    "Qualification": ['B.Sc', 'B.Sc', 'M.Sc', 'B.Sc', 'B.Sc'],
    "Score": [80, 70, 65, 80, 90]
}

data1 = pd.DataFrame(d1, index=[0, 1, 2, 3, 4])
data2 = pd.DataFrame(d2,  index=[2, 3, 6, 7, 8])
print(data1)
print(data2)
final_df = pd.concat([data1, data2], axis=1, join='outer', sort=False)



print(final_df)




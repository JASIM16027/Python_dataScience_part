import pandas as pd

dictionary = {
    "Name":['Alok', 'Jasim', 'A.Karim', 'A.Rahim', 'Shanto'],
    'Age' :[23, 24, 25, 23, 24],
    "Address":['Tangail', 'Jhenaidah', 'Dhaka', 'Nator', 'Rajshahi'],
    "Qualification": ['B.Sc', 'B.Sc', 'M.Sc', 'B.Sc', 'B.Sc'],
    "Score": [80, 70, 65, 80, 90]
}

data = pd.DataFrame(dictionary)

x = data.groupby('Name')
multiple_key = data.groupby(['Name', 'Qualification'])

print(x.groups)
print(x.first())
print(multiple_key.groups)

grp = data.groupby(['Name']).sum()
print(grp)

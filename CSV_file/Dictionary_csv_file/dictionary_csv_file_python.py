import csv

mydict = [

    {'Name': 'Jasim Uddin', 'Deparment': 'CSE', 'Session': '2015-16', 'Batch': '13th', 'ID': 'CE-16027',
     'CGPA': '3.10'},
    {'Name': 'Alok',   'Deparment': 'CSE', 'Session': '2015-16', 'Batch': '13th', 'ID': 'CE-16023', 'CGPA': '3.20'},
    {'Name': 'Jewel',  'Deparment': 'CSE', 'Session': '2015-16', 'Batch': '13th', 'ID': 'CE-16035', 'CGPA': '3.30'},
    {'Name': 'Fahim',  'Deparment': 'CSE', 'Session': '2015-16', 'Batch': '13th', 'ID': 'CE-16041', 'CGPA': '3.25'},
    {'Name': 'Shanto', 'Deparment': 'CSE', 'Session': '2015-16', 'Batch': '13th', 'ID': 'CE-16026', 'CGPA': '3.25'}

        ]
fields = ['Name', 'Deparment', 'Session', 'Batch', 'ID', 'CGPA']  # list name fields

filename = 'university_records.csv'

with open(filename, 'w') as csvfile:
    # creating a csv dict writer object

    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # writing headers (field names)
    writer.writeheader()
    # writing data rows
    writer.writerows(mydict)


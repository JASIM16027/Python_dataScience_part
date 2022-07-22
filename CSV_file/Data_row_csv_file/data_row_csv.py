import csv

# field names

fields = ['Name', 'Deparment', 'Session', 'Batch', 'ID', 'CGPA']  # list name fields

# data row of csv file
# 2d list name rows here
rows = [

    ['Jasim Uddin', 'CSE', '2015-16', '13th', 'CE-16027', '3.10'],
    ['Alok', 'CSE', '2015-16', '13th', 'CE-16023', '3.20'],
    ['Jewel', 'CSE', '2015-16', '13th', 'CE-16035', '3.30'],
    ['Fahim', 'CSE', '2015-16', '13th', 'CE-16041', '3.25'],
    ['Shanto', 'CSE', '2015-16', '13th', 'CE-16026', '3.25']
]

# name of csv file name

filename = 'university_record.csv'

# writing to csv file

with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing  the fields
    csvwriter.writerow(fields)
    # writing the datarows
    csvwriter.writerows(rows)

import csv

# csv file name
file_name = '100 Sales Records.csv'

# initializing the titles and rows list
fields = []
rows = []

# Reading csv file

with open(file_name, 'r') as csvfile:

    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting file name through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total numbers of rows
    print("Total numbers of rows : %d " % csvreader.line_num)


# printing the fields name :

print("Field names are  ", '+'.join(field for field in fields))

print('\nFirst 5 rows are:\n')

for row in rows[:10]:
    for col in row:
        print(" %10s" % col),
    print('\n')

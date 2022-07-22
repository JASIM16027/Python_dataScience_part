import csv

with open('research-and-development-survey-2019-csv.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)

import json

dict1 = {

    'subject': {
        'math': 90,
        'physics': 95,
        'chemistry': 80
    }
}

with open("Sample.json", "w") as p:

    # json.dump() method can be used for writing to JSON file.
    json.dump(dict1, p)

#  In json Keys/Name must be strings with double quotes
employee = '{"Id" :"01", "Name": "Jasim", "Age": 25, "Salary" : 100000}'

# json.loads() method can parse a json string and the result will be a Python dictionary.
employee_dict = json.loads(employee)
print("Convert json string into python dictionary {}".format(employee_dict))

print(employee_dict['Name'])

# json.load() method can read a file which contains a JSON object.
# Consider a file named employee.json which contains a JSON object.
with open("Sample.json", "r") as read_it:
    data = json.load(read_it)
    print(data)
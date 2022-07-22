import json
"""
file = open('json_data.json')
f = file.read()
print(f)
"""
person = {

    "Student":[
        {
            "name": "Jasim",
            "age" : 24,
            "university": "Mbstu",
            "Dept": "CSE",
            "year": "2015-16"

        },
        {
            "name": "Jewel",
            "age": 24,
            "university": "Mbstu",
            "Dept": "CSE",
            "year": "2015-16"

        },
        {
            "name": "Shanto",
            "age": 24,
            "university": "Mbstu",
            "Dept": "CSE",
            "year": "2015-16"

        }

    ]
}
with open('json_f.json', 'w') as write_f:
    json.dump(person, write_f, indent=2)

with open('json_f.json', 'r') as read_f:
    data = json.load(read_f)

for p in data['Student']:
    del p['age']
with open('json_person_data.json', 'w') as write:
    json.dump(data, write, indent=2)

with open('json_person_data.json', 'r') as read:
    data_value = json.load(read)

print(data_value)
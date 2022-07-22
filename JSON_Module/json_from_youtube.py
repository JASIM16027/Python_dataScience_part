import json

people_string = '''
{
"people": [
    {
        "name": "Jasim",
        "age" : 24,
        "dept": "CSE",
        "profession": "Software Engineer"
    },
    
     {
        "name": "Jewel",
        "age" : 24,
        "dept": "CSE",
        "profession": "Software Engineer"
    },
    
     {
        "name": "Rakib",
        "age" : 24,
        "dept": "CSE",
        "profession": "Software Engineer"
    }

]
}

'''

data = json.loads(people_string)
print(type(data))
print(data['people'])
"""
print("converted json object into python dictionary\n {}".format(data), '\n')
print(data['people'][0])
print(data['people'][0]['name'], end='--->')
print(data['people'][0]['age'])
print(data['people'][0]['profession'])

print(data['people'][1])
print(data['people'][1]['name'], end='--->')
print(data['people'][1]['age'])

print(data['people'][2])
print(data['people'][2]['name'], end='--->')
print(data['people'][2]['age'])

"""

for person in data['people']:
    del person['age']


new_string = json.dumps(data, indent=2)   # sort_keys=True

print(type(new_string))
print(new_string)

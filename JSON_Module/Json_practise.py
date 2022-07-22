import json

person = {'name': 'Jasim uddin',
          'age': 24,
          'salary': 100000

          }

list1 = ['Jasim', 'Shanto', 'Jewel']

tuple1 = ('Jasim', 'Shanto', 'Jewel')

# json.dumps() method can convert a Python object into a JSON string.
a = json.dumps(person)
b = json.dumps(list1)

c = json.dumps(tuple1)

print('dictionary converted to json object : {}'.format(a))

print('List conversion to json array :{}'.format(b))

print('tuple conversion to json array :{}'.format(c))

# int, long, float are converted into number
print(json.dumps(1234))

# str is converted into string

print(json.dumps("Hello, I'm Jasim"))



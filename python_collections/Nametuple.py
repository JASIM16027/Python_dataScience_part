from collections import namedtuple
"""
Point = namedtuple('Point', 'x,y')

pt = Point(1, 5)

print(pt.x, pt.y)
print(pt)

Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(55, 155, 255)
# access by key value
print(color.red)
# access by indexing
print(color[2])
# Access using getattr()

print('the value of red : ', getattr(color, 'red'))

"""

Student = namedtuple('Student', ['name', 'age', 'DOB'])
student = Student('Jasim uddin', '25', '03-01-96')
print(student.DOB)

li = ['Yasin', '22', '03-01-1998']
dictionary = {'name': 'Tabassum', 'age': '23', 'DOB': '1-1-97'}

# using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is  : ")
print(student._asdict())

# using _make() to return namedtuple()
print("The namedtuple instance using iterable is  : ")
print(Student._make(li))

# using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is  : ")
print(Student(**dictionary))

print(student._fields)

print(student._replace(name='Jewel'))
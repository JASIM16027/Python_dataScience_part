Student = {'name': 'Jasim Uddin', 'age': 25, 'Stu_id': 'CE-16027',
           'courses': ['Math', 'Computer Science', 'Accounting']}
print(Student)
print()
print('printing each of index from start to end : ')
print(Student['name'])
print(Student['age'])
print(Student['Stu_id'])
print(Student['courses'])

print()
print(Student.get('name', 'Not found'))
print(Student.get('phone', 'Not found'))

Student['phone'] = '01987-476130'
print()
print(Student.get('name', 'Not found'))
print(Student.get('phone', 'Not found'))

Student.update({'name': 'Jasim Uddin', 'age': 26, 'school': 'Mbstu'})
age = Student.pop('age')
del Student['courses']
print(Student)
print(age)

# more method

print(Student.keys())
print(Student.values())
print(Student.__len__())
print(len(Student))

print(Student.items())

print()
print("###########################################################")

for key, value in Student.items():
    print(key, ' : ', value)


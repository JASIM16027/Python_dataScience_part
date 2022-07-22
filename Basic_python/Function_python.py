def func(greeting, name):
    return '{} , {} '.format(greeting, name)


print(func(greeting='Hi', name='Jasim'))
print(func(greeting="I'm there", name= 'Jasim'))
print(func('Hi', 'Jasim'))
print(func('Hi I am there', 'Jasim'))


# Example 01

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math','Physics', 'Computer Science',
             name="Jasim", age=25, major_sub='Computer Science', university='Mbstu')

list1 = ['Math', 'Physics', 'Computer Science']
dic = {'name': 'Jasim', 'age': 25, 'major_sub': 'Computer Science', 'university': 'Mbstu'}


def stu_info(*args, **kwargs):
    print(args)
    print(kwargs)


stu_info(list1, dic)
stu_info(*list1, **dic)


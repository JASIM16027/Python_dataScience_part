courses = ['Computer Science', 'Math', 'Science', 'Biology', 'Information Technology']
num = [4, 3, 2, 1, 5]
num.sort()
sorted_courses = sorted(courses)
print(sorted_courses)
print(num)
num.sort(reverse=True)
print(num)

print(courses.index('Computer Science'))
print(courses.index('Math'))
print(courses.index('Biology'))
print(courses.index('Information Technology'))

print()

print('Art' in courses)

print('Math' in courses)
print()
print("Starting from 0 to end : ")
for index, course in enumerate(courses):
    print(index, course)


print()
print('Starting from 1 to end : ')
for index, course in enumerate(courses, start=1):
    print(index, course)
print()

course_str =' --> '.join(courses)
print(course_str)

new_list = course_str.split(' --> ')
print(new_list)

empty_list1 = []
empty_list2 = list()
empty_list1.append('Art')
empty_list1.append('Science')
empty_list1.append('Math')
empty_list1.insert(1,'Biology')
empty_list2.extend(empty_list1)
empty_list2.append('Physics')
for index, item in enumerate(empty_list1, start=1):
    print(index, item)

print(empty_list1)
print(empty_list2)
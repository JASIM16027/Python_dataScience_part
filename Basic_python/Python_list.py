# List in python

courses = ['Math', 'Physics', 'Science', 'Chemistry', 'Biology']
courses1 = ['Management', 'Analytical Math']
print(courses)
print("the length of list  is ", len(courses[2:]))
print("the length of list  is ", len(courses))

print()
print()

print("the negative index value from -1 to -5 is : ")

print(courses[-1])
print(courses[-2])
print(courses[-3])
print(courses[-4])
print(courses[-5])
print()

print("the positive index value from 0 to 4 is : ")

print(courses[0])
print(courses[1])
print(courses[2])
print(courses[3])
print(courses[4])

print(courses[0:2])
print(courses[1:4])
print(courses[2:4])
print(courses[3:4])

print()
print()

print(courses[2:])
print(courses[:2])
print(courses[:1])

courses.append('Social Science')
courses.append('Religion Education')

print(courses)

courses.insert(3, 'Art')

print(courses)
# insert
courses.insert(0, courses1)
print("Insert one list into another : ")
print(courses)

courses.append(courses1)
print("append one list to another :")
print(courses)

courses.extend(courses1)
print("Extend one list to another is : ")
print(courses)

# remove method

courses.remove(courses1)
print(courses)

# pop() method

popped = courses.pop()
print(popped)
print("After popped up value from course :  ")
print(courses)

#courses.sort()
#print(courses)
courses.reverse()
print(courses)

cs_courses = {'Computer Science', 'Math', 'Science', 'Biology', 'Information Technology'}
art_courses = {'Art', 'Math', 'Science', 'Sociology', 'Information Technology'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))

print(cs_courses.union(art_courses))

empty_set = set()
empty_set.add(10)
empty_set.add(30)
empty_set.add(40)
print(empty_set)
empty_set.remove(10)
print(empty_set)

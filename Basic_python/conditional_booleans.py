language = 'Java'
if language == 'python':
    print('The language is Pyhton')

elif language == 'Java':
    print('The language is Java')

elif language == 'Javascript':
    print('The language is Javascript')

else:
    print("Not match")

# Example 02

user = 'Admin'
login = False

if user == 'Admin' or login:
    print("Admin page")

else:
    print('Not match')


# Example 03
logged_in = True

if not logged_in:
    print("Please logged in ")
else:
    print("Logged in successfully")

# Example 04

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]

print(list1 == list2)
print(list1 is list2)
print(id(list1))
print(id(list2))
print(id(list1) == id(list2))
print()
print()


# Example 05
list1 = [1, 2, 3, 4]
list2 = list1

print(list1 == list2)
print(list1 is list2)
print(id(list1))
print(id(list2))
print(id(list1) == id(list2))



from collections import OrderedDict

d={}
d['c'] = 4
d['a'] = 1
d['b'] = 2
d['d'] = 5

for key, value in d.items():
    print(key, value)
d['b'] = 6
print('this is a dictionary')
for key, value in d.items():
    print(key, value)

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 5

print('this is order dictionary : ')
for key, value in od.items():
    print(key, value)

od['f'] = 5
print('this is order dictionary : ')

for key, value in od.items():
    print(key, value)

od.pop('c')

print('After popping odered Dictionary ')
for key, value in od.items():
    print(key, value)

od['c'] = 6

print('After reinserting ')

for key, value in od.items():
    print(key, value)

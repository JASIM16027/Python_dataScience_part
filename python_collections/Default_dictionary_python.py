import collections
"""
from collections import defaultdict


def def_value():
    return 'Not present'


d = defaultdict(def_value)
d['a'] = 5
d['b'] = 6
d['c'] = 7

print(d['d'])
"""
"""
from collections import defaultdict

d = defaultdict(lambda: 'Not present')

d['a'] = 1
d['b'] = 2
d['c'] = 3

print(d['c'])
print(d['d'])
print(d.__missing__('a'))
print(d.__missing__('d'))

dl = defaultdict(list)

for i in range(10):
    dl[i].append(i)

print(dl)
# dl.update({1: [3], 2: [4]})

# print(dl)

di = defaultdict(int)
l = [1, 2, 3, 1, 2, 3, 4, 4, 4, 3, 5, 5]
for i in l:
    di[i] += 1
    print('i = ', i, 'di = ', di[i])
print(di)
"""
#  ChainMap in Python

dict1 = {'a': 5, 'b': 10, 'c': 20}
dict2 = {'a': 15, 'd': 10, 'b': 30, 'e': 15}
dict3 = {'h': 4, 'g': 27}
chain = collections.ChainMap(dict1, dict2)
print(chain)
print(chain.maps)

print(list(chain.keys()))
print(list(chain.values()))
chain1 = chain.new_child(dict3)
print(chain1)

print(chain1.maps)

print(list(chain1.keys()))

print(list(chain1.values()))

# displaying value associated with b before reversing
print(chain1['b'])
# reversing the ChainMap

chain1.maps = reversed(chain1.maps)
print(chain1['b'])
print(chain1['a'])
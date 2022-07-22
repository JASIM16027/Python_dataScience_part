import collections

de = collections.deque([1, 4, 5, 5, 5, 5, 6, 2, 3])
'''de.append(1)
de.append(5)
de.appendleft(6)
print(de)
de.pop()
de.popleft()
print(de)
'''

print(de.index(4, 1, 5))

# using insert() to insert the value 6 at 4th position
de.insert(3, 6)
print(de)

# using count() to count the occurrences of 5
print(de.count(5))

# using remove() to remove the first occurrence of 3

de.remove(3)
print(de)
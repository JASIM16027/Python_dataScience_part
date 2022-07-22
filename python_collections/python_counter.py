from collections import Counter

list1 = ['A', 'B', 'A', 'A', 'B', 'A', 'B', 'C', 'C', 'B', 'C', 'B', 'A', 'C', 'B', 'A','A']

print(Counter(list1))

print(Counter({'A': 5, 'B': 5, 'C': 4}))

print(Counter(A=5, B=5, C=4))

coun = Counter()
coun.update([1, 2, 3, 4, 5, 6, 7])
print(coun)

coun.update([1, 2, 3, 4, 5, 6])
print(coun)
coun.update([1, 2, 3, 4, 5, 6])
print(coun)

tally = Counter()
for i in list1:
    tally[i]+=1
    print((i, tally[i]), end=' ')
print('\n')
print(tally)


n = 'aaaaabbbbbccccccdddddddddddhhhhhhhhhhhh'
mycounter = Counter(n)
print(mycounter)
print(mycounter.most_common(3))
print(mycounter.most_common(3)[0][0])

print(list(mycounter.elements()))

from collections import Counter
a = 'aaaaaaaabbbbcccccm'
my_counter = Counter(a)
print(list(my_counter.elements()))
print(my_counter, my_counter.values(),sep='\n')

print(my_counter.items(),
      my_counter.keys(),
      my_counter.most_common(1),
      my_counter.most_common(2),sep='\n')

print(my_counter.most_common(2)[1][1])

dictionary = {}
dictionary['b'] = 1
dictionary['b'] = 1
dictionary['b'] = 1


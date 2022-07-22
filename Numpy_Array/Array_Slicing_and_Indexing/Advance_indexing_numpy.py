import numpy as np

arr = np.array([
    [1, 2, 4, 5, 6],
    [5, 6, 7, 8, 9],
    [4, 6, 7, 8, 3],
    [4, 6, 6, 7, 3],
    [9, 7, 5, 3, 2]
])
# Purely integer indexing
print(arr[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]])
print(arr[[0, 1, 2, 3, 4], [4, 3, 2, 1, 0]])
print(arr[[0, 1, 2, 3, 4], [2, 2, 2, 2, 2]])

print('\n\n')

#  Combining advanced and basic indexing

print(arr[1:4:2, [1, 3, 4]])
print(arr[[1, 3, 4], 1:4:2])

# Boolean Array Indexing:

print(arr[arr > 8])

print(arr[arr % 4 == 0]**2)

sumrow = arr.sum(-1)
print(sumrow)
print(arr[sumrow % 7 == 0])

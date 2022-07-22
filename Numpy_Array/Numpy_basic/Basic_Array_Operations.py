import numpy as np

arr1 = np.array([

    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7]
])

arr2 = np.array([

    [2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 6, 7]
])

summation = arr1 + arr2
# Performing Binary operations
print(summation)

# Performing Unary operations
print('sum of array arr1 : ', arr1.sum())

print("Display arr1 and add 1 with arr1: ")
print(arr1, '\n')
print(arr1+1)

print("Display arr2 and subtract 2 from arr2: ")
print(arr2, '\n')
print(arr2-2, '\n')

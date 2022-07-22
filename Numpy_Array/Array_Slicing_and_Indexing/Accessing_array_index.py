import numpy as np

arr = np.array([
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [4, 5, 6, 7, 8],
    [2, 3, 4, 6, 7]

])

print(arr)

print("Start from 0 index to end index 2 : ")
arr1 = arr[:2, 2:]
print(arr1)

print("Start from 0 and jump 2 column each time : ")
arr2 = arr[::2, ::2]
print(arr2)


print("Index accessing : ")
Index_arr = arr[[1, 1, 0, 3, 2],
                [3, 2, 1, 0, 2]]
print(Index_arr)
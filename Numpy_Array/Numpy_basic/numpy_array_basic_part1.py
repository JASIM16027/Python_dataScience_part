import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Numpy 1d array : ")
print(arr)

print()
print("Numpy 2d array : ")
arr1 = np.array([[1, 2, 3, 4, 5],
                 [3, 4, 5, 6, 7],
                 [3, 2, 3, 4, 5]

                 ])
print(arr1)


arr3 = []
for x in range(0, 10):
    for y in range(0, 5):
        arr3.append(y)

numpy_arr = np.array(arr3)
numpy_arr1 = numpy_arr.reshape(5, 10)
print("Numpy 1d ---> 2d array : ")
print(numpy_arr1)





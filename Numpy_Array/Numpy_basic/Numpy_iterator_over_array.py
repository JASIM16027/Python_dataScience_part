import numpy as np

arr = np.arange(20)

arr = arr.reshape(4, 5)
print(arr)

for x in np.nditer(arr):
    print(x, end=" ")
print('\n')
a = arr.T

print("Transpose of arr  a: \n\n{}".format(a))
print('\n\n')
# Controlling Iteration Order

for x in np.nditer(arr, order='F'):
    print(x, end=" ")

print('\n')

b = arr.T
print("Transpose of arr  a: \n\n{}".format(b))


#  Modifying Array Values

print(arr)
for x in np.nditer(arr, op_flags=['readwrite']):
    x[...] = 5 * x

print(arr)

arr1 = np.arange(12)
arr1 = arr1.reshape(3, 4)

for x in np.nditer(arr1, flags=['external_loop'], order='C'):
    print(x)

numpy_arr = np.arange(12)
numpy_arr = numpy_arr.reshape(3, 4)

it = np.nditer(numpy_arr, flags=['c_index'], order='C')
while not it.finished:
    print("%d <--%d" % (it[0], it.index), end=" ")
    it.iternext()

print('\n')
it = np.nditer(numpy_arr, flags=['f_index'], order='C')
while not it.finished:
    print("%d <--%d" % (it[0], it.index), end=" ")
    it.iternext()

broadcast_array = np.arange(12)
broadcast_array = broadcast_array.reshape(3, 4)
print("the broadcast array is : \n {}".format(broadcast_array))

broadcast_array_second = np.array([1, 2, 4, 5])

for x, y in np.nditer([broadcast_array, broadcast_array_second]):
    print(" %d:%d" % (x, y), end=" ")

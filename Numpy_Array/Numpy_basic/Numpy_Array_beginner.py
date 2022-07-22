import numpy as np

list1 = [1, 2, 3, 4, 5]
arr = np.array(list1)

print(arr)
print('two dimensional array is ')
list2 = [1, 2, 4, 7, 9]
list3 = [8, 3, 4, 7, 9]

arr1 = np.array([list1, list2, list3])
print(arr1)

print()
print('the new array is  ')
print(arr1[0:2, 2:])

print()
print('the new array is  ')

print(arr1[0:2, 0:2])
print('the range between 0 and 10 but step size is 2 :')
arr2 = np.arange(0, 10, 2)

print(arr2)

print('the shape of arr1 is ')
print(arr1.shape)

print()
print('the reshape array is (5, 3) : ')

print(arr1.reshape(5, 3))

print()
print('the reshape array is (1, 15): ')

print(arr1.reshape(1, 15))

arr3 = arr1.copy()

print(arr3)

arr4 = np.array([arr1, arr3])

print('3d array : ')
print('Random value between 0 and 10 is ')
print(arr4)

print(np.linspace(0, 10, 100))

val = 2
ar = arr1 < 5
print(arr1[ar])

arr5 = np.arange(0, 15)

arr5[3:] =100

print(arr5)

arr7 = arr5

arr7[3:] = 500


print(arr7[3:])
import numpy as np

print(np.dtype(np.int16))

dt = np.dtype('>i4')

print("Byte order is : {}\nSize is {}\nName of data type is {}\n"
      .format(dt.byteorder, dt.itemsize, dt.name))

arr = np.array([1, 3, 4, 5, 6])

print("Data type = {} \ntype of numpy array = {} ".format(arr.dtype, type(arr)))

"""
Syntax : numpy.random.randint(low, high=None, size=None, dtype=’l’)

Parameters :
low : [int] Lowest (signed) integer to be drawn from the distribution.
But, it works as a highest integer in the sample if high=None.
high : [int, optional] Largest (signed) integer to be drawn from the distribution.
size : [int or tuple of ints, optional] Output shape. If the given shape is,e.g., (m, n, k),
then m * n * k samples are drawn. Default is None, in which case a single value is returned.
dtype : [optional] Desired output data-type.

Return : Array of random integers in the interval [low, high) or a single such random int if size not provided.
"""
import numpy as np
import random

a = np.random.randint(low=0, high=3, size=4)
print(a)

arr = np.random.randint(low=3, high=10, size=(4, 4))

b = np.random.randint(low=4, size=(3, 4))
print("2D array  : \n\n{}\n\n 2D array :\n\n {}\n\n".format(arr, b))

print()

# 3d array

arr_3d = np.random.randint(low=0, high=5, size=(2, 3, 3))
print("3D array :\n{}\n".format(arr_3d))

"""
Syntax : numpy.random.ranf(size=None)

Parameters :
size : [int or tuple of ints, optional] Output shape.
If the given shape is, e.g., (m, n, k), then m * n * k samples are drawn.
 Default is None, in which case a single value is returned.

Return : Array of random floats in the interval [0.0, 1.0). or a single such random float if size not provided
"""

arr_float = np.random.ranf(size=(3, 3, 3))
print("3D floating array : \n\n{}\n ".format(arr_float))

"""
# random integers

D3_arr = np.random.random_integers(low=1, high=5, size=(2, 3, 2))
print("3D array : \n{}".format(D3_arr))

D1_arr = np.random.random_integers(1, 5, size=3)

print(D1_arr)

"""



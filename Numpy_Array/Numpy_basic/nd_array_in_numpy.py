import numpy as np

"""
arr = np.array([

    [1, 2, 4, 6, 8],
    [3, 5, 7, 2, 8],
    [9, 6, 7, 2, 6]
])

print(" Array shape : {} \n Array size : {}\n Sum of Array {}\n Array type : {}\n "
      .format(arr.shape, arr.size, sum(arr), arr.dtype))

print("Dimension of array {}\n".format(arr.ndim))


"""
arr = np.array([
    [1, 3, 4, 5, 6],
    [4, 6, 8, 3, 5],
    [5, 6, 7, 3, 5]

    ],

    dtype='float'

)

print("Array : \n \n{} ".format(arr))

c = np.zeros((3, 5))

print("All element is zero in arr(3, 5) :\n\n{} ".format(c))

n = np.full((5, 4), 8, dtype=complex)

print("All the element is 6 :  \n{}  \n ".format(n))
import numpy as np

arr = np.arange(10)

#         arr:     [0   1  2  3  4  5  6  7  8  9]
#  positive index : 0   1  2  3  4  5  6  7  8  9
#  negative index :-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
x = arr[-2:10:1]
print("x = {}".format(x))

y = arr[-4:1:1]

print("x = {}".format(y))

print("a = {} ".format(arr[5:]))

print("b = {} ".format(arr[3:-2: 1]))
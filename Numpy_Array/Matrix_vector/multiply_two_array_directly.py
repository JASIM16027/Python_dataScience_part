import numpy as np


list1 = [1, 2, 4, 5, 6, 7]

list2 = [2, 4, 6, 8, 1, 6]

print(list1)

x = np.array(list1)

y = np.array(list2)

print("multiply x {} and  y{} =  product {} ".format(x, y, x*y))

s = np.arange(10, 1, -1)
s1= np.arange(10, 1, -1)

print(s)

xx = s[np.array([1, 3, 5])]
yy = s1[np.array([3, 5, 7])]

print(xx*yy)

a = np.arange(20)
print(a)
x = a[-8:17:1]
y = a[-19:13:1]
print(x)
print(y)

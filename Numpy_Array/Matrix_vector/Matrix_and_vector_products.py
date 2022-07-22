"""
numpy.dot(vector_a, vector_b, out = None) :
returns the dot product of vectors a and b.
It can handle 2D arrays but considering them as matrix and will perform matrix multiplication.
For N dimensions it is a sum product over the last axis of a and the second-to-last of b :

dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])

"""

import numpy as np

product1 = np.dot(5, 4)
print(product1)

vector_a = 3 + 2j
vector_b = 5 + 4j

product = np.dot(vector_a, vector_b)

print(product)

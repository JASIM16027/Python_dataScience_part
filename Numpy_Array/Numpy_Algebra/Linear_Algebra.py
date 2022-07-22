"""
Numpy | Linear Algebra
The Linear Algebra module of NumPy offers various methods to apply linear algebra on any numpy array.
One can find:

rank, determinant, trace, etc. of an array.
eigen values of matrices
matrix and vector products (dot, inner, outer,etc. product), matrix exponentiation
solve linear or tensor equations and much more!

"""
import numpy as np

A = np.array([
    [1, 2, 9],
    [2, 8, 4],
    [9, 5, 6]

])

print("Matrix Range of A : ", np.linalg.matrix_rank(A))

print("Matrix trace of A : ", np.trace(A))

print("Determinant of A : ", np.linalg.det(A))

print("Inverse of A :\n ", np.linalg.inv(A))

print("Matrix A raise to power 3 : \n", np.linalg.matrix_power(A, 3))


#  Matrix eigenvalues Functions


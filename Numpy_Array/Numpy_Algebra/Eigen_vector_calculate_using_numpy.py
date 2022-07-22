"""
numpy.linalg.eigh(a, UPLO=’L’) :
This function is used to return the eigenvalues
and eigenvectors of a complex Hermitian (conjugate symmetric)
or a real symmetric matrix.Returns two objects,
a 1-D array containing the eigenvalues of a, and a 2-D square array
or matrix (depending on the input type) of the corresponding eigenvectors (in columns).

"""

import numpy as np

A = np.array([[1, -2j], [2j, 5]])

print(A)
print()

eigen_values, two_d_square_matrix = np.linalg.eigh(A)

print("Eigen Value of A \n{} \n\n2D Square Matrix :\n {}".format(eigen_values, two_d_square_matrix))

"""
numpy.linalg.eig(a) :
This function is used to compute the eigenvalues and right eigenvectors of a square array.
"""

B = np.diag((7, 9, 6))

print("Array : \n", B)

a, b = np.linalg.eigh(B)

print("Eigen Value : \n", a)

print("Eigen Vector : \n ", b)

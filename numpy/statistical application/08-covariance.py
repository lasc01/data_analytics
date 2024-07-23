import numpy as np

# Covariance matrix is a type of matrix that is used to represent 
# the covariance values between pairs of elements given in a random vector.

matrix_A = np.array([[2,0,2,0,3],[4,2,2,0,3],[3,2,1,2,1]])

print(np.cov(matrix_A))

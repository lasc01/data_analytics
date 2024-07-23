import numpy as np

# The median takes an input array and returns the median value after being sorted. e.g

matrix_A = np.array([[2,0,2,0,3],[4,2,2,0,3],[3,2,1,2,1]])

print(np.sort(matrix_A, axis= None))

print(np.median(matrix_A))
import numpy as np

# nan functions are very useful when we have incomplete data. e.g

matrix_A = np.array([[2,0,2,0,3],[4,2,np.nan,0,3],[3,2,1,2,1]])
print(matrix_A)

print(np.nanmean(matrix_A))

print(np.nanvar(matrix_A))

print(np.nanpercentile(matrix_A, 60))
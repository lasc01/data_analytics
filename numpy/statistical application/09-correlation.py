import numpy as np

# Correlation coefficiant(corrcoef()) finds the relationship between every two rows and array. 

matrix_A = np.array([[2,0,2,0,3],[4,2,2,0,3],[3,2,1,2,1]])

print(np.corrcoef(matrix_A))

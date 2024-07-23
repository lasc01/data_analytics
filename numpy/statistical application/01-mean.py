import numpy as np

# The mean function helps us to find the mean of set of values in a data set. e.g

matrix_A = np.array([[2,0,2,0,3],[4,2,2,0,3],[3,2,1,2,1]])

print(matrix_A)

# The below will print out the mean of the data set.
# print(np.mean(matrix_A))

# To get the mean of just a row, check below. Below will print out the mean of the 2nd row
# print(np.mean(matrix_A[1]))

# To get the mean of just a column, check below. Below will print out the mean of the 1st column
# print(np.mean(matrix_A[:,0]))

# To get the mean of just all column alone, check below. Below will print out the mean of all columns
# print(np.mean(matrix_A, axis = 0))

# To get the mean of just all row alone, check below. Below will print out the mean of all rows
print(np.mean(matrix_A, axis = 1))
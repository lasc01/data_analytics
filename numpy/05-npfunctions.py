import numpy as np

array_a = np.array([1,2,3])

array_b = np.array([[1],[2]])

matrix_c = np.array([[1,2,3], [4,5,6]])

# print(array_a, array_b, matrix_c)\

# BROADCASTING

# Broadcasting is the act of stretching a variable over another oner in order to get same shape
# the example below adds array_ to matrix_c. The output gives a result of the shape of the matrix_c
# This implies that the elements in array_a is broadcasted & added to all elements in matrix_c
# Therefore, the vector [1,2,3] becomes a matrix [[1,2,3][1,2,3]] in order to complete the computation

# print(np.add(array_a, matrix_c))

# This can also word in form of columns.
# If array_b is added to matrix c, it is broadcasted to suit the shape of matrix_c. i.e array_b becomes
# [[1],[2]], [[1],[2]], [[1],[2]] 

# print(np.add(array_b, matrix_c))

# TYPE CASTING

# Type casting is the act of taking every element in an array & changing it to a specific datatype
# e.g

# print(np.add(array_b, matrix_c, dtype='float64'))

# RUNNING OVER AN AXIS
# This is the act of running a function over an axis. Running it over axis = 0 means you are running
# the function over a column. But running it over an axis = 1 means you are running the function
# over a row. e.g

print(np.mean(matrix_c, axis=0))
print(np.mean(matrix_c, axis=1))

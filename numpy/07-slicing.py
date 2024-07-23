import numpy as np

matrix_A = np.array([[1,2,3],[4,5,6]])

# BASIC SLICING
# SLICING ROWS

# Note that the upper limit is mot always included but the lower limit is included. 
# E.G the example below will print out the first row only

# print(matrix_A[0:1])

# This will proint out only the second row
# print(matrix_A[1:2])

# While this will print an empty array
# print(matrix_A[0:0])

# The example below should print all rows before index 1
# print(matrix_A[:1])

# This should print out all row after the first row
# print(matrix_A[1:])

# NB: Slicing and indexing are a lot similar. But the main difference between them is the output of
# the array. while they both print out same values, indexing will always print out a 1-d array
# while slicing prints out the the dimension of the initial array. E.g 

# print(matrix_A[0])
# 1-d array
# print(matrix_A[:1])
# 2-d array

# SLICING COLOMNS

# In order to slice a column, you must add the comma sign to differentiate the row from the column
# With the first value being the row, and the second value being the column. E.g
# The example below will outpul all the rows, and the 2 columns from 1. so the output
# should be [[3,4], [5,6]]
# print(matrix_A[:, 1:])


# STEPWISE SLICING

# Syntax for the stepwise slicing is mor like the for loop. It is writter like [a:b:c]. Where a is 
# the beginning of the set, b is the end, and c is the step. by default, c is set to 1
# NB:The step value can't be 0

matrix_B = np.array([[1,1,2,3,4], [4,1,3,7,2], [9,4,6,1,4]])

# The e.g below will print out all value in the dataset as the step is defaultly set to 1
# print(matrix_B[::,::])

# This will print out the the value of the row only in 2 steps
# print(matrix_B[::2, ::])

# This will print out the column only in 2 steps
# print(matrix_B[::,::2])

# This will print out the row and column in 2 steps
# print(matrix_B[::2,::2])

# This will print out 2 steps of colum amd row from the second index
# print(matrix_B[1::2,1::2])


# CONDITIONAL SLICING

matrix_C = np.array([[1,1,2,3,4], [4,1,3,7,2], [9,4,6,1,0]])

# The example below will display a dataset consisting of boolaen for every value in all row
# of the first column
# print(matrix_C[:,0] > 2)

# To get an interger dataset rather than a boolaen, you wrap the matrix_C index in another
# matrix_c variable. The example below will display all value greater than 2 in a 1-d array.
# print(matrix_C[matrix_C[:] > 2])

# To add more than one condition, use the &(and) or |(or) and a parenthesis to separate both conditions
# The example below will display the values that are even and greater than 2 in a 1-d array
# print(matrix_C[(matrix_C[:] % 2 == 0) & (matrix_C[:] > 2)])


# SQUEEZE FUNCTION

# This helps to remove all unnescessary array. E.g Let us consider the below examples

matrix_D = np.array([[1,1,2,3,4], [4,1,3,7,2], [9,4,6,1,4]])

# This will display a single scalar value od 1. You can also verifies by checking the type
# print(matrix_D[0,0])

# This will display a vector of 1-d array of 1
# print(matrix_D[0,0:1])

# This will produce a matrix of 2-d array of 1
# print(matrix_D[0:1,0:1])

# So in order not to get a confusing output, we use the squeeze function. The queeze function gives 
# us an integer irrespective of whether we've sliced or not. Although, it's still an n-darray. e.g
# This helps us to access any value in the dataset easily
# The squeeze function can be used in 2 ways
# 1
print(matrix_D[0:1,0:1].squeeze())
# 2
print(np.squeeze(matrix_D[0:1,0:1]))



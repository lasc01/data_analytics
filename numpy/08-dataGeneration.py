import numpy as np
# The below are some functions that can be used to generate data quicly in numpy

# np.empty(): This helps to create an empty array. i.e return array without initializing
# enteries. e.g
array_empty = np.empty(shape = (2,3))
# print(array_empty)
# This returns an empty array

# np.zeros(): This create an array of 0s. e.g
array_0s = np.zeros(shape = (2,3), dtype="int")
# print(array_0s)

# np.ones(): This create an array of 1s. e.g
array_1s = np.ones(shape = (2,3), dtype="int")
# print(array_1s)


# np.ones(): This create an array filled with specified values, and contains
# an additional mandatory argument called fill_value. e.g
array_full = np.full(shape = (2,3), fill_value=3, dtype="int")
# print(array_full)


# LIKE FUNCTIONS
# In this case, we don't have to specify the shape of the array. Instead, we create an ndarray, then
# we use the like function to automatically take the shape of the created array. e.g

matrix_A = np.array([[3,4,5,6,2],[2,3,1,5,8],[1,6,2,1,4]])
# print(matrix_A)
array_empty_like = np.empty_like(matrix_A)
# this prints out an alike array with random numbers
# print(array_empty_like)

array_0s_like = np.zeros_like(matrix_A)
# this prints out an alike 
# print(array_0s_like)

array_full_like = np.full_like(matrix_A, fill_value=3)
# this prints out an alike 
print(array_full_like)

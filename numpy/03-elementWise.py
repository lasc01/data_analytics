import numpy as np

# elementwise simply means conducting mathematical computation to each element of an array

array_a = np.array([4,6,8])

array_b = np.array([[1,3,5],[7,9,11]])

# for example adding 2 to array_a or array_b will add 2 to every value in the array
# NB: Subtraction, multiplication and dividion also work like this 

# print(array_b + 2)

# We can add a 1-d array to a 2-d array by specifying the the indices of the 2-d array

# print(array_a + array_b[1])

# adding array_a and array_b directly without specifying the indices of the 2-d array will
# add up all value of array_a to array_b

print(array_a + array_b)
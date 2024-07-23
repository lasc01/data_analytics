import numpy as np

# The min function helps to determine the minimum value in an array
matrix_A = np.array([[2,0,2,0,3],[4,2,2,0,3],[3,2,1,2,1]])

print(matrix_A)

# To get the min value of the above array, check below. Note that you can also add all parameters
# such as axis and data type to get a mum specific resullt. e.g setting the axis to 0 should give
# you the minimum value of all columns
# print(np.min(matrix_A))
# print(np.min(matrix_A, axis=0))
# NB: amin() can also be used interchangeably with min(). They perform same function

# np.minimum() is quite different from that of np.min(). The minimum function always take two values
# and prints out two values. It compares the both values and print out the minima values between
# them. e.g
print(np.minimum(matrix_A[0], matrix_A[2]))

# The max syntax is actually the same as the minimum
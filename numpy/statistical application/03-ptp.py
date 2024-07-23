import numpy as np

# The ptp stands for peak to peak and it is a function that helps to determine the differnce betwwen
# maximum and minimum value in an array
matrix_A = np.array([[2,0,2,0,3],[4,2,2,0,3],[3,2,1,2,1]])

print(matrix_A)

# e.g the ptp function will give a result of of 9 from the array above, cause 9 is the max value while
# 0 is the min value. We can also use other parameter like axis and so on

print(np.ptp(matrix_A))
print(np.ptp(matrix_A, axis=0))
import numpy as np

# The percentile function returns the specific percentile of a given set. It requires a second input-
# the percentile(a value that is greater than the corresponding % of the dataset)
matrix_A = np.array([[2,0,2,0,3],[4,2,2,0,3],[3,2,1,2,1]])

print(matrix_A)

# to get the percentile of the above example, use the below. Note that it first arranges the numbers
# in ascending order before finding the percentile. the below will display 4 because 4 is because
# 4 becomes the last number after the dataset has been rearranged, therefore making it the 100th percentle
# 

print(np.percentile(matrix_A, 100))
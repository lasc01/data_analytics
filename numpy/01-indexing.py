import numpy as np

array_a = np.array([[1,2,3],[4,5,6]])

# NB: python uses zero indexing. Therefore, printing out [0] displays the first row
# print(array_a[0])

# to get the value of a particular single element, we need to specify both indices
# i.e the row and a column using double tuples. E.g The result of the below is 6

# print(array_a[1][2])

# Another way of getting the same result is using a comma to separate both indices in the same tuple

# print(array_a[1,2])

# To get just the column of the array, we use a method called slicing. Check e.g below

# print(array_a[:,1])

# NEGATIVE INDEXING
# This is the act of counting the index backward. Rather than starting from 0, negative index
# starts from -1 because there is no such thing as -0. E.g The below example will display
# 4,5,6 because it is the last row(element). [-2] will also display 1,2,3

print(array_a[-1])
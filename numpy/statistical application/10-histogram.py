import numpy as np
import matplotlib.pyplot as plt

# Histogram is a way to examine a dataset by dissecting it into density. i.e how many dataset fall
# within a pre-determined range. e.g 

matrix_A = np.array([[2,0,2,0,3],[4,2,2,0,3],[3,2,1,2,1]])
print(np.sort(matrix_A, axis=None))

# print(np.histogram(matrix_A))

# NB: The first result is the number of time a value occur in an interval.
# While the second result is the interval itself
# The interval can be determined by selecting bin as a parameter. If bin is set to 4, we get an interval
# of size 5. E.g

# print(np.histogram(matrix_A, bins=4))

# We can also specify the interval by selecting the range argument(be careful)

# print(np.histogram(matrix_A, bins=4, range=(1,3)))

# to display on a graph, import matplotlib and follow the below

plt.hist(matrix_A.flat, bins = np.histogram(matrix_A)[1])
print(plt.show)

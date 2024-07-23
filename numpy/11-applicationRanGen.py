import numpy as np
from numpy.random import Generator as gen
from numpy.random import PCG64 as pcg
# This is a test creation application of random data that is used to test how wel a program works in
# the absence of real data
array_RG = gen(pcg(seed = 22))

# Below is using different methods to generate a column of data with 1000 rows

array_column1 = array_RG.normal(loc=7, scale=2, size=1000)
array_column2 = array_RG.normal(loc=3, scale=1, size=1000)
array_column3 = array_RG.poisson(lam=2, size=1000)
array_column4 = array_RG.geometric(p=0.4, size=1000)
array_column5 = array_RG.exponential(scale=5, size=1000)

# the .transpose() method helps to switch the column to row and vice versa

random_test_data = np.array([array_column1,array_column2,array_column3,array_column4,array_column5]).transpose()

# to save the file on my local computer, use the below

np.savetxt("random_test_data.csv", random_test_data, fmt='%s', delimiter=',')

# print(random_test_data)

# to import the saved file back, use the below

my_random = np.genfromtxt('random_test_data.csv', delimiter=',')
print(my_random)
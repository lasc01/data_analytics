import numpy as np

# argwhere goes over an entire ndarray to check whether the individual element satisfy a given condition

lending_co_num = np.loadtxt('Lending-company-Numeric.csv', delimiter = ',')
# print(lending_co_num)

# this will print out all indexes of values in the array that is not 0 as the default conditin will
# only check for values different from 0.
# Note that the first column rep the row while the second column rep the column
# print(np.argwhere(lending_co_num))

# To get index of values that are 0, we just need to equate the data set to 0
# print(np.argwhere(lending_co_num == False))

# This is similar to slicing but this returns the co-ordinates rather than the actual value
# ÷It doesnt have a methd


# We can also use the argwhere to substitute values.
lending_co_num_NAN = np.genfromtxt('Lending-company-Numeric-NAN.csv', delimiter = ';')
# print(lending_co_num_NAN)

# print(np.isnan(lending_co_num_NAN).sum())

# print(np.argwhere(np.isnan(lending_co_num_NAN)))

# to check
# print(lending_co_num_NAN[11])

# To sustitute the nan values with 0 using iteration 
for i in np.argwhere(np.isnan(lending_co_num_NAN)):
    lending_co_num_NAN[i[0], i[1]] = 0

# to check
print(np.isnan(lending_co_num_NAN).sum())
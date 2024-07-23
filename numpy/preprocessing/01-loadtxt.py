import numpy as np

# PRE-PROCESSING
# This is the process of detecting missing values from a dataset
# The firs step to go about this is to load the data with the below function(np.loadtxt())

lend_com_num = np.loadtxt("Lending-company-Numeric.csv", delimiter=",")
# print(lend_com_num)

# We can then use another function to display the whether there is an NAN or not in the dataset
# In order t achieve this, we use the fuction (np.isnan.()). This will output true/false depending
# on whether there is an NAN in the dataset or not.

# print(np.isnan(lend_com_num))

# Checking every value one after the other to know if it's true or false can be straining. Therefore,
# we can use the (sum()) methos to get this mathematicallu.
# Recall the false = 0 and True = 1. Therefore, if we get 0 as the sum of the dataset, it means that
# no NAN data set, but if we get a number, it means there is an NAN depending on the output of the number

# print(np.isnan(lend_com_num).sum())



# Another example of a dataset wit nan
# Note that loadtxt()function will crash if used to load a data set that contains another data type aside
# an int or float. Therefore, we may have to use genfromtxt() to load the data set

lend_com_num_nan = np.genfromtxt("Lending-company-Numeric-NAN.csv", delimiter=";")
# print(lend_com_num_nan)
# print(np.isnan(lend_com_num_nan))
# print(np.isnan(lend_com_num_nan).sum())

# We have 260 missing values in the data set, we can fill them in by adding the (filling_values) parameter
# when importing the dataset
# But before ading the filling_values parameter, note that it is not adviseable to use 0 as the filling
# values because, 0 can happen to be in the dataset normally. Therefore it is adviseable to use values
# above or below the highest/lowest value of the dataset by using the .min/.max function.

temp_fill_val = np.nanmax(lend_com_num_nan).round(2) + 1
# print(temp_fill_val)

lend_com_num_nan = np.genfromtxt("Lending-company-Numeric-NAN.csv", delimiter=";", filling_values = temp_fill_val)
print(np.isnan(lend_com_num_nan).sum())



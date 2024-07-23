import numpy as np 

# Stacking is the act of placing multiple objects together to get a bigger object

# importing dataset with no nan
lending_com_num = np.loadtxt('Lending-company-Numeric.csv', delimiter = ",")
# print(np.isnan(lending_com_num).sum())

# importing data set with nan
lending_com_num_nan = np.genfromtxt('Lending-company-Numeric-NAN.csv', delimiter = ";")
# print(lending_com_num_nan)

temp_nan = np.nanmax(lending_com_num_nan).sum() + 1
# print(temp_nan)

temp_mean = np.nanmean(lending_com_num_nan, axis = 0).round(2)
# print(temp_mean)

lending_com_num_nan = np.genfromtxt('Lending-company-Numeric-NAN.csv', delimiter = ";", filling_values = temp_nan)
np.set_printoptions(suppress=True)
# print(lending_com_num_nan)

for i in range(lending_com_num_nan.shape[1]):
    lending_com_num_nan[:,i] = np.where(lending_com_num_nan[:,i] == temp_nan,
                                     temp_mean[i],
                                     lending_com_num_nan[:,i]
                                     )
    
# print(lending_com_num_nan)


# Back to stacking
# The example below stanck column 1 and 2 of the data set and display its transpose
# print(np.stack((lending_com_num_nan[:,0], lending_com_num_nan[:,1])))

# To get it displayed in the way you want, you have to specify the axis
# print(np.stack((lending_com_num_nan[:,0], lending_com_num_nan[:,1]), axis = 1))
# Note that the arrays must be in the same shape for you to stack them

# np.vstack(). vertical stack stacks 2 dataset on top of eachother to get a longer dataset.
# print(np.vstack((lending_com_num, lending_com_num_nan)))
# To confirm that it actually work, check the shape of the 2 stacked data set before and after stacking

# np.hstack(). horizontal stack stacks 2 dataset beside eachother to get a wide dataset.
# print(np.hstack((lending_com_num, lending_com_num_nan)))
# To confirm that it actually work, check the shape of the 2 stacked data set before and after stacking

# np.hstack(). depth stack stacks 2 dataset and return an array of higher dimension
print(np.dstack((lending_com_num, lending_com_num_nan)).shape)

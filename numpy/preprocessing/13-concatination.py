import numpy as np 

# concatenation is the act of linking object in a plane together

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


# Back to concatination
# Note that concatenation always have the same number of dimension for both input and output unlike stacking
#  e.g Let's try to concatinate the 1st and 2nd column of the data set with no nan.
# Since both are 1d array, the output will also be a 1-d array
# print(np.concatenate((lending_com_num[:,0], lending_com_num[:,1])))

# We can also concatenate a 2-d array of lending_com_num and ending_com_num_nan
print(np.concatenate((lending_com_num, lending_com_num_nan)))

# We can also select an axis to specify where the concatination happens(column or row). The default
# axis is set to 0(row). I.e they will be over each other


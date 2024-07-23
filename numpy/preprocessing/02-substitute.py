import numpy as np

# SUBSTITUTING MISSING VALUES
# This is the process of substituting NAN value with a reasonable number. Most times, we use the 
# mean of the column. E.g

lend_com_num_nan = np.genfromtxt("Lending-company-Numeric-NAN.csv", delimiter=";")
# print(lend_com_num_nan)

temp_mean = np.nanmean(lend_com_num_nan, axis=0).round(2)
print(temp_mean[0])

temp_nan = np.nanmax(lend_com_num_nan).round(2) + 1
print(temp_nan)

lend_com_num_nan = np.genfromtxt("Lending-company-Numeric-NAN.csv", delimiter=";", filling_values=temp_nan)
print(lend_com_num_nan.round(2))

# Using the np.where()function to substitute

# lend_com_num_nan[:,0] = np.where(lend_com_num_nan[:,0] == temp_nan,
#                                  temp_mean[0],
#                                  lend_com_num_nan[:,0]
#                                  )

# print(lend_com_num_nan)

# Now to do it for all column using loop. The .shape[1] indicates that we are dealing with columns

for i in range(lend_com_num_nan.shape[1]):
    lend_com_num_nan[:,i] = np.where(lend_com_num_nan[:,i] == temp_nan,
                                     temp_mean[i],
                                     lend_com_num_nan[:,i]
                                     )
    
print(lend_com_num_nan)

# We can also remoe all negative numbers in the same way

# for i in range(lend_com_num_nan.shape[1]):
#     lend_com_num_nan[:,i] = np.where(lend_com_num_nan[:,i] < 0,
#                                      0,
#                                      lend_com_num_nan[:,i]
#                                      )
    
# print(lend_com_num_nan)
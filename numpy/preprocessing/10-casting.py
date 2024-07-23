import numpy as np

# Casting is the act of creating array and storing the values of the original array with a new datatype

lending_co_num = np.loadtxt('Lending-company-Numeric.csv', delimiter = ',')[:6]
# print(lending_co_num)

# cast a dataset, we use the assign type method astype() method. e.g

# print(lending_co_num.astype(dtype=np.int32))

# Note that we can always change from one data type to anther
# The only exception is changing from string to int. This will result to an error message.
# Therefore, we have to change fro str to float, then back to int. e.g below

lending_co_num_str = lending_co_num.astype(dtype=np.str_)
# print(lending_co_num_str)

lending_co_num_float = lending_co_num_str.astype(dtype=np.float64)

# print(lending_co_num_float.astype(dtype=int))

# Another way of getting same result is to use the astype method twice in thesame line
print(lending_co_num_float.astype(dtype=np.float64).astype(dtype=np.int32))


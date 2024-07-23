import numpy as np

# Unique function takes an array as an input and create another array that contains all different
# values from the first one.

lend_com_num = np.loadtxt("Lending-company-Numeric.csv", delimiter=",")
# print(lend_com_num)

# print(np.unique(lend_com_num))
# This prints all values in the dataset in a 1-D array in increasing fashion

# Let us consider a dataset of string containing integers, uper-case and lower-case letters
example = np.array(['a1','A1','AA1','b1','B4','Bb6','c4'])
# print(np.unique(example))

# Note that the precedence of arrangement are as follows
# 1) Intergers
# 2) ASCII(upper-case > lower-case)
# 3) Alphabets

# To get how frequently the unique values occur, add the return_count argument to be True
print(np.unique(lend_com_num, return_counts = True))
import numpy as np

# argsort arranges the values of the data set in ascending order with their index

lending_com_num = np.genfromtxt('Lending-company-Numeric.csv', delimiter = ",")
# print(lending_com_num)

# print(np.argsort(lending_com_num))
# The output displayed indicates that column 1 is the lowest, folowed by 2, followed by 0, then 3 and so on

# We can also specify the axis just like we did for sort.

# We can also use this to arrange individual rows or columns. E.g
# print(np.argsort(lending_com_num[:,0]))

# The returned output indicates that the value with index 537 is the lowest value and so on
# This will produce a one dimensional aray ehich may not be too effective in the datset.
# To effect this in the data set, we need to store in a variabe

np.set_printoptions(suppress = True)

# The below will help re-arrange all successful values in the first position

lending_com_num = lending_com_num[np.argsort(lending_com_num[:,0])]
print(lending_com_num)

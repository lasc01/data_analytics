import numpy as np

# sorting is the act of arranging dataset in ascending order

lending_com_num = np.genfromtxt('Lending-company-Numeric.csv', delimiter = ",")
print(lending_com_num)

# print(np.sort(lending_com_num))
# Note that the default axis is set to -1 which mean it deal with column(backward). We can manually set
# it to 0 if we want to deal with rows
# print(np.sort(lending_com_num, axis = 0))

# To remove the return value fro displayng in scientific form, we can use the function below
np.set_printoptions(suppress = True)

# print(np.sort(lending_com_num, axis = 1))

# To arrange the dataset in descending order, put a minus sign before and inside the function. E.g
# print(-np.sort(-lending_com_num, axis = 1))

# We can also specify a particular column to be sorted
print (np.sort(lending_com_num[:,3]))

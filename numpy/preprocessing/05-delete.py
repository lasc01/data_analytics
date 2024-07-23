import numpy as np

# Deleting is the act of removing values from a data set

lending_com_num = np.genfromtxt('Lending-company-Numeric.csv', delimiter = ",")
print(lending_com_num)

# We can delete with the np.delete() function.
# Save it in a var if you are willing to use it late in the code

# print(np.delete(lending_com_num, 0))
# To compare
# print(np.delete(lending_com_num, 0).shape)
# print(np.size(lending_com_num))

# You can also delete an entire row or column by specifying the axis
# The below deletes the last row of the dataset
# print(np.delete(lending_com_num, -1, axis = 0))

# We can also remove multiple row/colums with a tupple or list
print(np.delete(lending_com_num, (1,2), axis = 1))

# We can also delete both columns and rows in the same line of code

print(np.delete(np.delete(lending_com_num, (1,2), axis = 1), (1,2), axis = 1))


import numpy as np

# RESHAPING IS THE ACT OF MORPHINGTHE SHAPE OF AN OBJECT A CERTAIN WAY

lending_com_num = np.genfromtxt('Lending-company-Numeric.csv', delimiter = ",")
# print(lending_com_num)

# In order to reshape this, we can simply use the reshape function or method(np.reshape() or .reshape(0))
# print(lending_com_num.shape)
print(np.reshape(lending_com_num, (6, 1043)))

# Not that the reshape function is different from the transpose function as the transpose function helps
# to switch rows to columns and vice versa

print(np.transpose(lending_com_num))
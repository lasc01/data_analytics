import numpy as np

array_a = np.array([[1,2,3], [4,5,6]])

# By assigning the 13 as the new value for the value in the second row and second column,
# the array changes the value of 5 to 13 instantlly
# array_a[1,1] = 13

# print(array_a)

# we can also assign an identical value to a vector of an array(row or column). E.g
# row
array_a[0] = 9
# colum
array_a[:,0]= 9
# print(array_a)

# To assign an unidentical value to a vector of an array, we'll need to use a list

list_a = [2,7,1]
list_b = [9,2,5]

array_a[0] = list_a
array_a[1] = list_b

print(array_a)
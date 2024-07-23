import numpy as np

# array_a = np.array([1,2,3])

# print(type(array_a))

# NB: Array is just the name of the function that produces an Ndarray. Ndarray is the object

# Arrays vs lists
# They are displayed in different ways. Array are displayes in tables. List are dispayed in a single line

list_a = [[1,2,3],[4,5,6]]

array_a = np.array(list_a)

# print(list_a)

# print(array_a)

# Arrays perform computatinal methods. List doesn't

list_b = list_a[0] + list_a[1]
array_b = array_a[0] + array_a[1]

# print(list_b)
# print(array_b)

# Array uses built in numpy functions and methods. E.g. List will have to impot the maths function

print(np.sqrt(array_a[1,0]))


# LIST VS OBJECT VS NUMBER

Lending_co_lt = np.genfromtxt("lending-co-LT.csv", delimiter=",", dtype="object")

print(Lending_co_lt)
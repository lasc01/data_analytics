import numpy as np

# arange() is a way of generating non-random sequence of number e.g

array_rng = np.arange(38)
# print(array_rng)

# we can also specify where the range starts, stops, and the steps also just like in the case of 
# indexing. You can also select the data type

array_rng_2 = np.arange(start=1, stop=30, step=2.2, dtype='int')
print(array_rng_2)
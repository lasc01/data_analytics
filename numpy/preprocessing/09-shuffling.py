import numpy as np

# Suffling is the rearrangement of the parts of a dataset

lending_co_num = np.loadtxt('Lending-company-Numeric.csv', delimiter = ',')[:6]
# print(lending_co_num)

# to get a shuffled dataset of the first 6 rows
np.random.shuffle(lending_co_num)
# print(lending_co_num)

# Another way of using the shuffle is by importing it from numpy in the beginning of our code
from numpy.random import shuffle

shuffle(lending_co_num)
# print(lending_co_num)

# We can also use the shuffle in random generated data
from numpy.random import Generator as gen
from numpy.random import PCG64 as pcg

array_rd = gen(pcg())
array_rd.shuffle(lending_co_num)
print(lending_co_num)

# NB A shuffle prevails over the use of seeds
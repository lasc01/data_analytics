import numpy as np
from numpy.random import Generator as gen
from numpy.random import PCG64 as pcg

array_RG = gen(pcg())
# The below will genereate a random value 
# print(array_RG.normal())

# We can also specify the number of values that we want by specifying the size. 
# e.g below will gener8 a 1d array 0f 5 random values
# print(array_RG.normal(size = 5))

# The below example will create a 2d array of 4 by 3
# print(array_RG.normal(size=(3,4)))

# The issue with the examles above is that they keep generating new set of values which will alter our
# models and make it impossible to work with. Therefore, we have to add a seed to the pcg. 
# This ensures we get the same set of value everyting we call the function
# NB: We must reset the seed everytime we want to use it
array_RG = gen(pcg(seed = 22))
# print(array_RG.normal(size=(3,4)))


# .integers()
# We can also generate set of integers of certain range  using the .integers function. e.g

array_int = gen(pcg(seed = 22))
# print(array_RG.integers(10, size=(3,4)))
# The example above will print out a 2d array with a set of integers between 0-9
# We can also specify the range with low and high below
# print(array_RG.integers(low=10, high=15, size=(3,4)))

# .random
# We can also generate set of PROBABILITY using the .random function. e.g

array_prob = gen(pcg(seed = 22))
# print(array_prob.random(size=(3,4)))


# .choice()
# This helps us generate a matrix by specifying a list of numbers

array_choice = gen(pcg(seed = 22))
# print(array_choice.choice([1,2,3,4,5], p = [0.2,0.1,0.2,0.4, 0.1], size=(3,4)))

# NB: We can manually set the probability for each value in the choice by creating a p list
# 1)the list in p must have the length as the choice list
# 2)the sum of the value of p must be equal to 1


# .poisson()
# The poisson distribution explains how over a fixed interval period of time, distance, or space,
# we expect an event to only occur once.

array_poi = gen(pcg(seed = 22))
# print(array_poi.poisson(lam = 10, size=(3,4)))


# .binomial
# The binomial distribution measures how many times a certain outcome can appear over a series of trials
# where there are only 2 possible outcomes. binomial method require 2 parameter, n and p. Where n is
# the number of trials and p(0-1) is the probability ofgetting the desire outcome

array_bino = gen(pcg(seed = 22))
# print(array_bino.binomial(n=100, p=0.5, size=(3,4)))

# .logistic
# This is similar to the binomial aside the parameteer and the dtype outcome(float)

array_logi = gen(pcg(seed = 22))
print(array_logi.logistic(loc=10, scale=0.2, size=(3,4)))

# other methods that can be used with the gen and pcg generator can be found in the numpy doc

time = 1,3, 12
products = ['product A', 'product B']

print('Expected sales for a period of {} month(s) for {}:'.format(time[1], products[1]))

# There are 2 parameters used in the format method. The 1st is the position
# Just like in the example above, python helps with the default position
# i.e the first {} will be 0, the 2nd will be 1 and so on, but we can also
# decide to position it ourselves

# print('Expected sales for {1} is for {0} month(s):'.format(time[1], products[1]))

# The keyward parameter is the second
# this is done by assigning a keyword or a variable to another variable in the
# format method. This is the mostly used method

# print('Expected sales for a period of {tim[1]} month(s) for {prod[1]}:'.format(tim =time, prod = products))


companies = ['Company A', 'Company B']
quarter = [1, 2, 3, 4]
sales_performance_prediction = ['increase', 'decrease', 'remain the same'] 
print("{com[1]} expects their next year's sales of Q{quart[3]} to {sales_perf[2]}.".format(com = companies, quart = quarter, sales_perf = sales_performance_prediction))

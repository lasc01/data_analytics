import numpy as np

np.set_printoptions(suppress=True, linewidth=200, precision=2)
# Suppress stops numpy from using scientific notation
# number of character on a line is set to 100 with linewidth
# precision displays characters in 2 dp

loan_data = np.genfromtxt("loan-data.csv", delimiter = ";", 
                          encoding='latin-1', skip_header = 1, 
                          autostrip = True, 
                          )
# delimeter helps numpy to know the separator used in the dataset
# encoding specifies the character encoding to be used when reading the CSV file.
# skip_header helps to skip the first row(usually the header)
# autostrip removes excess white space 
# print(loan_data)

# To check the numbers of missing values
# print(np.isnan(loan_data).sum())

temp_nan = np.nanmax(loan_data) + 1
# print(temp_nan)

temp_mean = np.nanmean(loan_data, axis = 0)
# print(temp_mean)

loan_data = np.genfromtxt("loan-data.csv", delimiter = ";", 
                          encoding='latin-1', skip_header = 1, 
                          autostrip = True, 
                        #   filling_values = temp_nan
                          )
# print(loan_data)

temp_stat = np.array([np.nanmin(loan_data, axis = 0),
                      temp_mean,
                      np.nanmax(loan_data, axis = 0)
                      ])
# print(temp_stat)

# To split the strings from the numbers in the dataset, we introduce argwhere to know where we have
# integers and strings

# This locates the string values with nan.
column_string = np.argwhere(np.isnan(temp_mean)).squeeze()
# print(column_string)

# This locates the numeric values with nan.
column_numeric = np.argwhere(np.isnan(temp_mean) == False).squeeze()
# print(column_numeric)


# To re-import the dataset, we use the usecols parameter

# for the strings
loan_data_strings = np.genfromtxt("loan-data.csv", delimiter = ";", 
                          encoding='latin-1', skip_header = 1, 
                          autostrip = True, 
                          filling_values = temp_nan,
                          usecols = column_string,
                          dtype = np.str_
                          )
# print(loan_data_strings)

# for numeric data
loan_data_numeric = np.genfromtxt("loan-data.csv", delimiter = ";", 
                          encoding='latin-1', skip_header = 1, 
                          autostrip = True, 
                          filling_values = temp_nan,
                          usecols = column_numeric,
                          )
# print(loan_data_numeric)


# Name the columns
# use skkip_footer instead of skip head

header_full = np.genfromtxt("loan-data.csv", delimiter = ";", 
                          encoding='latin-1', 
                          skip_footer = loan_data.shape[0], 
                          autostrip = True, 
                          dtype = np.str_
                          )
# print(header_full)

header_strings = np.genfromtxt("loan-data.csv", delimiter = ";", 
                          encoding='latin-1', 
                          skip_footer = loan_data_strings.shape[0], 
                          usecols = column_string,
                          autostrip = True, 
                          dtype = np.str_
                          )
# print(header_strings)

header_numeric = np.genfromtxt("loan-data.csv", delimiter = ";", 
                          encoding='latin-1', 
                          skip_footer = loan_data_numeric.shape[0], 
                          usecols = column_numeric,
                          autostrip = True, 
                          dtype = np.str_
                          )
# print(header_numeric)

# The shorter method to get header_string and header_numeric is below

header_strings, header_numeric = header_full[column_string], header_full[column_numeric]
# print(header_strings)
# print(header_numeric)


# CHECKPOINT
# Checkpoint are places through out our code where we store a copy of dataset(or part of it).

def checkpoint(file_name, checkpoint_header, checkpoint_data):
    np.savez(file_name, header = checkpoint_header, data = checkpoint_data)
    checkpoint_variable = np.load(file_name + ".npz")
    return (checkpoint_variable)

checkpoint_test = checkpoint("checkpoint-test", header_strings, loan_data_strings)

# print(checkpoint_test['header'])
# print(checkpoint_test['data'])

# To check
# print(np.array_equal(checkpoint_test['data'], loan_data_strings))


# Manipulating Text data
# In this phase, we will be manipulating the columns with strings.

# 1) issue_d
# We first rename the header issue_d to issue date
header_strings[0] = 'issue_date' 
# To check
# print(header_strings)
# We now work on the data of the issue date column. We first check the columm below
# print(loan_data_strings[:,0])
# We use the unique function to check all values in that column
# print(np.unique(loan_data_strings[:,0]))
# Note that there is an empty string in the beginning, which indicates a missing data
# Also note that the values are arranged in alphabetical order
# We notice that they are have the same year in common, so we can strip the year off 
np.chararray.strip(loan_data_strings[:,0], "-15")
# Save it in a loan_data_strings[:,0] in order to overwrite the actual data
loan_data_strings[:,0] = np.chararray.strip(loan_data_strings[:,0], "-15")
# print(np.unique(loan_data_strings[:,0]))

# Now, we represent the month values as integers in order to save memory.
months = np.array(['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])

for i in range(13):
    loan_data_strings[:,0] = np.where(loan_data_strings[:,0] == months[i],
                                      i,
                                      loan_data_strings[:,0]
                                      )
# print(np.unique(loan_data_strings[:,0]))


# 2)loan_status
# checking all the data in the loan_status column using the unique function
# print(np.unique(loan_data_strings[:,1]))
# In case of a very large data set, to get the total number of unique values, we use the size attribute
# print(np.unique(loan_data_strings[:,1]).size)

# In this case, we treat the data as either good or bad based on the economy situation of loan applicants
# NB: an empty data is usually treated with the worse case scenerio. Therefore, it is bad
# 1 reps good and 0 reps bad

bad_loan = np.array(['', 'Charged Off', 'Default', 'Late (31-120 days)'])

# Then we use the np.isin() function to check whether the values of bad_loan is in loan_data_strings,
# then, we use to where to rep 0 if it is there and 1 if it is not

loan_data_strings[:,1] = np.where(np.isin(loan_data_strings[:,1], bad_loan), 0, 1)

# print(np.unique(loan_data_strings[:,1]))


# 3) term
# print(header_strings)
# print(np.unique(loan_data_strings[:,2]))
# since the column has " months" in common, we first strip it off all data in the column

loan_data_strings[:,2] = np.chararray.strip(loan_data_strings[:,2], " months")
# print(np.unique(loan_data_strings[:,2]))

# rename the term to term-month, so we can know the term is in months
header_strings[2] = "term_months"
# print(header_strings)

# Now, we represent the empty space with the worst case which is 60 months using where() function

loan_data_strings[:,2] = np.where(loan_data_strings[:,2] == '', 60, loan_data_strings[:,2])

# print(np.unique(loan_data_strings[:,2]))
# Note that in most cases where we have only 2 unique values, we tend to use 0 and 1 to represent
# them, but in this case we will leave it for understanding case


# 4) grade & sub_grade
# print(header_strings)
# print(np.unique(loan_data_strings[:,3]))
# print(np.unique(loan_data_strings[:,4]))
# We notice both are similar, except that the sub_grade has numbers in its strings
# The grade column should be scrap in theory, since we have all the values there in sub_grade, but
# because we want to substitute a missing value in the sub_grade with the potential highest value
# of that grade. 
# E.G If the miss value in the sub_grade is within grace C, we substitute it with the highest possible
# value in C which is C5. This is achieved with the below

for i in np.unique(loan_data_strings[:,3])[1:]:
    loan_data_strings[:,4] = np.where((loan_data_strings[:,4] == '') & (loan_data_strings[:,3] == i),
                                      i + '5',
                                      loan_data_strings[:,4]
                                      )

# print(np.unique(loan_data_strings[:,4]))
# We still get an empty string because there are values that still don,t meet the conditions st above.
# Now, to check the number of missing value we have, we use the return_counts parameter

# print(np.unique(loan_data_strings[:,4], return_counts = True))
# From the above, we can see that we have 9 missing data
# Let us now represent this missing data with the worst possible outcome than G5, which is H1

loan_data_strings[:,4] = np.where(loan_data_strings[:,4] == '',
                                    'H1',
                                    loan_data_strings[:,4]
                                      )
# print(np.unique(loan_data_strings[:,4]))

# Now that we have no more missing value in the sub_grade, we can now remove the grade column

loan_data_strings = np.delete(loan_data_strings, 3, axis = 1)
# print(loan_data_strings[:,3])

# to delete the header also
header_strings = np.delete(header_strings, 3,)
# print(header_strings[3])

# To convert the sub_grade values to integers using dictionaries

# print(np.unique(loan_data_strings[:,3]).size)

key = list(np.unique(loan_data_strings[:,3]))
values = list(range(1, np.unique(loan_data_strings[:,3]).shape[0] + 1))
dict_sub_grade = dict(zip(key, values))

# print(dict_sub_grade)

for i in np.unique(loan_data_strings[:,3]):
    loan_data_strings[:,3] = np.where(loan_data_strings[:,3] == i,
                                      dict_sub_grade[i],
                                      loan_data_strings[:,3]
                                      )
# print(np.unique(loan_data_strings[:,3]))


# 5) Verification Status
# print(header_strings)
# print(np.unique(loan_data_strings[:,4]))

# We use a similar to the loan_status. '' and 'Not Verified' are stored in a variable.
# The we use the where and isin function to replace unrerified with 0 & verified with 1

# unverified = np.array(['', 'Not Verified'])

# loan_data_strings[:,4] = np.where(np.isin(loan_data_strings[:,4], unverified), 0, 1)

# Asorter way of getting thesame result using just the np.where function is to use the | operato
loan_data_strings[:,4] = np.where((loan_data_strings[:,4] == '') | (loan_data_strings[:,4] == 'Not Verified'),
                                  0,
                                  1
                                  )

# print(np.unique(loan_data_strings[:,4]))


# 6) URL
# print(loan_data_strings[:,5])

# Note that we there is a common value in all the column, so we can strip it off
loan_data_strings[:,5] = np.chararray.strip(loan_data_strings[:,5], 'https://www.lendingclub.com/browse/loanDetail.action?loan_id=')
# print(loan_data_strings[:,5])

# The remaining part looks to be equal with our first column(id) but they have different data type
# print(loan_data_numeric[:,0])

# print(np.array_equal(loan_data_strings[:,5].astype(dtype = np.int32), loan_data_numeric[:,0].astype(dtype = np.int32)))

# Since they are similar, then there is no point keepin the column anymore because they share the same
# information. Therefore, we can delete the URL column

loan_data_strings = np.delete(loan_data_strings, 5, axis = 1)
header_strings = np.delete(header_strings, 5)

# print(header_strings)


# 7) State Address
# print(header_strings)
# First rename the header ro state_address
header_strings[5] = "state_address"
# print(header_strings)
# check the unique values
# print(np.unique(loan_data_strings[:,5]))
# To check how many times each state appear
# print(np.unique(loan_data_strings[:,5], return_counts = True))
# But all states are arranged in alphabetical order. And we want it to be arranged in order of how
# most each state appear
# This can be achieved using the argsort function. But firstly, we save the abouve in 2 variables
state_name, state_counts = np.unique(loan_data_strings[:,5], return_counts = True)
state_counts_sorted = np.argsort(-state_counts)
# The minus sign indicate that we are sorting in decreasing order
# print(state_name[state_counts_sorted], state_counts[state_counts_sorted])

# To take care of the missing 500 values, we substitute with 0
loan_data_strings[:,5] = np.where(loan_data_strings[:,5] == '', 0, loan_data_strings[:,5])

# print(np.unique(loan_data_strings[:,5]))

# To breakdown the data for easier analysis, we can group the states into geographical zone

state_west = np.array(['WA','OR','CA','NV','ID','MT','WY','UT','CO','AZ','NM','HI','AK'])
state_south = np.array(['TX','OK','AR','LA','MS','AL','GA','FL','SC','TN','NC','KY','WV','VA','MD','DC','DE'])
state_midwest = np.array(['ND','SD','NE','KS','MN','IA','MO','IL','WI','IN','OH','MI'])
state_east = np.array(['PA','NJ','NY','ME','NH','VT','MA','CT','RI'])

# To substitute each geographical zone with number
loan_data_strings[:,5] = np.where(np.isin(loan_data_strings[:,5], state_west), 1, loan_data_strings[:,5])
loan_data_strings[:,5] = np.where(np.isin(loan_data_strings[:,5], state_south), 2, loan_data_strings[:,5])
loan_data_strings[:,5] = np.where(np.isin(loan_data_strings[:,5], state_midwest), 3, loan_data_strings[:,5])
loan_data_strings[:,5] = np.where(np.isin(loan_data_strings[:,5], state_east), 4, loan_data_strings[:,5])

# print(np.unique(loan_data_strings[:,5]))



# Now, we need to convert all the strings that looks like integers into proper integers with the astype function
# print(loan_data_strings.astype(np.int32))

# Now we need to save this by overwriting using same variable

loan_data_strings = loan_data_strings.astype(np.int32)

# print(loan_data_strings)


# Checkpoint2
# Since we already have a checkpoint defined up, we just need to call it, and change the file name to a distinct name

checkpoint_string = checkpoint("checkpoint-string", header_strings, loan_data_strings)

# print(checkpoint_string['header'])
# print(checkpoint_string['data'])

# In order to be sure that we have the same data saved in the checkpoint
# print(np.array_equal(checkpoint_string['data'], loan_data_strings))



# Manipulating numeric data
# In this phase, we will be manipulating the columns with numbers.

# Firstly, to check if there is any missing data here
# print(np.isnan(loan_data_numeric).sum())
# This returns a 0, which indicate that their are no missing values there.
# But recall that we,ve filled all missing value with temp_nan
# But now, we have to substitute those missing values with the worst possible values rather than temp_nan

# Firstly, let us check the headers of the numeric data
# print(header_numeric)

# The first column to work on is the ID
# To check if there is no data that was replaced with the temp_nan value

# print(np.isin(loan_data_numeric[:,0], temp_nan).sum())
# We get 0. Therefore, no value in the ID column was replaced

# For the other columns, we observe that the only column that will have the min value as the worst 
# outcome is the "funded_amt"
# Recall that we stored the min, mean and max valuues in a variable called "temp_stat"

# print(temp_stat)
# But we are not interested in the nan values, therefore, we select only the numeric values using the below
# print(temp_stat[:, column_numeric])

# 3) funded_amt

# print(loan_data_numeric[:,2])

loan_data_numeric[:,2] = np.where(loan_data_numeric[:,2] == temp_nan,
                                  temp_stat[0, column_numeric[2]],
                                  loan_data_numeric[:,2]
                                  )
# print(loan_data_numeric[:,2])

# 4) loan_amnt, int_rate, installment, total_pymnt
# We will be filling all these column with the max possible value using temp_stat
# print(header_numeric)

for i in [1,3,4,5]:
    loan_data_numeric[:,i] = np.where(loan_data_numeric[:,i] == temp_nan,
                                      temp_stat[2, column_numeric[i]],
                                      loan_data_numeric[:,i]
                                      )
# print(loan_data_numeric[:,1])
# print(loan_data_numeric[:,3])
# print(loan_data_numeric[:,4])
# print(loan_data_numeric[:,5])


# Currency conversion
# Firstly, we import the exchange rate csv file into a variable

EUR_USD = np.genfromtxt('EUR-USD.csv', delimiter = ',', autostrip = True, dtype = np.str_)
# print(EUR_USD)

# We have 5 columns
# 1) open column is the exchange rate at the beginning of the day
# 2) high column is the highest exchange rate of the day
# 3) low column is the lowest exchange rate of the day
# 4) close column is the exchange rate at the end of the day
# 5) volume column is the number of transanction made in a day. Usually 0

# We usually use the close column, which is the fourth column

# Since we now already know the column to work with, we can now skip the header & usecols = 3
EUR_USD = np.genfromtxt('EUR-USD.csv', delimiter = ',', autostrip = True, skip_header = True, usecols = 3)
# print(EUR_USD)

# Now, we have 12 exchange rate for the 12 months we have.
# Recall that we already have a column for all the months in column 0 of the load_column_strings
# Now, let's save the string in a new variable since we are going to alter some things

exchange_rate = loan_data_strings[:,0]
# print(exchange_rate)

# Now, let us link each month to its exchange rate using a for loop
for i in range(1,13):
    exchange_rate = np.where(exchange_rate == i,
                             EUR_USD[1-i],
                             exchange_rate
                             )
    exchange_rate = np.where(exchange_rate == 0,
                             np.mean(EUR_USD),
                             exchange_rate
                             )
# print(exchange_rate)

# Note that the reason why we used EUR_USD[1-i] is because we only have 12 exchange rates for the 12 months
# Recall that we have used 0 to represent missing month. So we technocally have 13 months.
# So january exchange rate is the first value in the EUR_USD which has an index of 0
# We now created another where() function for the missing month with index 0 to be equal to the mean
# of the exchange rate. Which will give a value of 1.1

# Now, we need to add this data to the dataset we have 
# To do this, they must have compatible shape. To check
# print(exchange_rate.shape)
# print(loan_data_numeric.shape)

# Exchange rate is 1d while loan_data_numeric is 2d, which means that we will have to reshape exchange_rate
exchange_rate = np.reshape(exchange_rate, (10000,1))
# print(exchange_rate.shape)

# Now, to horizontally stack exchange_rate to the load_data_numeric data set
# overwrite loan_data_numeric 
loan_data_numeric = np.hstack((loan_data_numeric, exchange_rate))
# print(loan_data_numeric)
# Now, to horizontally stack 'exchange_rate' to the header_numeric data set
# overwrite header_numeric 
header_numeric = np.hstack((header_numeric, np.array(['exchange_rate'])))
# print(header_numeric)

 

# Converting other columns in USD to EUR
# print(header_numeric)
# Viewing the header_numeric, we'll discover that there are 4 columns in USD that needs to be converted
# to EUR: 'loan_amnt' 'funded_amnt' 'installment' 'exchange_rate'. In order to save ourselves the
# sress of converting the columns one after another, we can save all their indices in a variable
column_dollars = np.array([1,2,4,5])
# Now, we can now call the loan_data_numeric for just the four columns

# print(loan_data_numeric[:,column_dollars])

# Now, we can have the data of the just the 4 columns we want to work with.
# Now, we can loop through the column_dollars and horizontally stack each column's the conversion rate
# at the end of the loan_data_numeric

for i in column_dollars:
    loan_data_numeric = np.hstack((loan_data_numeric, 
                                  np.reshape(loan_data_numeric[:,i] / loan_data_numeric[:,6], (10000,1)
                                  )))
                             
# The loan_data_numeric is in 2d, while the conversion is in 1d, therefor we get an error
# We therefore need to reshape the conversion (1000,1)

# print(loan_data_numeric)
# We'll discover that the exchange_rate is no longer the last column. This is because the 4 converted columns
# have been stacked beside it
# print(loan_data_numeric.shape)

# Now, to name the header of the 4 columns in the column_dollars

header_addition = np.array([column_name + "_EUR" for column_name in header_numeric[column_dollars]])
# This code will add _EUR to every column name in header_numeric with indexes column_dollars
# print(header_addition)

# To add the newly named headers to header numeric 

header_numeric = np.concatenate((header_numeric, header_addition))
# print(header_numeric)

# To also rename the loan_amnt' 'funded_amnt' 'installment' 'exchange_rate' by adding _USD 

header_numeric[column_dollars] = np.array([column_name + "_USD" for column_name in header_numeric[column_dollars]])
# print(header_numeric)

# To arrange our columns proprerly so that the conversion in USD & EUR can be beside each other

column_index_order = [0,1,7,2,8,3,4,9,5,10,6]

header_numeric = header_numeric[column_index_order]
# print(header_numeric)

# To also do it to the loan_data_numeric
loan_data_numeric = loan_data_numeric[:, column_index_order]
# print(loan_data_numeric)


# INTEREST RATE
# The only column that we are left to alter is the interest rate. And it is in percentage
# To make our qork easier, we need to convert it to quantile. To achieve this

# print(header_numeric)

loan_data_numeric[:,5] = loan_data_numeric[:,5]/100
# print(loan_data_numeric[:,5])


# CHECKPOINT 2

checkpoint_numeric = checkpoint("checkpoint-numeric", header_numeric, loan_data_numeric)

# print(checkpoint_numeric['header'])
# print(checkpoint_numeric['data'])


# Finalizing the Dataset
# Now, we have to stack the loan_data_numeric_ and the loan_data_string back together
# Note that it is best advised to use the checkpoint to achieve this

loan_data = np.hstack((checkpoint_numeric['data'], checkpoint_string['data']))
# print(loan_data)
# To confirm
# print(loan_data.shape)
# print(checkpoint_numeric['data'].shape)
# print(checkpoint_string['data'].shape)
# To check if we still have missing values
# print(np.isnan(loan_data).sum())

# To concatenate the header also 
header_full = np.concatenate((checkpoint_numeric['header'], checkpoint_string['header']))

# print(header_full)


# Sorting the new dataset
loan_data = loan_data[np.argsort(loan_data[:,0])]
# print(loan_data)
# print(np.argsort(loan_data[:,0]))

# Vertically stack the header_full data to the loan_data
loan_data = np.vstack((header_full, loan_data))
# print(loan_data)
# Note that all the datatype will now be string as the vstack automatically takes the datatype
# witht the least memory size. This is the string in this case

# Saving the dataset

np.savetxt('loan_data_preprocessed.csv', 
           loan_data, 
           fmt = '%s', 
           delimiter = "," 
           )

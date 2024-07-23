import pandas as pd

# pd.set_printoptions(suppress=True, linewidth=200, precision=2)

raw_data = pd.read_csv('Absenteeism-data.csv', 
                       delimiter = ',')

# The first step is to create a copy of the raw data in ordr not to tamper with the raw data

df = raw_data.copy()

# In order to display the whole content of the dataset, we can use
# pd.options.display.max_columns = None
# pd.options.display.max_rows = None

# print(df)

# We can also get the info about the dataset using the info method
# print(df.info())


# Time to preprocess each column of the dataset
# 1) ID

# The ID column is just a set of numbers that represents each enployee. It doesn't help with our
# analysis in any way. Hence, needs to be dropped

df = df.drop(['ID'], axis = 1)
# print(df)

# 2) Reason for Absence
# We can check all the distinct values in this column using the unique method
# print(pd.unique(df['Reason for Absence']))

# We can also get the minimum and maximum number in the column using the min() and max() method
# print(df['Reason for Absence'].min())
# print(df['Reason for Absence'].max())

# We can also find the number of unique values in the column using the len() function
# print(len(df['Reason for Absence'].unique()))

# From the result above, we can deduce that there are 28 unique values in between 0 & 28.
# This means that there is one missing value between 0 & 28
# We can check the value by first sorting the unique values

# print(sorted(pd.unique(df['Reason for Absence'])))

# Fom the above, we can deduce that the missing value is the number 20

# Creating a dummy for the reason for absence column using the get_dummy() function
reason_columns = pd.get_dummies(df['Reason for Absence'])
# print(reason_columns)

# To confirm whether each employees has only 1 reason for absence 
reason_columns['check'] = reason_columns.sum(axis=1)
# print(reason_columns['check'])
# The expected result should print out 1 in a new check column
# To confirm that they are all 1
# print(reason_columns['check'].unique())

# To confirm the reason_columns['check'] vertically
reason_columns['check'] = reason_columns.sum(axis=0)
# print(reason_columns)

# Convert the boolean values to integers (0s and 1s)
# Fill NA values with 0 before converting to integers
reason_columns = reason_columns.fillna(0).astype(int)

# We can now remove the check column

reason_columns = reason_columns.drop(['check'], axis=1)
# print(reason_columns)

# In order to drop the first column in the newly crated data frame reason_columns

reason_columns = pd.get_dummies(df['Reason for Absence'], drop_first = True).fillna(0).astype(int)
# print(reason_columns)
# print(reason_columns.columns.values)

# Grouping the reason for absence column
# We can classify the reasons into 4 groups(diseases(1-14), pregnancy(15-17), medical emergency(18-21), minor reasons(21-28))
# Firstly, let us drop reason for absence column

df = df.drop(['Reason for Absence'], axis = 1)
# print(df)

# Secondly, We can therefore create a dataframe for each group
reason_type_1 = reason_columns.loc[:,1:14].max(axis = 1)
reason_type_2 = reason_columns.loc[:,15:17].max(axis = 1)
reason_type_3 = reason_columns.loc[:,18:21].max(axis = 1)
reason_type_4 = reason_columns.loc[:,22:].max(axis = 1)
# The max methods used behind is to check if every individual has more than 1 reason. The ideal max
# number of each column should be 1
# print(reason_type_1)
# print(reason_type_2)
# print(reason_type_3)
# print(reason_type_4)

# thirdly,we can concatinate the reason type into the dataframe back

df = pd.concat([df, reason_type_1, reason_type_2, reason_type_3, reason_type_4], axis = 1)
# print(df)

# Now, we need to replace the column names 0,1,2,3 to a more relatable name
# To first get all the column names
# print(df.columns.values)
# Then we can store the list in a variable

column_names = ['Date', 'Transportation Expense', 'Distance to Work', 'Age',
 'Daily Work Load Average', 'Body Mass Index', 'Education', 'Children', 'Pets',
 'Absenteeism Time in Hours', 'Reason_1', 'Reason_2', 'Reason_3', 'Reason_4']

# Save the variable as the default df column names

df.columns = column_names
# print(df.columns.values)

# To reorder the column names and arrange it back to the default arrangement of the dataset 
column_names_reorder = ['Reason_1', 'Reason_2', 'Reason_3', 'Reason_4', 'Date', 'Transportation Expense', 'Distance to Work', 'Age',
 'Daily Work Load Average', 'Body Mass Index', 'Education', 'Children', 'Pets',
 'Absenteeism Time in Hours']
df = df[column_names_reorder]
# print(df)


# CHECKPOINT_1
df_checkpoint_1 = df[column_names_reorder]
# print(df_checkpoint_1) 


df_reason_mod = df.copy()
# print(df_reason_mod)


# Date
# The next column to work on is the date
# print(df_reasobn_mod.columns)
# print(df_reason_mod['Date'])

# To get the datatype of the column
# print(type(df_reason_mod['Date']))

# To get the data type of individual values in the column
# print(type(df_reason_mod['Date'][0]))
# It shows that it is a strings

# We need to convert this strings to timestamp(data type used for date and time)

df_reason_mod['Date'] = pd.to_datetime(df_reason_mod['Date'], format = '%d/%m/%Y')
# print(df_reason_mod['Date'])

# Now, in order to confirm that it has been adjusted, we can check the type once again
# print(type(df_reason_mod['Date'][0]))
# print(df_reason_mod['Date'][0])

# To now extract the month value

# print(df_reason_mod['Date'][0].month)
# Note that the convention for the month in this library is 1 - 12, rather than the usual programming 0 - 11
# create an empty list month
list_month = []
# use a for loop to append df_reason_mod into list_month
# print(df_reason_mod.shape)
for i in range(df_reason_mod.shape[0]):
    list_month.append(df_reason_mod['Date'][i].month)

# print(list_month)
# print(len(list_month))

# We can now add the newly created list to a column in a our df_reason_mod dataset

df_reason_mod['Month Value'] = list_month
# print(df_reason_mod.head())


# To now extract the day value
print(df_reason_mod['Date'][699].weekday())
# Note that the convention for the month in this library is 0 - 6, rather than the month convention(0-monday, 1-tuesday....)
# create an empty list month
list_weekday = []
# use a for loop to append df_reason_mod into list_month
# print(df_reason_mod.shape)
for i in range(df_reason_mod.shape[0]):
    list_weekday.append(df_reason_mod['Date'][i].weekday())

# print(list_weekday)

df_reason_mod['Weekday Value'] = list_weekday
# print(df_reason_mod.head())


# print(df_reason_mod.columns)
# The following columns won't be manipulated 'Transportation Expense', 'Distance to Work', 'Age',
# 'Daily Work Load Average', 'Body Mass Index'.


# Education column
# using unique method to get the total numner of unique values in the education column
# print(df_reason_mod['Education'].unique())
# (1 means high school grad, 2 is draduate, 3 is postgrad, 4 is msc or bsc)

# In order to know how many times each unique value appear in the dataset, we use
# print(df_reason_mod['Education'].value_counts())

# Now, we want to divite the column into just non-graduate and graduate(0 & 1). non-grad are just the
# high school grad while grad are from grad to phd
# We can use the map method to achieve this

df_reason_mod['Education'] = df_reason_mod['Education'].map({1:0, 2:1, 3:1, 4:1})

# To confirm the above code has worked by using the unique and valu_count method once again
print(df_reason_mod['Education'].unique())
print(df_reason_mod['Education'].value_counts())

# print(df_reason_mod)


# FINALCHECKPOINT
df_cleaned = df_reason_mod.copy()
print(df_cleaned)

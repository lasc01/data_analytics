import pandas as pd

data = pd.read_csv('Lending-company.csv', index_col= 'StringID')
Lending_data = data.copy()

# print(Lending_data.head())

# to access a particular column
# print(Lending_data.head().CustomerGender)
# or   Note that below is a more acceptable syntax
# print(Lending_data['Location'])

# Note that the above code will print out a series data type. If we are to get a dataframe data type,
# asthe data type, we double the square bracket like...
# print(Lending_data[['Location']])
# print(type(Lending_data[['Location']]))

# In order to access more than 1 column at a time, we use
# print(Lending_data.head()[['Location', 'Product']])

# We can also decide to store the column name in a variation to allow more easy accessibility
loc_prod = ['Location', 'Product']
print(Lending_data.head()[loc_prod])


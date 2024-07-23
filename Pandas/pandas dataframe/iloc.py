import pandas as pd

data = pd.read_csv('Lending-company.csv', index_col= 'StringID')
lending_data = data.copy()

# print(lending_data.head()['Product'])

# But when using iloc, we can specify the row and column by their index numbers.
# e.g to specify the second row, we use .iloc[1]

# print(lending_data.iloc[1])

# We can also specify the column by adding a comma, e.g .iloc[1,3]. This will retun the 
# second row and the fourth column

# print(lending_data.iloc[1,3])

# to get all data in just one row, use .iloc[2, :]. The : means "all". Therfore, this prints
# all data in row 3

# print(lending_data.iloc[2,:])

# to get all data in just one column, use .iloc[:, 4]. The : means "all". Therfore, this prints
# all data in column 5

# print(lending_data.iloc[:,4])

# to get all from the row from a specifier,use the below. This will print out the 2nd and 
# 4th row with all the columns

print(lending_data.iloc[[3,1], :])

# to get all from the column from a specifier,use the below. This will print out the 2nd and 
# 4th column with all the rows

print(lending_data.iloc[:, [3,1]])



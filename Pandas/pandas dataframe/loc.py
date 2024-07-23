import pandas as pd
data = pd.read_csv('Lending-company.csv', index_col= 'StringID')
lending_data = data.copy()

# print(lending_data)

# to get the whole data of a specific row using loc, use the syntax below

# print(lending_data.loc['LoanID_4', :])

# to get the specific data of a particular row and column, use the below syntax

# print(lending_data.loc['LoanID_3', 'Region'])

# to get the whole data of a specific column using loc, use the syntax below

print(lending_data.loc[:, 'Location'])

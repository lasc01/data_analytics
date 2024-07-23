#Creating a data frame from an external data set via importing

import pandas as pd

data = pd.read_csv('Lending-company.csv', index_col='LoanID')
lending_data = data.copy()

print(lending_data.head())
# prints out number of index(rows)
print(lending_data.index) 
# prints out all names of columns
print(lending_data.columns)
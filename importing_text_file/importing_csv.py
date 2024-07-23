import pandas as pd
landing_company = "importing_text_file/Lending-company.csv"
show_table = pd.read_csv(landing_company, index_col = "LoanID")
# print(show_table)

# use index_col parameter to make LoanID the default index column
# im order to select some particular columns you are only interested in
# use the usecols parameter. E.g below

show_table = pd.read_csv(landing_company, 
                         usecols =["StringID", "Location", "Region"], 
                         index_col = "StringID"
                         )
# print(show_table.head())
# print(show_table)

# the delimiter and sep parameter are similar. They tend to make ever row a
# string, thereby arranging the column in the right way

landing_company = "importing_text_file/Lending-company.csv"
show_table = pd.read_csv(landing_company, 
                         sep = "\,", 
                         engine = "python",
                         index_col = "LoanID")
# print(show_table)

# importing data with squeeze method

show_table = pd.read_csv(landing_company, 
                         usecols =["StringID"]
                         )
df_squeeze = show_table.squeeze("columns")
print(df_squeeze)
print(type(df_squeeze))


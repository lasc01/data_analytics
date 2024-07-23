import pandas as pd
lending_com_loc = "importing_text_file/Lending-company.xlsx"
lending_com_data_val = pd.read_excel(lending_com_loc, sheet_name="Sheet1")
print(lending_com_data_val)
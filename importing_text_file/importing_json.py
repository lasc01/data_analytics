import pandas as pd
lending_com_loc = "importing_text_file/Lending-company.json"
lending_com_data_val = pd.read_json(lending_com_loc)

print(type(lending_com_data_val))
print(lending_com_data_val)
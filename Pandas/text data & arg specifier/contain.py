import pandas as pd
names = pd.Series(["Martin Peterson", "John Fitzpatrick", "Kate Cruz"])
last_names = names.str.split().str[1]

contains_s = last_names.str.contains('s')

print(contains_s)
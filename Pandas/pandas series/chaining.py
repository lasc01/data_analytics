import pandas as pd

data = pd.read_csv('Location.csv')

location_data = data.copy()

# the below is an example of attribute chainning

location_data.index.name = "Index"

# print(location_data.index.name)

# the below is an example of method chainning

print(location_data.sort_values(by="Location").head())
import pandas as pd

data = pd.read_csv("/Users/mac/Documents/Data Analytics/Location.csv")
location_data = data.copy()

# print(type(location_data))
# print(data.describe())

print(location_data.nunique())
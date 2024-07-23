import pandas as pd

data = pd.read_csv('Location.csv')

location_data = data.copy()

location_data_sv = location_data.sort_values(by='Location', ascending=False)

location_data_sv.index.sort_values(ascending=False)

# print(location_data_sv.index.sort_values(ascending=False))

print(location_data_sv.sort_index())
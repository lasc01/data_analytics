import pandas as pd

data = pd.read_csv('Location.csv')

location_data = data.copy()

# numbers = pd.Series([15, 1000, 453, 200, 320])

# print(numbers.sort_values(ascending=False))

print(location_data.sort_values(by='Location', ascending=False))

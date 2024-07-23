import pandas as pd
import matplotlib.pyplot as plt

df_used_cars = pd.read_csv("data viz/bar_chart_data.csv")

print(df_used_cars)

plt.bar(x=df_used_cars['Brand'], 
        height=df_used_cars['Cars Listings'])

plt.show
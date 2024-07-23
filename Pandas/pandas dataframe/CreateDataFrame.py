import pandas as pd

# first method of creating a DataFrame is by creating a Dict, wit a list inside it
# dictionary of list + specifying index

data = {
    "productName": ["Apple", "Mango", "Banana"], 
    "productPrice": [300, 100, 500]
    }

index_ID = ["A", "B", "C"]

# Another method of creatting a dataframe is by creating a list with Dicts inside
# list of dictionary

data = [{"productName": "Apple", "productPrice": 300},
        {"productName": "Mango", "productPrice": 300}, 
        {"productName": "Banana", "productPrice": 300}]

df = pd.DataFrame(data, index = index_ID)

# print(df)

# another method of creating a DataFrame is by creating a Dict, wit a list inside it
# dictionary of list

data = {
    "Name": ["Amy White", "Jack Stewart", "Richard Lauderdale", "Sara Johnson"],
    "Age": [50, 53,35, 43],
    "working Experience(Yrs.)": [5, 8, 3, 10]
}

df = pd.DataFrame(data)

# print(df)

# method 4 is dictionary of pandas series

ser_product = pd.Series(["Apple", "Mango", "Banana"], index=["A", "B", "C"])
ser_price = pd.Series([300, 100, 500], index=["A", "B", "C"])

df = pd.DataFrame({"product_name": ser_product, "product_price": ser_price})

# print(df)

# method 5 is list of list

data = [["Apple", 300], ["Mango", 100], ["Banana", 500]]
df = pd.DataFrame(data)
df.columns = ["product_name", "product_price"]
df.index = ["A", "B", "C"]

# print(df)

#method 6 is the professional way

df = pd.DataFrame(
    data = [["Apple", 300], ["Mango", 100], ["Banana", 500]],
    columns = ["product_name", "product_price"],
    index = ["A", "B", "C"]
)

print(df)


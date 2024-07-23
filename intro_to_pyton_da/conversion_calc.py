
# # Where USD is the base currency you want to use
# url = 'https://v6.exchangerate-api.com/v6/93c02bc1eba287ef7dd91d9e/latest/USD'

# # Making our request
# response = requests.get(url)
# data = response.json()

# # Your JSON object with ident 4 making result look prettier
# print(json.dumps(data, indent=4))


import requests

date = input("Please enter the date in this format 'yyyy-mm-dd' or 'latest': ")
base = input("Convert from (currency): ")
curr = input("Convert to (currency): ")
quan = float(input("How much {} do you want to convert: ".format(base)))

base_url = "https://v6.exchangerate-api.com/v6/93c02bc1eba287ef7dd91d9e/"

url = base_url + "latest/" + base
response = requests.get(url)

if response.ok:
    data = response.json()
    if 'error' in data:
        print("\nError: {}".format(data['error']))
    else:
        rate = data['conversion_rates'][curr]
        result = quan * rate
        print("{} {} is equal to {} {} as at {}".format(quan, base, result, curr, date))
else:
    print("\nError: {}".format(response.status_code))

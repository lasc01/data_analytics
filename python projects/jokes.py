import requests
import json

base_url = "https://official-joke-api.appspot.com/jokes"

url_programming = base_url + "/programming/random"

r = requests.get(url_programming)

data = r.json()

print(json.dumps(data, indent = 4))
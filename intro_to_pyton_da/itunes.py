import requests
import json
import pandas as pd

base_url = "https://itunes.apple.com/search"
# url = base_url + "?term=drake&country=us"
# another way of automatically incorporating the parameter is 
r = requests.get(base_url, params = {"term": "drake", "country": "us"})
info = r.json()
# print(info.keys())
# there are 2 keys here

# print(json.dumps(info, indent = 4))
# print the first in the result key only

# print(json.dumps(info['results'][1], indent=4))

# this will print out the title name of the first track
# print(info['results'][0]['trackName'])

# This prints out all 50 tack names
# for result in info['results']:
    # print(result['releaseDate'])

# to structure this as as a dataframe using pandas
song_df =pd.DataFrame(info['results'])
print(song_df)
